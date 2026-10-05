"""Matches every Survey 3 reference (DOI and normalised title) against the Retraction Watch Database
(Crossref open dataset, https://gitlab.com/crossref/retraction-watch-data) and writes
Survey3_method_workbook/retraction_check_list.md.
Usage (from github/s): python3 tools/retraction_check.py path/to/retraction_watch.csv"""
import csv, os, re, sys, unicodedata, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from biblib import parse, clean
from make_data_package import study_name, ident, W, level
S = os.path.dirname(HERE) + '/'
BIB = parse(S + 'Survey3_TNNLS_LaTeX_Overleaf/refs.bib')
csv.field_size_limit(10**9)
def norm(t): return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', clean(t)).encode('ascii', 'ignore').decode().lower())
dois, titles, n, last = set(), set(), 0, ''
for r in csv.DictReader(open(sys.argv[1], encoding='utf-8', errors='replace')):
    n += 1
    for k in ('OriginalPaperDOI', 'RetractionDOI'):
        if r.get(k): dois.add(r[k].strip().lower())
    if len(norm(r['Title'])) > 25: titles.add(norm(r['Title']))
    d = (r.get('RetractionDate') or '').split()[0]
    try:
        d = datetime.datetime.strptime(d, '%m/%d/%Y').date().isoformat()
        last = max(last, d)
    except ValueError: pass
hits = []
for k, (t, f) in BIB.items():
    doi = clean(f.get('doi', '')).lower()
    if (doi and doi in dois) or norm(f.get('title', '')) in titles: hits.append(k)
nd = sum(1 for _, f in BIB.values() if f.get('doi'))
L = ['# Retraction check list (Survey 3)', '',
     'Result (%s): all %d references of Survey 3 (%d with a DOI; titles for all) were matched automatically against the full' % (datetime.date.today().strftime('%-d %B %Y'), len(BIB), nd),
     'Retraction Watch Database (Crossref open dataset, https://gitlab.com/crossref/retraction-watch-data,',
     '%s records, latest retraction date %s). ' % (format(n, ','), last) +
     ('No match: none of the cited works has been retracted.' if not hits else 'Matches requiring attention: ' + ', '.join(hits) + '.'),
     '', 'Preprints without a DOI are matched by title only; the check should be repeated before submission and before each revision.', '',
     '| # | Study | Evidence level | DOI or identifier | Retracted |', '|---|---|---|---|---|']
for i, e in enumerate(W, 1):
    L.append('| %d | %s | %s | %s | %s |' % (i, study_name(e['key']), level(e), ident(e['key']) or '—', 'Yes' if e['key'] in hits else 'No'))
open(S + 'Survey3_method_workbook/retraction_check_list.md', 'w').write('\n'.join(L) + '\n')
print(n, last, hits)
