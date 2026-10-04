"""Writes m/Survey2_download_links.md: a clickable link for every Survey 2 work whose full text is not in
Survey2_fulltexts/, plus the new papers from the literature check. Run: python3 github/m/tools/make_download_links.py"""
import csv, os, re, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), 'k', 'tools'))
from biblib import parse, clean, authors, venue, ident
M = os.path.dirname(HERE)
bib = parse(os.path.join(M, 'Survey2_AIR_LaTeX_Overleaf', 'refs.bib'))
idx = {r['Citation key']: r for r in csv.DictReader(open(os.path.join(M, 'Survey2_fulltexts', 'index.csv'), encoding='utf-8-sig'))}
col = [c for c in next(iter(idx.values())) if c.startswith('Source')][0]
lev = {}
for f in ('extraction_table.csv', 'theory_evidence_studies.csv'):
    for r in csv.DictReader(open(os.path.join(M, 'Survey2_data_package', f), encoding='utf-8-sig')):
        lev[r['Key']] = r['Evidence level']
def links(f, title):
    out = []
    i = ident(f)
    if i.startswith('doi:'):
        d = i[4:]
        out.append('[DOI](https://doi.org/%s)' % d)
        m = re.match(r'10\.48550/arXiv\.(.+)', d, re.I)
        if m: out.append('[arXiv PDF](https://arxiv.org/pdf/%s)' % m.group(1))
    elif i.startswith('arXiv:'):
        out.append('[arXiv](https://arxiv.org/abs/%s)' % i[6:]); out.append('[PDF](https://arxiv.org/pdf/%s)' % i[6:])
    elif i.startswith('http'):
        out.append('[link](%s)' % i)
    if f.get('eprint') and not any('arxiv' in o for o in out):
        out.append('[arXiv PDF](https://arxiv.org/pdf/%s)' % clean(f['eprint']))
    out.append('[Scholar](https://scholar.google.com/scholar?q=%s)' % urllib.parse.quote_plus(title))
    return ' · '.join(out)
ORDER = ['application', 'theory and evidence', 'review', 'background', 'method']
TITLE = {'application': 'Application studies — download first (needed for the quality appraisal)',
         'theory and evidence': 'Theory and evidence studies', 'review': 'Reviews', 'background': 'Background works (books may need library access)',
         'method': 'Method references'}
missing = [k for k, r in idx.items() if r[col] == 'MISSING' and k != 'Guru2026']
L = ['# Survey 2 — papers to download manually', '',
     'Cited works whose full text is not yet in the repository, and the new candidates from the literature check. '
     'Save each paper as `<key>.pdf` in `github/m/Survey2_fulltexts/primary/` (application studies) or `references/` (all others), '
     'then update `index.csv`, re-check the extraction against the full text and complete the appraisal cells that need it.', '',
     'Each entry has a DOI or arXiv link where one exists, and always a Google Scholar search (the Scholar result often has a free PDF on the right).', '',
     '| Group | Missing |', '|---|---|']
for g in ORDER:
    n = sum(1 for k in missing if idx[k]['Group'] == g)
    if n: L.append('| %s | %d |' % (g.capitalize(), n))
L += ['| **Total cited works** | **%d** |' % len(missing), '| New papers from the 4 Oct 2026 check (not yet cited) | 21 (+1 book) |', '']
for g in ORDER:
    ks = [k for k in missing if idx[k]['Group'] == g]
    if not ks: continue
    L += ['## %s (%d)' % (TITLE[g], len(ks)), '']
    for k in sorted(ks, key=str.lower):
        t, f = bib[k]; ti = clean(f.get('title', ''))
        L.append('- [ ] `%s`%s — %s (%s). *%s*. %s. %s' % (k, (' [%s]' % lev[k]) if k in lev else '', authors(f.get('author', f.get('editor', ''))) or '—',
                 clean(f.get('year', '')), ti, venue(t, f) or '—', links(f, ti)))
    L.append('')
NEW = [
 ('Romeo2026', 'Extreme Quantum Cognition Machines for Deliberative Decision Making', 'arXiv:2603.05430'),
 ('Beuria2025', 'Collective motion using quantum-like entanglement of neighbours in perceptual space', 'arXiv:2409.18985'),
 ('NonMarkovianCollective2025', 'Non-Markovian Collective Motion from Self-Regulated Perceptual Dynamics', 'arXiv:2510.23688'),
 ('SelfHealingSwarm2026', 'Self-Healing Coordination in Cognitive Swarm Agents with Bloch-Type Perceptual Memory', 'arXiv:2607.11960'),
 ('Chen2025QiNN', 'QiNN-QJ: A Quantum-inspired Neural Network with Quantum Jump for Multimodal Sentiment Analysis', 'arXiv:2510.27091'),
 ('Liu2023QPsarcasm', 'A Quantum Probability Driven Framework for Joint Multi-Modal Sarcasm, Sentiment and Emotion Analysis', 'arXiv:2306.03650'),
 ('Snow2022', 'Lyapunov based Stochastic Stability of a Quantum Decision System for Human-Machine Interaction', 'arXiv:2205.12378'),
 ('Agostino2025', 'A quantum semantic framework for natural language processing', 'arXiv:2506.10077'),
 ('Agostino2026', 'The production of meaning in the processing of natural language', 'arXiv:2603.20381'),
 ('Li2020NHB', 'Quantum reinforcement learning during human decision-making', 'doi:10.1038/s41562-019-0804-2'),
 ('Chen2022DTQW', 'On the use of discrete-time quantum walks in decision theory', 'doi:10.1371/journal.pone.0273551'),
 ('Laine2025a', 'The Quantum LLM: Modeling Semantic Spaces with Quantum Principles', 'arXiv:2504.13202'),
 ('Laine2025b', 'Quantum LLMs Using Quantum Computing to Analyze and Process Semantic Information', 'arXiv:2512.02619'),
 ('Mertova2026', 'Quantum Cognition Meets Quantum Computing: Modeling Human Reasoning for Advanced Decision Systems', 'https://aisel.aisnet.org/ecis2026/quantum/quantum/1/'),
 ('Pothukuchi2023', 'The QUATRO Application Suite: Quantum Computing for Models of Human Cognition', 'arXiv:2309.00597'),
 ('Wang2019sim', 'Simulating Cognition with Quantum Computers', 'arXiv:1905.12599'),
 ('Lawless2026', "Toward tunable advantages of quantum-like teams: the physics of interdependent teams to 'squeeze' uncertainty", 'doi:10.3389/fphy.2025.1715888'),
 ('Edwards2025', 'Further N-Frame networking dynamics of conscious observer-self agents via a functional contextual interface', 'doi:10.3389/fncom.2025.1551960'),
 ('CPB2025HBN', 'Hybrid quantum-classical multi-agent decision-making framework based on hierarchical Bayesian networks in the noisy intermediate-scale quantum era', 'doi:10.1088/1674-1056/adefd7'),
 ('EPJST2025BN', 'Recursive quantum-classical hybrid Bayesian network inference quantum decision networks EPJ Special Topics 2025', ''),
 ('Singh2025QNN', 'Quantum neural networks for multimodal sentiment, emotion, and sarcasm analysis', ''),
 ('Maksymov2026 (book)', 'Cognition in Superposition: Quantum Models in AI, Economics, Defence, Gaming and Collective Behaviour', 'doi:10.1007/978-3-032-25965-3'),
]
L += ['## New papers from the literature check of 4 October 2026 (%d)' % len(NEW), '',
      'Not yet cited; details and priorities are in `Survey2_reference_list.md` §1. Save them in `github/m/Survey2_fulltexts/candidates/` under the name given (a provisional key).', '']
for k, ti, i in NEW:
    f = {'doi': i[4:]} if i.startswith('doi:') else ({'eprint': i[6:]} if i.startswith('arXiv:') else ({'url': i} if i else {}))
    L.append('- [ ] `%s` — *%s*. %s' % (k, ti, links(f, ti)))
open(os.path.join(M, 'Survey2_download_links.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('missing', len(missing), 'new', len(NEW))
