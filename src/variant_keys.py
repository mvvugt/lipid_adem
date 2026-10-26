#!/usr/bin/env python3
"""
Variant keys (``chrom:pos:a1:a2``) and small table helpers shared by
burden_exposure.py and compare_marvel_runs.py. Needs only pandas and
log_tools, not biomed_api (`functions`), so it runs in the Snellius env.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# imports

from __future__ import annotations

from pathlib import Path

import pandas as pd
from log_tools.emitter import log_info

from project_constants import Constants, MarvelCompareColumns

_C = MarvelCompareColumns
# the variant part of a marvel exposure / carriers column name
_VARIANT_PATTERN: str = Constants.MARVEL_VARIANT_PATTERN
_KEY_SEP: str = ":"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def variant_key(
    chrom: pd.Series, pos: pd.Series, a1: pd.Series, a2: pd.Series
) -> pd.Series:
    """Build ``chrom:pos:a1:a2`` keys, ``chr`` removed, alleles upper case.

    Parameters
    ----------
    chrom, pos, a1, a2 : `pd.Series`
        Variant details, read as text.

    Returns
    -------
    keys : `pd.Series`
        `string` dtype; NA where any part is missing or blank.
    """
    parts = [
        chrom.astype("string")
        .str.strip()
        .str.replace(r"^chr", "", regex=True, case=False)
        .str.upper(),
        pos.astype("string").str.strip(),
        a1.astype("string").str.strip().str.upper(),
        a2.astype("string").str.strip().str.upper(),
    ]
    keys = parts[0].str.cat(parts[1:], sep=_KEY_SEP)
    blank = pd.concat([p.isna() | (p == "") for p in parts], axis=1)
    return keys.mask(blank.any(axis=1))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def key_from_id(ids: pd.Series) -> pd.Series:
    """Build variant keys from marvel variant IDs (``chr:pos:a1:a2``).

    Parameters
    ----------
    ids : `pd.Series`
        Variant IDs or other exposure names (``Intercept``, ``PC1``).

    Returns
    -------
    keys : `pd.Series`
        `string` dtype; NA where the ID is not a variant.
    """
    parts = ids.astype("string").str.strip().str.extract(_VARIANT_PATTERN)
    return variant_key(parts["chrom"], parts["pos"], parts["a1"], parts["a2"])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def swap_key(keys: pd.Series) -> pd.Series:
    """Swap a1 and a2 of variant keys.

    Parameters
    ----------
    keys : `pd.Series`
        ``chrom:pos:a1:a2`` keys (NA allowed).

    Returns
    -------
    swapped : `pd.Series`
        ``chrom:pos:a2:a1``; NA where the key is NA.
    """
    parts = keys.astype("string").str.split(_KEY_SEP, expand=True)
    if parts.shape[1] != 4:
        return pd.Series(pd.NA, index=keys.index, dtype="string")
    return parts[0].str.cat([parts[1], parts[3], parts[2]], sep=_KEY_SEP)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def match_to_new(old_keys: pd.Series, new: pd.DataFrame) -> pd.DataFrame:
    """Find old variant keys in the new list.

    Tried in order: exact, the new form before normalisation, and both
    again with a1/a2 swapped (`_C.MATCH_*`).

    Parameters
    ----------
    old_keys : `pd.Series`
        Distinct old variant keys.
    new : `pd.DataFrame`
        `load_new_list` output.

    Returns
    -------
    matches : `pd.DataFrame`
        `_C.OLD_KEY`, `_C.NEW_KEY` (NA if not found), `_C.MATCH`.
    """
    old_keys = pd.Series(old_keys.unique(), dtype="string")
    exact = pd.Series(new[_C.NEW_KEY].to_numpy(), index=new[_C.NEW_KEY])
    with_orig = new.dropna(subset=["orig_key"])
    with_orig = with_orig[with_orig["orig_key"] != with_orig[_C.NEW_KEY]]
    orig = pd.Series(
        with_orig[_C.NEW_KEY].to_numpy(), index=with_orig["orig_key"]
    )
    orig = orig[~orig.index.duplicated()]
    swapped = swap_key(old_keys)
    new_key = pd.Series(pd.NA, index=old_keys.index, dtype="string")
    match = pd.Series(_C.MATCH_NONE, index=old_keys.index, dtype="string")
    lookups = (
        (exact, old_keys, _C.MATCH_EXACT),
        (orig, old_keys, _C.MATCH_ORIG),
        (exact, swapped, _C.MATCH_SWAPPED),
        (orig, swapped, _C.MATCH_SWAPPED_ORIG),
    )
    for table, keys, label in lookups:
        found = keys.map(table).astype("string")
        todo = new_key.isna() & found.notna()
        new_key[todo] = found[todo]
        match[todo] = label
    return pd.DataFrame(
        {_C.OLD_KEY: old_keys, _C.NEW_KEY: new_key, _C.MATCH: match}
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _join_unique(values: pd.Series) -> str:
    """Join the distinct non-blank values of a group with ``,``.

    Parameters
    ----------
    values : `pd.Series`
        Text values.

    Returns
    -------
    joined : `str`
        Distinct values in first-seen order.
    """
    kept = [str(v) for v in values.dropna() if str(v) != ""]
    return ",".join(dict.fromkeys(kept))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def _write_table_atomic(df: pd.DataFrame, path: Path) -> None:
    """Write a gzipped TSV atomically (stage-then-move).

    Same as `functions.write_table_atomic`, which is not imported here
    because `functions` needs biomed_api.

    Parameters
    ----------
    df : `pd.DataFrame`
        Table to write.
    path : `Path`
        Destination ``.tsv.gz``; its directory is created if needed.

    Returns
    -------
    `None`
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    df.to_csv(tmp_path, sep="\t", index=False, na_rep="NA",
              compression="gzip")
    tmp_path.replace(path)
    log_info(f"wrote {len(df)} rows to {path}")
