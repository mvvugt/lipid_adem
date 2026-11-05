#!/usr/bin/env python3
"""
Archive a batch of results/output and results/figures files per label.

Runs the same locally, on Myriad and on Snellius (stdlib + log_tools, no
pandas). Each file is put in an archive group (`GROUP_RULES`, by label
in its name) and gets a status:

- current: written with the newest files of its group;
- stale: more than `STALE_HOURS` older than the newest file of its group
  (not rewritten by the last run);
- redundant: an output equal to another set (ClinVar adds no carriers:
  lof = ptv, ptv_clinvar_am = ptv_am, am_clinvar ~ am; unoriented = the
  oriented run for the LoF sets);
- retired: a group the pipeline no longer writes (`RETIRED_GROUPS`).

Shared inputs (`KEEP`) and files matching no rule are never moved; the
latter are listed as unclassified.

Dry run by default: writes nothing, logs the move list. With `--apply`,
per group under `Paths.ARCHIVE / <tag> / <group>/`:

1. a group with more than `TAR_MIN_FILES` files gets `output.tar.gz` and
   `figures.tar.gz` (paths relative to the project root, so extracting
   in the root restores them); smaller groups get plain copies;
2. each tarball or copy is written to a `.tmp` name, verified (names and
   sizes for tarballs, md5 for copies), then renamed;
3. `README.md` (outside the tarballs) = the hand-written text in
   `Paths.README_TEXT / <group>.md` plus a generated part: dates,
   commits, a table of files with status and the tarball md5s;
4. only then are the originals removed.

Writes `inventory.tsv.gz` and an index `README.md` in the tag directory.
An existing tag directory is never overwritten.

Code version per file: the git HEAD committed before its mtime, and the
RUN_LOG.md commit of the meta-analysis run with the same `--label` when
RUN_LOG.md still holds it (one entry per script, so only the last run).
On a machine that copied the files (local), mtimes are copy times.

Requires log_tools installed (pip install log_tools) for RUN_LOG.md
logging.
"""
from __future__ import annotations


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

import argparse
import csv
import gzip
import hashlib
import re
import shutil
import subprocess
import tarfile
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

from log_tools.emitter import log_info, log_stage, log_warn
from log_tools.setup import runlog_setup

from project_constants import Paths, RunlogOrder

# shared inputs of the meta-analysis and figures: stay in place
KEEP = frozenset({
    "merged_associations.tsv.gz", "matched_variants.tsv.gz",
    "matched_burden.tsv.gz", "matched_region_variants.tsv.gz",
    "study_effect_scale.tsv.gz", "burden_exposure_summary.tsv.gz",
    ".gitkeep", ".DS_Store",
})
# label substring -> group; first match wins, so the longer labels first
GROUP_RULES = (
    ("annotated_eur_unoriented", "annotated_eur_unoriented"),
    ("annotated_eur", "annotated_eur"),
    ("maf_filter_all", "maf_filter_all"),
    ("region_rare", "region_rare"),
    ("thomassen_ad_lists", "lists_early"),
    ("thomassen_ad_ptv_clinvar", "lists_early"),
    ("dementia_lists", "lists_early"),
    ("apoe_genotype", "apoe_genotype"),
)
# burden_/meta_<ANC>.tsv.gz without a label: the broad per-variant IVW run
BROAD_GROUP = "broad_per_variant"
# files from before the labelled pipeline (not "old*": .gitignore)
SNAPSHOT_GROUP = "early_snapshots"
SNAPSHOT_NAMES = frozenset({
    "CETP_PTV_results.tsv.gz", "final_results.tsv", "final_results.tsv.gz",
    "meta_variant.tsv.gz",
})
RETIRED_GROUPS = frozenset({"lists_early", SNAPSHOT_GROUP})
VARIANT_SETS = ("ptv_clinvar_am", "am_clinvar", "ptv_am", "clinvar", "ptv",
                "gof", "am")
# suffixes after the set, longest first
VARIANTS = ("apoe_strata_no_apoe_e2e4_directed_only",
            "apoe_strata_no_apoe_e2e4", "apoe_strata_directed_only",
            "no_apoe_e2e4_directed_only", "apoe_strata", "no_apoe_e2e4",
            "directed_only")
# lof-default groups and their duplicate sets: set -> the set it equals
REDUNDANT_GROUPS = frozenset({"annotated_eur", "maf_filter_all"})
REDUNDANT_SETS = {"lof": "ptv", "ptv_clinvar_am": "ptv_am",
                  "am_clinvar": "am (near-identical)"}
FIGURE_OUTCOMES = re.compile(
    r"_(all_cause_dementia|alzheimers_dementia|vascular_dementia|"
    r"frontotemporal_dementia|ascvd|CETP)$"
)
RESULT_RE = re.compile(r"^(?:burden|meta)_(?:EUR|MULTI)(?:_(?P<rest>.+))?"
                       r"\.tsv\.gz$")
FIGURE_RE = re.compile(r"^(?:forest|heatmap)_(?:[a-z]+?)_(?P<rest>.+)\.pdf$")
RUNLOG_HEADER = re.compile(r"^## \[\d+\] meta_analysis \(`(?P<cmd>.*)`\)")
STALE_HOURS = 6
TAR_MIN_FILES = 5
INVENTORY_COLUMNS = ("path", "kind", "group", "label", "variant_set",
                     "variant", "mtime", "size_kb", "head_at_mtime",
                     "runlog_commit", "status", "reason")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# classification

@dataclass
class Entry:
    """One results file and its archive metadata."""
    path: Path
    kind: str
    group: str
    label: str = ""
    variant_set: str = ""
    variant: str = ""
    mtime: datetime = field(default_factory=datetime.now)
    head_at_mtime: str = ""
    runlog_commit: str = ""
    status: str = ""
    reason: str = ""

    def row(self, root: Path) -> dict[str, str]:
        """Return the inventory row of this entry."""
        return {
            "path": str(self.path.relative_to(root)),
            "kind": self.kind,
            "group": self.group,
            "label": self.label,
            "variant_set": self.variant_set,
            "variant": self.variant,
            "mtime": self.mtime.strftime("%Y-%m-%d %H:%M"),
            "size_kb": f"{self.path.stat().st_size / 1024:.0f}",
            "head_at_mtime": self.head_at_mtime,
            "runlog_commit": self.runlog_commit,
            "status": self.status,
            "reason": self.reason,
        }


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def split_label(rest: str) -> tuple[str, str, str]:
    """Split a file-name remainder into its label, variant set and variant.

    Parameters
    ----------
    rest : `str`
        The part after ``burden_<ANC>_`` (or after the figure kind),
        without extension and outcome, e.g.
        ``annotated_eur_ptv_am_apoe_strata``.

    Returns
    -------
    label, variant_set, variant : `tuple` [`str`, `str`, `str`]
        E.g. ``("annotated_eur", "ptv_am", "apoe_strata")``; an empty
        string when absent.
    """
    variant = ""
    for name in VARIANTS:
        if rest == name or rest.endswith(f"_{name}"):
            variant = name
            rest = rest[: -len(name)].rstrip("_")
            break
    variant_set = ""
    for name in VARIANT_SETS:
        if rest.endswith(f"_{name}"):
            variant_set = name
            rest = rest[: -len(name) - 1]
            break
    return rest, variant_set, variant


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def classify(path: Path) -> Entry | None:
    """Return the archive entry of a results file.

    Parameters
    ----------
    path : `Path`
        A file under results/output or results/figures.

    Returns
    -------
    entry : `Entry` or `None`
        `None` for a shared input (`KEEP`); group ``unclassified`` for a
        file matching no rule (never moved).
    """
    name = path.name
    if name in KEEP:
        return None
    kind = "output" if Paths.OUTPUT in path.parents else "figure"
    mtime = datetime.fromtimestamp(path.stat().st_mtime)
    if name in SNAPSHOT_NAMES or name.endswith(".zip"):
        return Entry(path, kind, SNAPSHOT_GROUP, mtime=mtime)
    m_res, m_fig = RESULT_RE.match(name), FIGURE_RE.match(name)
    if m_res:
        rest = m_res.group("rest") or ""
    elif m_fig:
        rest = FIGURE_OUTCOMES.sub("", m_fig.group("rest"))
        rest = rest.removeprefix("sets_")
    else:
        return Entry(path, kind, "unclassified", mtime=mtime)
    label, variant_set, variant = split_label(rest)
    if "genotype" in label:
        group = "apoe_genotype"
    elif not label:
        group = BROAD_GROUP
    else:
        # match on the unsplit name: a set suffix can be part of a label
        # (thomassen_ad_ptv_clinvar)
        group = next(
            (g for pattern, g in GROUP_RULES if pattern in rest), ""
        )
        if not group:
            return Entry(path, kind, "unclassified", label=label,
                         mtime=mtime)
    if not variant_set and group in REDUNDANT_GROUPS | {
        "annotated_eur_unoriented"
    }:
        variant_set = "lof"
    return Entry(path, kind, group, label, variant_set, variant, mtime)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def set_status(entries: list[Entry]) -> None:
    """Fill `status` and `reason` of each entry in place.

    Parameters
    ----------
    entries : `list` [`Entry`]
        All classified entries; the newest mtime per group sets the
        stale cut-off.

    Returns
    -------
    `None`
    """
    newest: dict[str, datetime] = {}
    for e in entries:
        newest[e.group] = max(newest.get(e.group, e.mtime), e.mtime)
    for e in entries:
        if e.group == "unclassified":
            e.status, e.reason = "unclassified", "matches no rule: not moved"
        elif e.group in RETIRED_GROUPS:
            e.status = "retired"
            e.reason = "no longer written by src/lipid_adem.sh"
        elif newest[e.group] - e.mtime > timedelta(hours=STALE_HOURS):
            e.status = "stale"
            e.reason = (f"not rewritten by the last run of the group "
                        f"({newest[e.group]:%Y-%m-%d %H:%M})")
        elif (e.kind == "output" and e.group in REDUNDANT_GROUPS
              and e.variant_set in REDUNDANT_SETS):
            e.status = "redundant"
            e.reason = (f"equals the {REDUNDANT_SETS[e.variant_set]} set "
                        "(ClinVar adds no carriers)")
        elif (e.kind == "output" and e.group == "annotated_eur_unoriented"
              and e.variant_set != "gof"):
            e.status = "redundant"
            e.reason = "equals the oriented run (no flips in LoF sets)"
        else:
            e.status = "current"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# code versions

def head_before(mtime: datetime, cache: dict[str, str]) -> str:
    """Return the short git HEAD committed before `mtime`, with its date.

    Parameters
    ----------
    mtime : `datetime`
        File modification time.
    cache : `dict` [`str`, `str`]
        Results per minute, filled in place (one git call per minute).

    Returns
    -------
    head : `str`
        E.g. ``"ecae536 2026-10-26 15:03"``; empty outside a git repo.
    """
    key = mtime.strftime("%Y-%m-%dT%H:%M")
    if key not in cache:
        out = subprocess.run(
            ["git", "-C", str(Paths.HERE), "log", "-1",
             f"--before={key}", "--format=%h %cd",
             "--date=format:%Y-%m-%d %H:%M"],
            capture_output=True, text=True, check=False,
        )
        cache[key] = out.stdout.strip()
    return cache[key]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def runlog_commits(path: Path) -> dict[str, str]:
    """Return the RUN_LOG.md commit of the meta_analysis run per label.

    Parameters
    ----------
    path : `Path`
        RUN_LOG.md; missing is fine (empty result).

    Returns
    -------
    commits : `dict` [`str`, `str`]
        ``--label`` value -> ``"<commit> (<last run>)"``.
    """
    commits: dict[str, str] = {}
    if not path.exists():
        return commits
    label, last_run = "", ""
    for line in path.read_text().splitlines():
        header = RUNLOG_HEADER.match(line)
        if line.startswith("## "):
            label = ""
            if header:
                m = re.search(r"--label (\S+)", header.group("cmd"))
                label = m.group(1) if m else ""
        elif label and line.startswith("- last run:"):
            last_run = line.split(":", 1)[1].strip()
        elif label and line.startswith("- commit:"):
            commit = line.split(":", 1)[1].strip().replace("`", "")
            commits[label] = f"{commit} ({last_run})"
    return commits


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def collect(results_dirs: tuple[Path, ...]) -> list[Entry]:
    """Classify every file below `results_dirs` and add versions.

    Parameters
    ----------
    results_dirs : `tuple` [`Path`, ...]
        Directories to scan recursively.

    Returns
    -------
    entries : `list` [`Entry`]
        Sorted by group and path.
    """
    paths = sorted(
        p for d in results_dirs if d.exists()
        for p in d.rglob("*") if p.is_file()
    )
    entries = [e for e in map(classify, paths) if e is not None]
    set_status(entries)
    cache: dict[str, str] = {}
    commits = runlog_commits(Paths.HERE / "RUN_LOG.md")
    for e in entries:
        e.head_at_mtime = head_before(e.mtime, cache)
        full_label = "_".join(
            x for x in (e.label, "" if e.variant_set == "lof"
                        else e.variant_set) if x
        )
        e.runlog_commit = commits.get(full_label, "")
    return sorted(entries, key=lambda e: (e.group, str(e.path)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# writing

def md5sum(path: Path) -> str:
    """Return the md5 hex digest of a file, read in 1 MiB chunks."""
    digest = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_tarball(entries: list[Entry], target: Path) -> str:
    """Write and verify a tarball of `entries`; return its md5.

    Parameters
    ----------
    entries : `list` [`Entry`]
        Files to pack, stored relative to `Paths.HERE`.
    target : `Path`
        Final ``.tar.gz`` path; written as ``<target>.tmp`` first.

    Returns
    -------
    md5 : `str`
        md5 of the verified tarball.

    Raises
    ------
    RuntimeError
        If the tarball's names or sizes differ from the files.
    """
    tmp = target.with_name(target.name + ".tmp")
    with tarfile.open(tmp, "w:gz") as tar:
        for e in entries:
            tar.add(e.path, arcname=str(e.path.relative_to(Paths.HERE)))
    expected = {str(e.path.relative_to(Paths.HERE)): e.path.stat().st_size
                for e in entries}
    with tarfile.open(tmp, "r:gz") as tar:
        found = {m.name: m.size for m in tar.getmembers() if m.isfile()}
    if found != expected:
        tmp.unlink()
        raise RuntimeError(f"{target}: tarball does not match its files")
    tmp.replace(target)
    return md5sum(target)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def copy_verified(entry: Entry, target_dir: Path) -> str:
    """Copy one file into `target_dir`, verify its md5; return the md5.

    Raises
    ------
    RuntimeError
        If the copy's md5 differs from the original's.
    """
    target = target_dir / entry.path.name
    tmp = target.with_name(target.name + ".tmp")
    shutil.copy2(entry.path, tmp)
    md5 = md5sum(entry.path)
    if md5sum(tmp) != md5:
        tmp.unlink()
        raise RuntimeError(f"{target}: copy does not match {entry.path}")
    tmp.replace(target)
    return md5


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def group_readme(group: str, entries: list[Entry],
                 packed: dict[str, str]) -> str:
    """Return the README.md text of one archive group.

    Parameters
    ----------
    group : `str`
        Archive group.
    entries : `list` [`Entry`]
        The group's files.
    packed : `dict` [`str`, `str`]
        Archive member (tarball or file name) -> md5.

    Returns
    -------
    text : `str`
        The hand-written part (`Paths.README_TEXT / <group>.md`,
        a placeholder when missing) plus the generated part.
    """
    text_path = Paths.README_TEXT / f"{group}.md"
    if text_path.exists():
        text = text_path.read_text().rstrip() + "\n"
    else:
        log_warn(f"{text_path} missing: README gets a placeholder")
        text = f"# {group}\n\n(no description in {text_path})\n"
    mtimes = [e.mtime for e in entries]
    heads = sorted({e.head_at_mtime for e in entries if e.head_at_mtime})
    commits = sorted({e.runlog_commit for e in entries if e.runlog_commit})
    lines = [
        text,
        "## Generated by `src/archive_results.py`",
        "",
        f"- archived: {datetime.now():%Y-%m-%d %H:%M} on "
        f"{Paths.HERE}",
        f"- files: {len(entries)}, written {min(mtimes):%Y-%m-%d %H:%M} "
        f"to {max(mtimes):%Y-%m-%d %H:%M} (mtime; copy time if copied)",
        "- git HEAD at those times: " + ("; ".join(heads) or "unknown"),
        "- RUN_LOG.md meta_analysis commit: "
        + ("; ".join(commits) or "not in RUN_LOG.md (only the last run "
           "per script is kept)"),
        "- restore: `tar xzf <tarball>` in the project root",
        "",
        "| Archive member | md5 |",
        "|---|---|",
        *(f"| `{name}` | `{md5}` |" for name, md5 in packed.items()),
        "",
        "| File | Set | Variant | Written | Status | Reason |",
        "|---|---|---|---|---|---|",
        *(f"| `{e.path.relative_to(Paths.HERE)}` | {e.variant_set} | "
          f"{e.variant} | {e.mtime:%Y-%m-%d %H:%M} | {e.status} | "
          f"{e.reason} |" for e in entries),
        "",
    ]
    return "\n".join(lines)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def index_readme(tag_dir: Path, groups: dict[str, list[Entry]]) -> str:
    """Return the index README.md text of an archive tag directory."""
    lines = [
        f"# Results archive {tag_dir.name}",
        "",
        "One directory per label group; each holds a README.md (what, "
        "inputs, choices, interpretation, files) and the tarballs or "
        "files. Overview and interpretation of the whole batch: "
        "`docs/reports/results_overview.md`. All files with their "
        "status and code version: `inventory.tsv.gz`.",
        "",
        "| Group | Files | Status | Description |",
        "|---|---|---|---|",
    ]
    for group, entries in groups.items():
        text_path = Paths.README_TEXT / f"{group}.md"
        summary = ""
        if text_path.exists():
            body = [ln for ln in text_path.read_text().splitlines()
                    if ln.strip() and not ln.startswith("#")]
            summary = body[0] if body else ""
        counts: dict[str, int] = {}
        for e in entries:
            counts[e.status] = counts.get(e.status, 0) + 1
        status = ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
        lines.append(f"| [`{group}`]({group}/README.md) | {len(entries)} "
                     f"| {status} | {summary} |")
    lines += [
        "",
        "Left in `results/output` (shared inputs): "
        + ", ".join(f"`{n}`" for n in sorted(KEEP) if not n.startswith(".")),
        "",
    ]
    return "\n".join(lines)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_inventory(entries: list[Entry], path: Path) -> None:
    """Write the inventory as a gzipped TSV atomically."""
    tmp = path.with_name(path.name + ".tmp")
    with gzip.open(tmp, "wt", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=INVENTORY_COLUMNS,
                                delimiter="\t")
        writer.writeheader()
        writer.writerows(e.row(Paths.HERE) for e in entries)
    tmp.replace(path)
    log_info(f"wrote {len(entries)} rows to {path}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def archive_group(group: str, entries: list[Entry], tag_dir: Path) -> None:
    """Pack, verify and document one group; then remove its originals.

    Parameters
    ----------
    group : `str`
        Archive group (the directory name).
    entries : `list` [`Entry`]
        The group's files.
    tag_dir : `Path`
        Tag directory (`Paths.ARCHIVE / <tag>`).

    Returns
    -------
    `None`
    """
    group_dir = tag_dir / group
    group_dir.mkdir(parents=True)
    packed: dict[str, str] = {}
    if len(entries) > TAR_MIN_FILES:
        for kind, name in (("output", "output.tar.gz"),
                           ("figure", "figures.tar.gz")):
            part = [e for e in entries if e.kind == kind]
            if part:
                packed[name] = write_tarball(part, group_dir / name)
    else:
        for e in entries:
            packed[e.path.name] = copy_verified(e, group_dir)
    readme = group_dir / "README.md"
    readme.write_text(group_readme(group, entries, packed))
    for e in entries:
        e.path.unlink()
    log_info(f"{group}: {len(entries)} files -> {group_dir} "
             f"({', '.join(packed) if len(packed) <= 2 else 'plain files'})")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def archive_results(tag: str, apply: bool, groups_only: list[str]) -> None:
    """Classify the results files and (with `apply`) archive them.

    Parameters
    ----------
    tag : `str`
        Archive batch name: the directory under `Paths.ARCHIVE`.
    apply : `bool`
        False (default): log the move list only, write nothing.
    groups_only : `list` [`str`]
        Restrict to these groups; empty means all.

    Returns
    -------
    `None`

    Raises
    ------
    FileExistsError
        If the tag directory already exists (with `apply`).
    """
    log_stage("collect")
    entries = collect((Paths.OUTPUT, Paths.FIGURES))
    groups: dict[str, list[Entry]] = {}
    for e in entries:
        if groups_only and e.group not in groups_only:
            continue
        groups.setdefault(e.group, []).append(e)
    for group, part in groups.items():
        counts: dict[str, int] = {}
        for e in part:
            counts[f"{e.kind} {e.status}"] = counts.get(
                f"{e.kind} {e.status}", 0) + 1
        log_info(f"{group}: {len(part)} files ("
                 + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
                 + ")")
    unclassified = groups.pop("unclassified", [])
    for e in unclassified:
        log_warn(f"unclassified, not moved: {e.path}")
    if not apply:
        log_info("dry run: nothing written (use --apply)")
        return
    log_stage("archive")
    tag_dir = Paths.ARCHIVE / tag
    if tag_dir.exists():
        raise FileExistsError(f"{tag_dir} exists: choose another --tag")
    tag_dir.mkdir(parents=True)
    write_inventory([e for part in groups.values() for e in part]
                    + unclassified, tag_dir / "inventory.tsv.gz")
    for group, part in groups.items():
        archive_group(group, part, tag_dir)
    (tag_dir / "README.md").write_text(index_readme(tag_dir, groups))
    log_info(f"wrote {tag_dir / 'README.md'}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLI

def _init_cmd_args() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Archive results/output and results/figures per label "
        "group (dry run unless --apply)."
    )
    parser.add_argument(
        "--tag", default=date.today().strftime("%Y%m%d"),
        help="Archive batch directory under results/archive "
        "(default: today, YYYYMMDD).",
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Pack, verify, write READMEs and remove the originals.",
    )
    parser.add_argument(
        "--groups", nargs="*", default=[],
        help="Only these groups (default: all).",
    )
    return parser


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _parse_cmd_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    args = parser.parse_args()
    if not re.fullmatch(r"[\w.-]+", args.tag):
        parser.error(f"--tag {args.tag!r}: use letters, digits, _ . -")
    return args


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Entry point

def main() -> None:
    """Entry point for the CLI."""
    parser = _init_cmd_args()
    args = _parse_cmd_args(parser)
    with runlog_setup(root=Paths.HERE, order=RunlogOrder.ARCHIVE_RESULTS):
        archive_results(args.tag, args.apply, args.groups)


if __name__ == "__main__":
    main()
