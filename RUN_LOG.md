## [10] filter_gwas_cat (`/myriadfs/home/rmgpmva/projects/lipid_adem/src/filter_gwas_cat.py --gene ANGPTL3 --study-accession GCST90450864 --chrom 1 --start 62587567 --end 62614814 --outfile /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/gwas_filtered/ANGPTL3_GCST90450864_result.tsv.gz --source gwas_catalog`)
- first run: 2026-09-21 22:58:26
- last run: 2026-09-23 18:02:14
- commit: `2e7f9f6` (dirty)
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
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 1398, in resolve_sumstats_source
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
  File "/myriadfs/home/rmgpmva/projects/lipid_adem/src/functions.py", line 1398, in resolve_sumstats_source
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
- last run: 2026-09-23 17:44:37
- commit: `2e7f9f6`

Output:
```text
[info]  2026-09-23 17:42:38 9 genes, 50 icd codes
[info]  2026-09-23 17:42:40 EFO_0000249 -> 0 studies
[info]  2026-09-23 17:42:40 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:41 EFO_0000712 -> 0 studies
[info]  2026-09-23 17:42:41 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:43 EFO_0000713 -> 0 studies
[info]  2026-09-23 17:42:43 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:45 EFO_0001645 -> 0 studies
[info]  2026-09-23 17:42:45 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:46 EFO_0003144 -> 0 studies
[info]  2026-09-23 17:42:46 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:47 EFO_0003763 -> 0 studies
[info]  2026-09-23 17:42:47 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:49 EFO_0003777 -> 0 studies
[info]  2026-09-23 17:42:49 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:42:50 EFO_0003875 -> 0 studies
[info]  2026-09-23 17:42:50 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:03 EFO_0003913 -> 50 studies
[info]  2026-09-23 17:43:04 50 studies -> 45 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:43:05 EFO_0003914 -> 0 studies
[info]  2026-09-23 17:43:05 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:07 EFO_0004277 -> 0 studies
[info]  2026-09-23 17:43:07 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:43:30 EFO_0004614 -> 124 studies
[info]  2026-09-23 17:43:31 124 studies -> 99 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:43:58 EFO_0004615 -> 127 studies
[info]  2026-09-23 17:43:59 127 studies -> 102 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:00 EFO_0005669 -> 0 studies
[info]  2026-09-23 17:44:00 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:02 EFO_0006799 -> 1 studies
[info]  2026-09-23 17:44:02 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:04 EFO_0008583 -> 0 studies
[info]  2026-09-23 17:44:04 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:05 EFO_0008584 -> 2 studies
[info]  2026-09-23 17:44:05 2 studies -> 2 with full sumstats -> 2 included after cap=10
[info]  2026-09-23 17:44:07 EFO_0011057 -> 1 studies
[info]  2026-09-23 17:44:08 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:17 EFO_0022264 -> 52 studies
[info]  2026-09-23 17:44:17 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:28 EFO_0022266 -> 52 studies
[info]  2026-09-23 17:44:28 52 studies -> 51 with full sumstats -> 10 included after cap=10
[info]  2026-09-23 17:44:30 MONDO_0000914 -> 0 studies
[info]  2026-09-23 17:44:30 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:33 MONDO_0004648 -> 15 studies
[info]  2026-09-23 17:44:34 15 studies -> 3 with full sumstats -> 3 included after cap=10
[info]  2026-09-23 17:44:35 MONDO_0008243 -> 1 studies
[info]  2026-09-23 17:44:35 1 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:37 MONDO_0043224 -> 0 studies
[info]  2026-09-23 17:44:37 0 studies -> 0 with full sumstats -> 0 included after cap=10
[info]  2026-09-23 17:44:37 wrote 675 tasks to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/tasks.tsv
[info]  2026-09-23 17:44:37 wrote 458 study-discovery rows to /myriadfs/home/rmgpmva/projects/lipid_adem/data/temp/study_discovery_log.tsv

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
