"""Writes the Survey 3 reference list, the download checklist and the full-text index:
  Survey3_reference_list.md, Survey3_download_links.md, Survey3_fulltexts/index.csv
Run from github/s:  python3 tools/make_reference_list.py
A full text counts as present when Survey3_fulltexts/primary/<key>.pdf or references/<key>.pdf exists."""
import csv, os, re, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from biblib import parse, clean, authors, venue, ident, esc
S = os.path.dirname(HERE) + '/'
BIB = parse(S + 'Survey3_TNNLS_LaTeX_Overleaf/refs.bib')
EXT = {r['Key']: r for r in csv.DictReader(open(S + 'Survey3_data_package/extraction_table.csv', encoding='utf-8-sig'))}
SUM = {r['Key']: r for r in csv.DictReader(open(S + 'Survey3_data_package/study_summaries.csv', encoding='utf-8-sig'))}
FT = S + 'Survey3_fulltexts/'
METHOD = {'Page2021', 'Kitchenham2007'}
OWN = {'Guru2026a', 'Guru2026b', 'Guru2026c'}


def group(k):
    if k in METHOD: return 'method'
    if k in OWN: return 'companion'
    L = EXT[k]['Evidence level']
    return 'primary' if L.startswith('E') else ('review' if L == 'R' else 'software')


def present(k):
    for sub in ('primary', 'references'):
        if os.path.exists(FT + sub + '/' + k + '.pdf'): return sub + '/' + k + '.pdf'
    return ''


def links(f):
    out = []
    if f.get('doi'): out.append('[DOI](https://doi.org/%s)' % clean(f['doi']))
    m = re.search(r'(\d{4}\.\d{4,5})', ' '.join(f.get(x, '') for x in ('eprint', 'journal', 'note', 'url', 'howpublished')))
    if m: out += ['[arXiv](https://arxiv.org/abs/%s)' % m.group(1), '[PDF](https://arxiv.org/pdf/%s)' % m.group(1)]
    elif f.get('url') and not f.get('doi'): out.append('[Link](%s)' % clean(f['url']))
    out.append('[Scholar](https://scholar.google.com/scholar?q=%s)' % urllib.parse.quote_plus(clean(f.get('title', ''))))
    return ' · '.join(out)


keys = list(BIB)
# ---- index.csv
with open(FT + 'index.csv', 'w', encoding='utf-8-sig', newline='') as fh:
    wr = csv.writer(fh); wr.writerow(['Citation key', 'Group', 'Evidence level', 'Title', 'File (or MISSING)'])
    for k in keys:
        wr.writerow([k, group(k), EXT[k]['Evidence level'] if k in EXT else '', clean(BIB[k][1].get('title', '')), present(k) or ('not applicable' if k in OWN else 'MISSING')])

# ---- reference list
from collections import Counter
G = Counter(group(k) for k in keys); M = Counter(group(k) for k in keys if not present(k) and k not in OWN)
L = ['# Survey 3 — reference list (IEEE Transactions on Neural Networks and Learning Systems)', '',
     '**Meta-Learning Orchestration of Learning Modalities on Resource-Constrained Robots: A Systematic Review**  ',
     'Yeshwanth Guru and Dev Kunwar Singh Chauhan · generated from `Survey3_TNNLS_LaTeX_Overleaf/refs.bib`, `Survey3_fulltexts/index.csv` and the data package', '',
     '| Group | Cited | Full text missing |', '|---|---|---|']
for g, lab in [('primary', 'Primary studies (E2–E5)'), ('review', 'Reviews'), ('software', 'Software, datasets, benchmarks'), ('method', 'Method references'), ('companion', 'Companion manuscripts')]:
    L.append('| %s | %d | %d |' % (lab, G[g], M[g]))
L.append('| **Total** | **%d** | **%d** |' % (len(keys), sum(M.values())))
L += ['', 'None of the 180 reviewed works is cited in Survey 1 or Survey 2 (title match). Full texts go in `Survey3_fulltexts/` '
      '(private: never upload with the submission). Verification notes come from the data package.', '',
      '| # | Key | Authors | Year | Title | Venue | Identifier | Level | Full text | Verification note |', '|---|---|---|---|---|---|---|---|---|---|']
for i, k in enumerate(keys, 1):
    t, f = BIB[k]
    L.append('| %d | `%s` | %s | %s | %s | %s | %s | %s | %s | %s |' % (i, k, esc(authors(f.get('author', ''))) or '—', clean(f.get('year', '')),
             esc(clean(f.get('title', ''))), esc(venue(t, f)) or '—', esc(ident(f)), EXT[k]['Evidence level'] if k in EXT else '—',
             'yes' if present(k) else ('—' if k in OWN else 'missing'), esc(SUM[k]['Verification_note']) if k in SUM else ''))
open(S + 'Survey3_reference_list.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# ---- download checklist
D = ['# Survey 3 — papers to download manually', '',
     'No full text of the 180 reviewed works is in the repository. Save each paper as `<key>.pdf` in '
     '`github/s/Survey3_fulltexts/primary/` (primary studies) or `references/` (reviews and software), rerun '
     '`python3 tools/make_reference_list.py`, check the write-up and the appraisal codes against the full text, and '
     'record any changed code in `Survey3_data_package/quality_appraisal.csv`.', '',
     'Order: real-robot studies first (they carry the evidence profile), then the core works, then the rest. Each entry has '
     'a DOI or arXiv link where one exists, and always a Google Scholar search.', '']
def item(k):
    t, f = BIB[k]; e = EXT[k]
    return '- [ ] `%s` [%s; %s] — %s (%s). *%s*. %s. %s' % (k, e['Evidence level'], e['Role'].lower(), authors(f.get('author', '')),
            clean(f.get('year', '')), clean(f.get('title', '')), venue(t, f) or 'arXiv preprint', links(f))
sets = [('Real-robot studies (E4, E5)', [k for k in keys if k in EXT and EXT[k]['Evidence level'] in ('E4', 'E5') and not present(k)]),
        ('Core works at E2 or E3', [k for k in keys if k in EXT and EXT[k]['Evidence level'] in ('E2', 'E3') and EXT[k]['Role'] == 'Core' and not present(k)]),
        ('Other works at E2 or E3', [k for k in keys if k in EXT and EXT[k]['Evidence level'] in ('E2', 'E3') and EXT[k]['Role'] != 'Core' and not present(k)]),
        ('Reviews, software and datasets', [k for k in keys if k in EXT and EXT[k]['Evidence level'] in ('R', 'S') and not present(k)])]
for title, ks in sets:
    D += ['## %s (%d)' % (title, len(ks)), ''] + [item(k) for k in ks] + ['']
D += ['## Candidates from the targeted search of 4 October 2026 (not yet included)', '',
      '- [ ] Zhang, Mehradfar, Dimitriadis and Avestimehr (2025). *Leveraging Uncertainty Estimation for Efficient LLM Routing*. arXiv:2502.11021. [arXiv](https://arxiv.org/abs/2502.11021) · [PDF](https://arxiv.org/pdf/2502.11021)',
      '- [ ] Guan, Hu, Li and Cheng (2025). *Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey*. arXiv:2510.17111. [arXiv](https://arxiv.org/abs/2510.17111) · [PDF](https://arxiv.org/pdf/2510.17111)',
      '- [ ] Vats, Konidaris et al. (2026). *Deliberate Practice: Learning Robot Skills under a Budget*. arXiv:2608.13415. [arXiv](https://arxiv.org/abs/2608.13415) · [PDF](https://arxiv.org/pdf/2608.13415)',
      '- [ ] Online metareasoning for probabilistic planning (AAMAS 2026). Full record to be identified. [Scholar](https://scholar.google.com/scholar?q=online+metareasoning+probabilistic+planning+AAMAS+2026)', '']
open(S + 'Survey3_download_links.md', 'w', encoding='utf-8').write('\n'.join(D))
print(G, M)
