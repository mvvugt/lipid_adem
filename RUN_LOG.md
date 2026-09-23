## [10] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene HMGCR --study-accession GCST90450864 --chrom 5 --start 75332606 --end 75370339 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/HMGCR_GCST90450864_result.tsv.gz --source gwas_catalog`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-23 14:37:50
- commit: `9224d5c`
- status: failed

Output:
```text
Traceback (most recent call last):
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 540, in _make_request
    response = conn.getresponse()
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connection.py", line 638, in getresponse
    httplib_response = super().getresponse()
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 1430, in getresponse
    response.begin()
    ~~~~~~~~~~~~~~^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 331, in begin
    version, status, reason = self._read_status()
                              ~~~~~~~~~~~~~~~~~^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 292, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/socket.py", line 719, in readinto
    return self._sock.recv_into(b)
           ~~~~~~~~~~~~~~~~~~~~^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/adapters.py", line 696, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/util/retry.py", line 510, in increment
    raise reraise(type(error), error, _stacktrace)
          ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/util/util.py", line 39, in reraise
    raise value
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 793, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 542, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 373, in _raise_timeout
    raise ReadTimeoutError(
        self, url, f"Read timed out. (read timeout={timeout_value})"
    ) from err
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Read timed out. (read timeout=30)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 240, in main
    run_filter(
    ~~~~~~~~~~^
        gene=args.gene,
        ^^^^^^^^^^^^^^^
    ...<5 lines>...
        source=args.source,
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 193, in run_filter
    filtered = _run_filter_gwas_catalog(gene, study_accession, region, outfile)
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 80, in _run_filter_gwas_catalog
    source_url, is_indexed = functions.resolve_sumstats_source(
                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        location, study_accession
        ^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 875, in resolve_sumstats_source
    response = requests.get(f"{location}/", timeout=30)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/api.py", line 87, in get
    return request("get", url, params=params, **kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/api.py", line 71, in request
    return session.request(method=method, url=url, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/sessions.py", line 651, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/sessions.py", line 784, in send
    r = adapter.send(request, **kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/adapters.py", line 742, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Read timed out. (read timeout=30)

--- error output (raw) ---
Traceback (most recent call last):
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 540, in _make_request
    response = conn.getresponse()
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connection.py", line 638, in getresponse
    httplib_response = super().getresponse()
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 1430, in getresponse
    response.begin()
    ~~~~~~~~~~~~~~^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 331, in begin
    version, status, reason = self._read_status()
                              ~~~~~~~~~~~~~~~~~^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/http/client.py", line 292, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/socket.py", line 719, in readinto
    return self._sock.recv_into(b)
           ~~~~~~~~~~~~~~~~~~~~^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/adapters.py", line 696, in send
    resp = conn.urlopen(
        method=request.method,
    ...<9 lines>...
        chunked=chunked,
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/util/retry.py", line 510, in increment
    raise reraise(type(error), error, _stacktrace)
          ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/util/util.py", line 39, in reraise
    raise value
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 793, in urlopen
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 542, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/urllib3/connectionpool.py", line 373, in _raise_timeout
    raise ReadTimeoutError(
        self, url, f"Read timed out. (read timeout={timeout_value})"
    ) from err
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Read timed out. (read timeout=30)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 240, in main
    run_filter(
    ~~~~~~~~~~^
        gene=args.gene,
        ^^^^^^^^^^^^^^^
    ...<5 lines>...
        source=args.source,
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 193, in run_filter
    filtered = _run_filter_gwas_catalog(gene, study_accession, region, outfile)
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py", line 80, in _run_filter_gwas_catalog
    source_url, is_indexed = functions.resolve_sumstats_source(
                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        location, study_accession
        ^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 875, in resolve_sumstats_source
    response = requests.get(f"{location}/", timeout=30)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/api.py", line 87, in get
    return request("get", url, params=params, **kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/api.py", line 71, in request
    return session.request(method=method, url=url, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/sessions.py", line 651, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/sessions.py", line 784, in send
    r = adapter.send(request, **kwargs)
  File "/home/rmgpmva/mambaforge/envs/biomed-api/lib/python3.13/site-packages/requests/adapters.py", line 742, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Read timed out. (read timeout=30)

```

## [10] gwas_cat_prep (`/home/rmgpmva/projects/lipid_adem/src/gwas_cat_prep.py`)
- first run: 2026-09-21 22:45:06
- last run: 2026-09-22 18:23:09
- commit: `9224d5c`

Output:
```text
[info]  2026-09-22 18:21:25 6 genes, 50 icd codes
[warn]  2026-09-22 18:21:25 No EFO term found for: F02.0A
[warn]  2026-09-22 18:21:25 No EFO term found for: Unspecified dementia
[warn]  2026-09-22 18:21:25 No EFO term found for: Delirium superimposed on dementia
[warn]  2026-09-22 18:21:25 No EFO term found for: Circumscribed brain atrophy
[warn]  2026-09-22 18:21:26 No EFO term found for: G31.09
[warn]  2026-09-22 18:21:26 No EFO term found for: Certain current complications following acute myocardial infarction
[warn]  2026-09-22 18:21:26 No EFO term found for: Vascular dementia of acute onset
[warn]  2026-09-22 18:21:26 No EFO term found for: Mixed cortical and subcortical vascular dementia
[warn]  2026-09-22 18:21:26 No EFO term found for: Vascular dementia, unspecified
[info]  2026-09-22 18:21:28 wrote resolved efo_ids to /myriadfs/home/rmgpmva/projects/lipid_adem/data/raw/icd_codes.txt
[info]  2026-09-22 18:21:29 EFO_0000249 -> 0 studies
[info]  2026-09-22 18:21:29 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:31 EFO_0000712 -> 0 studies
[info]  2026-09-22 18:21:31 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:32 EFO_0000713 -> 0 studies
[info]  2026-09-22 18:21:32 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:33 EFO_0001645 -> 0 studies
[info]  2026-09-22 18:21:33 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:35 EFO_0003144 -> 0 studies
[info]  2026-09-22 18:21:35 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:36 EFO_0003763 -> 0 studies
[info]  2026-09-22 18:21:36 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:37 EFO_0003777 -> 0 studies
[info]  2026-09-22 18:21:37 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:39 EFO_0003875 -> 0 studies
[info]  2026-09-22 18:21:39 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:47 EFO_0003913 -> 50 studies
[info]  2026-09-22 18:21:48 50 studies -> 45 with full sumstats -> 10 included after cap=10
[info]  2026-09-22 18:21:50 EFO_0003914 -> 0 studies
[info]  2026-09-22 18:21:50 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:21:51 EFO_0004277 -> 0 studies
[info]  2026-09-22 18:21:51 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:10 EFO_0004614 -> 124 studies
[info]  2026-09-22 18:22:11 124 studies -> 99 with full sumstats -> 10 included after cap=10
[info]  2026-09-22 18:22:29 EFO_0004615 -> 127 studies
[info]  2026-09-22 18:22:30 127 studies -> 102 with full sumstats -> 10 included after cap=10
[info]  2026-09-22 18:22:31 EFO_0005669 -> 0 studies
[info]  2026-09-22 18:22:31 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:33 EFO_0006799 -> 1 studies
[info]  2026-09-22 18:22:33 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:34 EFO_0008583 -> 0 studies
[info]  2026-09-22 18:22:34 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:36 EFO_0008584 -> 2 studies
[info]  2026-09-22 18:22:36 2 studies -> 2 with full sumstats -> 2 included after cap=10
[info]  2026-09-22 18:22:38 EFO_0011057 -> 1 studies
[info]  2026-09-22 18:22:38 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:46 EFO_0022264 -> 52 studies
[info]  2026-09-22 18:22:46 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-22 18:22:54 EFO_0022266 -> 52 studies
[info]  2026-09-22 18:22:54 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-22 18:22:56 MONDO_0000914 -> 0 studies
[info]  2026-09-22 18:22:56 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:22:59 MONDO_0004648 -> 15 studies
[info]  2026-09-22 18:22:59 15 studies -> 3 with full sumstats -> 3 included after cap=10
[info]  2026-09-22 18:23:01 MONDO_0008243 -> 1 studies
[info]  2026-09-22 18:23:01 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:23:03 MONDO_0043224 -> 0 studies
[info]  2026-09-22 18:23:03 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:23:04 NA -> 0 studies
[info]  2026-09-22 18:23:04 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-22 18:23:06 wrote 450 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-22 18:23:08 wrote 458 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv

```

## [10] merge_associations (`/home/rmgpmva/projects/lipid_adem/src/merge_associations.py`)
- first run: 2026-09-22 15:24:19
- last run: 2026-09-22 15:48:03
- commit: `7afbc49`

Output:
```text
[info]  2026-09-22 15:36:43 EFO_0000249 -> 0 curated associations in region
[info]  2026-09-22 15:37:00 MONDO_0004648 -> 0 curated associations in region
[info]  2026-09-22 15:42:23 EFO_0004614 -> 21 curated associations in region
[info]  2026-09-22 15:42:23 CETP -> 0 gene-burden evidence rows
[info]  2026-09-22 15:42:25 EFO_0000249 -> 0 curated associations in region
[info]  2026-09-22 15:42:41 MONDO_0004648 -> 0 curated associations in region
[info]  2026-09-22 15:48:02 EFO_0004614 -> 0 curated associations in region
[info]  2026-09-22 15:48:03 HMGCR -> 0 gene-burden evidence rows
[info]  2026-09-22 15:48:03 wrote 3110 rows to /myriadfs/home/rmgpmva/projects/lipid_adem/results/output/final_results.tsv

```
