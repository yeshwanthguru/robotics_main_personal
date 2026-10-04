"""Writes k/Survey1_reference_list.md and m/Survey2_reference_list.md (all cited works, full-text status,
download checklist, candidates). Run from anywhere: python3 github/k/tools/make_reference_lists.py"""
import sys, csv, re, collections
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from biblib import *
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/'
def rows(p): return list(csv.DictReader(open(p, encoding='utf-8-sig')))

def entry_line(n, key, typ, f, extra):
    return '| %d | `%s` | %s | %s | %s | %s | %s | %s |' % (n, key, esc(authors(f.get('author', f.get('editor','')))) or '—',
        clean(f.get('year','')) or '—', esc(clean(f.get('title',''))), esc(venue(typ, f)) or '—', esc(ident(f)), extra)

# ---------- Survey 1
bib1 = parse(R+'k/Survey1_CSUR_LaTeX_Overleaf/refs.bib')
bib2 = parse(R+'m/Survey2_AIR_LaTeX_Overleaf/refs.bib')
def norm(t): return re.sub(r'[^a-z0-9]','',clean(t).lower())[:60]
T1 = {norm(f.get('title','')): k for k,(ty,f) in bib1.items()}
T2 = {norm(f.get('title','')): k for k,(ty,f) in bib2.items()}
idx1 = {r['Citation key']: r for r in rows(R+'k/Survey1_fulltexts/index.csv')}
ext1 = rows(R+'k/Survey1_data_package/extraction_table.csv')
import unicodedata
def asc(x): return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', clean(x).replace('ı','i')).encode('ascii','ignore').decode().lower())
lev1 = {}
for r in ext1:
    m = re.match(r'([^\s,]+).*?\[?(\d{4})', r['Study'])
    if m:
        lev1.setdefault((asc(m.group(1)), m.group(2)), r['Evidence level'])
def lvl1(key, f):
    a = asc(authors(f.get('author','')).split()[0].rstrip(',')) if f.get('author') else ''
    return lev1.get((a, clean(f.get('year',''))), '')
src1 = idx1[next(iter(idx1))].keys()
col1 = [c for c in src1 if c.startswith('Source')][0]
missing1 = [k for k in bib1 if idx1.get(k, {}).get(col1, 'MISSING') == 'MISSING']
L = []
w = L.append
w('# Survey 1 — reference list (ACM Computing Surveys)')
w('')
w('**Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints**  ')
w('Yeshwanth Guru and Dev Kunwar Singh Chauhan · generated 4 October 2026 from `Survey1_CSUR_LaTeX_Overleaf/refs.bib` and `Survey1_fulltexts/index.csv`')
w('')
g = collections.Counter(idx1.get(k, {}).get('Group', 'not in index') for k in bib1)
w('| | Count |'); w('|---|---|')
w('| Works cited | %d |' % len(bib1))
for k_, v in sorted(g.items()): w('| %s | %d |' % ({'primary':'Primary studies','references':'Other references (reviews, background, methods)'}.get(k_, k_), v))
w('| Full text in the repository | %d |' % (len(bib1) - len(missing1)))
w('| **Full text missing (to download)** | **%d** |' % len(missing1))
w('| Candidate studies awaiting the supervisor (not yet cited) | 12 (5 include, 4 exclude, 3 not yet assessed) |')
w('')
w('Full texts are in `github/k/Survey1_fulltexts/` (private: never upload with the submission).')
w('')
w('## 1. To download (%d)' % len(missing1))
w('')
w('Tick each box when the PDF is saved; name it by the citation key (for example `%s.pdf`).' % (missing1[0] if missing1 else 'Key'))
w('')
for grp, title in (('primary', 'Primary studies'), ('references', 'Other references')):
    ks = [k for k in missing1 if idx1.get(k, {}).get('Group') == grp]
    if not ks: continue
    w('**%s (%d)**' % (title, len(ks))); w('')
    for k in ks:
        typ, f = bib1[k]
        o = T2.get(norm(f.get('title','')))
        w('- [ ] `%s` — %s (%s). *%s*. %s. %s%s' % (k, authors(f.get('author', f.get('editor',''))) or '—', clean(f.get('year','')), clean(f.get('title','')), venue(typ, f) or '—', ident(f), (' — *also needed for Survey 2 (`%s`)*' % o) if o else ''))
    w('')
w('## 2. Candidate studies found after the main search (pending supervisor decision)')
w('')
w('Not cited yet. Full texts are already in `github/k/Survey1_fulltexts/candidates/`; the assessment is in `github/k/Survey1_method_workbook/candidate_studies_assessment.md`.')
w('')
w('| # | Study | Proposed decision | Full text |'); w('|---|---|---|---|')
for i, (s, d, ft) in enumerate([
    ('Eker et al. 2026, QANTIS (arXiv:2603.00785)', 'Include (borderline), L3', 'candidates/include/Eker2026_QANTIS.pdf'),
    ('Cunha et al. 2025, QBRL', 'Include, L2', 'candidates/include/Cunha2025_QBRL.pdf'),
    ('Liu 2025, parallel QAOA grid path planning', 'Include (weak), L2', 'candidates/include/LiuJ2025_parallel_QAOA_grid.pdf'),
    ('Santos et al. 2025, QG-PSO inverse kinematics', 'Include (strong fit), L2', 'candidates/include/Santos2025_QG-PSO_IK.pdf'),
    ('Ho and Hoorn 2022, Q-Coppélia', 'Include (borderline), L1', 'candidates/include/Ho2022_Q-Coppelia.pdf'),
    ('Efe et al. 2026, Ising acceleration', 'Exclude: not quantum', 'candidates/exclude/Efe2026_Ising_acceleration.pdf'),
    ('Gandhudi et al. 2026, QAQL for remaining useful life', 'Exclude: no robot', 'candidates/exclude/Gandhudi2026_QAQL_RUL.pdf'),
    ('Kong et al. 2026, UAV swarm quantum annealing', 'Exclude: Chinese full text', 'candidates/exclude/Kong2026_UAV_swarm_QA_Chinese.pdf'),
    ('van der Meer et al. 2025, quantum-like trust dynamics', 'Exclude: no robot (cited in Survey 2)', 'candidates/exclude/vanderMeer2025_trust_QRW.pdf'),
    ('Tang et al. 2024, CIM for AGV scheduling models, Sci. Rep. 14:12205', 'Not assessed (from your database)', 'not in repo — download'),
    ('Liu, H.-Y. et al. 2020, drone-based entanglement distribution, Natl Sci. Rev.', 'Not assessed (from your database)', 'not in repo — download'),
    ('NV-centre magnetometers for GPS-denied UAV control, Research Square preprint 2025', 'Not assessed (from your database)', 'not in repo — download')], 1):
    w('| %d | %s | %s | %s |' % (i, s, d, ft if ft.startswith('not') else '`'+ft+'`'))
w('')
w('Still to check: the JNEP 2025 AMR task-allocation paper. Candidates 10–12 came from your literature database (see `Survey1_method_workbook/Survey1_database_update.csv` for the database corrections).')
w('')
w('## 3. All cited works (%d)' % len(bib1))
w('')
w('Group: P = primary study, R = other reference; "also S2" = also cited in Survey 2 (%d works are cited in both).' % len(set(T1)&set(T2)))
w(' Level: evidence level from the extraction table (primary studies only, matched by first author and year; blank if not matched).')
w('')
w('| # | Key | Authors | Year | Title | Venue | DOI / arXiv | Group · Level · Full text |')
w('|---|---|---|---|---|---|---|---|')
for n, k in enumerate(sorted(bib1, key=lambda k: k.lower()), 1):
    typ, f = bib1[k]
    grp = idx1.get(k, {}).get('Group', '?')
    lv = lvl1(k, f) if grp == 'primary' else ''
    have = 'no' if k in missing1 else 'yes'
    o = T2.get(norm(f.get('title','')))
    w(entry_line(n, k, typ, f, '%s%s · %s%s' % ({'primary':'P','references':'R'}.get(grp, grp), (' · ' + lv) if lv else '', have, (' · also S2' if o else ''))))
open(R+'k/Survey1_reference_list.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('S1', len(bib1), 'missing', len(missing1), 'levels matched', sum(1 for k in bib1 if idx1.get(k,{}).get('Group')=='primary' and lvl1(k, bib1[k][1])), 'of', sum(1 for k in bib1 if idx1.get(k,{}).get('Group')=='primary'))

# ---------- Survey 2
idx2 = {r['Citation key']: r for r in rows(R+'m/Survey2_fulltexts/index.csv')}
col2 = [c for c in next(iter(idx2.values())) if c.startswith('Source')][0]
ext2 = {r['Key']: r for r in rows(R+'m/Survey2_data_package/extraction_table.csv')}
th2 = {r['Key']: r for r in rows(R+'m/Survey2_data_package/theory_evidence_studies.csv')}
missing2 = [k for k in bib2 if idx2.get(k, {}).get(col2, 'MISSING') == 'MISSING' and k != 'Guru2026']
GN = {'application':'A','theory and evidence':'T','review':'Rv','background':'B','excluded (E5)':'E5','method':'M'}
ORDER = ['application','theory and evidence','review','background','excluded (E5)','method']
TITLE = {'application':'Application studies','theory and evidence':'Theory and evidence studies','review':'Reviews','background':'Background works','excluded (E5)':'Excluded under E5 (cited once; reviewed in Survey 1)','method':'Method references'}
NEW = [
 # (priority, group, citation, why)
 ('A', 'Application (I1) – circuit design', 'Romeo, F. and Settino, J. (2026). *Extreme Quantum Cognition Machines for Deliberative Decision Making*. arXiv:2603.05430', 'Quantum-cognition learning architecture for decisions with noisy and contradictory data'),
 ('A', 'Application (I1) – multi-agent', 'Beuria, J., Chaurasiya, M. and Behera, L. (2025). *Collective motion using quantum-like entanglement of neighbours in perceptual space*. Proc. R. Soc. A 481, 20250489 (arXiv:2409.18985)', 'Quantum-like perception model for swarm collective motion; recovers the Vicsek model (Section 12)'),
 ('A', 'Application (I1) – multi-agent', '*Non-Markovian Collective Motion from Self-Regulated Perceptual Dynamics* (2025). arXiv:2510.23688 — authors to verify (probably the same IIT Mandi group)', 'Open-quantum-system perception and self registers for swarm agents'),
 ('A', 'Application (I1) – multi-agent', '*Self-Healing Coordination in Cognitive Swarm Agents with Bloch-Type Perceptual Memory* (2026). arXiv:2607.11960 — authors to verify', 'Follow-up on quantum-like perceptual memory for swarm coordination'),
 ('A', 'Application (I1) – deep learning', 'Chen, Y., Yan, K., Pan, Y. and Dong, D. (2025). *QiNN-QJ: A Quantum-inspired Neural Network with Quantum Jump for Multimodal Sentiment Analysis*. arXiv:2510.27091', 'Quantum-inspired multimodal fusion with learned Hamiltonian and Lindblad operators (Sections 8–9)'),
 ('A', 'Application (I1) – deep learning', 'Liu, Y. et al. (2023). *A Quantum Probability Driven Framework for Joint Multi-Modal Sarcasm, Sentiment and Emotion Analysis*. arXiv:2306.03650 — author list to verify', 'Quantum-probability multimodal decision fusion (same line as Li2021a/b, Gkoumas2021)'),
 ('A', 'Application (I1) – human–machine', 'Snow, L., Jain, S. and Krishnamurthy, V. (2022). *Lyapunov based Stochastic Stability of a Quantum Decision System for Human-Machine Interaction*. arXiv:2205.12378 (related version arXiv:2204.00059; check the published venue)', 'Controls a Lindbladian (quantum) human decision model in a human–machine loop'),
 ('A', 'Application (I1) – LLMs', 'Agostino, C. J., Le Thien, Q., Apsel, M., Pak, D., Lesyk, E. and Majumdar, A. (2025). *A quantum semantic framework for natural language processing*. arXiv:2506.10077', 'Semantic Bell (CHSH) test on LLM agents; values above the classical bound reported (Section 9.3)'),
 ('A', 'Application (I1) – LLMs', "Agostino, C. J., Le Thien, Q., D'Souza, N. and van der Elst, L. (2026). *The production of meaning in the processing of natural language*. arXiv:2603.20381", 'Contextuality in LLM interpretation of ambiguous expressions'),
 ('B', 'Application (I1) – LLMs', 'Laine, T. A. (2025). *The Quantum LLM: Modeling Semantic Spaces with Quantum Principles*. arXiv:2504.13202', 'Quantum-probability reading of LLM semantic spaces'),
 ('B', 'Application (I1) – circuit on QPU', 'Laine, T. A. (2025). *Quantum LLMs Using Quantum Computing to Analyze and Process Semantic Information*. arXiv:2512.02619', 'LLM embedding similarity computed on a real quantum computer; check against E5'),
 ('B', 'Application (I1) – decision systems', 'Mertová, A., Figl, K. and Pothos, E. M. (2026). *Quantum Cognition Meets Quantum Computing: Modeling Human Reasoning for Advanced Decision Systems*. ECIS 2026 Proceedings (AIS eLibrary)', 'Quantum-cognition models of human reasoning for information/decision systems'),
 ('B', 'Application (I1) – circuit design', 'Pothukuchi, R. P. et al. (incl. Busemeyer, J. R. and Cohen, J. D.) (2023). *The QUATRO Application Suite: Quantum Computing for Models of Human Cognition*. arXiv:2309.00597', 'Benchmark suite of cognition models as quantum circuits (Section 20 software; companion to Widdows2023)'),
 ('B', 'Application (I1) – circuit design', 'Wang, H., Smith, J. W. and Sun, Y. (2019). *Simulating Cognition with Quantum Computers*. arXiv:1905.12599', 'Early proposal to run cognitive models on quantum computers'),
 ('B', 'Application (I1) – teams', "Lawless, W. F. (2026). *Toward tunable advantages of quantum-like teams: the physics of interdependent teams to 'squeeze' uncertainty*. Frontiers in Physics. doi:10.3389/fphy.2025.1715888", 'Continues Lawless2020/2023/2025 on quantum-like human–machine teams'),
 ('A', 'Theory and evidence (I2)', 'Li, J.-A., Dong, D., Wei, Z. et al. (2020). *Quantum reinforcement learning during human decision-making*. Nature Human Behaviour 4, 294–307. doi:10.1038/s41562-019-0804-2', 'Quantum RL fitted to human Iowa Gambling Task and fMRI data — direct human evidence for Section 10 and Case Study 3'),
 ('A', 'Theory and evidence (I2)', 'Chen, M., Ferro, G. M., Sornette, D. and Lorenzo, S. (2022). *On the use of discrete-time quantum walks in decision theory*. PLOS ONE 17(8), e0273551. doi:10.1371/journal.pone.0273551', 'Quantum-walk models of choice and confidence (Sections 5 and 21)'),
 ('B', 'Theory and evidence (I2)', 'Edwards, D. J. (2025). *Further N-Frame networking dynamics of conscious observer-self agents via a functional contextual interface ... in humans and AI*. Frontiers in Computational Neuroscience. doi:10.3389/fncom.2025.1551960', 'Theoretical model of decision fallacies for humans and AI; low evidence level'),
 ('C', 'Probably E5 (quantum computation for inference)', '*Hybrid quantum-classical multi-agent decision-making framework based on hierarchical Bayesian networks in the NISQ era* (2025). Chinese Physics B 34(12), 120304. doi:10.1088/1674-1056/adefd7 — authors to verify', 'Quantum circuits speed up Bayesian-network inference; record as an E5 exclusion (Table S7)'),
 ('C', 'Probably E5 (quantum computation for inference)', 'Recursive quantum-classical hybrid Bayesian-network inference with quantum decision networks (2025), European Physical Journal Special Topics — this is a description, not the exact title; find title, authors and DOI', 'As above; record as an E5 exclusion'),
 ('C', 'Check E5 (variational circuit)', 'Singh, J., Bhangu, K. S., Alkhanifer, A., Alzubi, A. A. and Ali, F. (2025). *Quantum neural networks for multimodal sentiment, emotion, and sarcasm analysis*. Alexandria Engineering Journal 124, 170–187', 'VQE-trained quantum neural network; probably quantum ML as accelerator (E5)'),
]
UPDATE = [
 ('`Maksymov2026` (was `Maksymov2025`)', 'Done 4 Oct 2026: now cited as the Springer book (2026), doi:10.1007/978-3-032-25965-3; the repository PDF is the arXiv preprint.'),
 ('`Busemeyer2012`', 'Done 4 Oct 2026: the entry carries a note on the 2024 second edition, and the text says so (Section 2.3).'),
]
CHECKED_OUT = ['arXiv:2512.20654 Q-RUN, quantum-inspired data re-uploading networks (generic ML, no cognition or decision model)',
 'arXiv:2601.18953, 2603.25138, 2602.12464, 2412.18208, 2507.01691 (reinforcement learning *for* or *on* quantum devices: quantum computation, Survey 1 territory)',
 'arXiv:2602.06286 Yamin et al. 2026, belief coherence of LLMs (classical probability only)',
 'Mannone et al. 2025, quantum computing for swarm robotics (already in Survey 1)',
 'Explainable Quantum AI for vehicle energy management (quantum ML + SHAP/LIME; no cognition model)']
L = []
w = L.append
w('# Survey 2 — reference list (Artificial Intelligence Review)')
w('')
w('**Quantum-Inspired Cognition and Decision-Making for Autonomous Agents, from Robotics to AI/ML Systems: A Systematic Review**  ')
w('Yeshwanth Guru and Dev Kunwar Singh Chauhan · generated 4 October 2026 from `Survey2_AIR_LaTeX_Overleaf/refs.bib`, `Survey2_fulltexts/index.csv` and the data package')
w('')
g = collections.Counter(idx2.get(k, {}).get('Group', '?') for k in bib2)
gm = collections.Counter(idx2.get(k, {}).get('Group', '?') for k in missing2)
w('| Group | Cited | Full text missing |'); w('|---|---|---|')
for grp in ORDER: w('| %s | %d | %d |' % (TITLE[grp], g[grp], gm[grp]))
w('| **Total** | **%d** | **%d** |' % (len(bib2), len(missing2)))
w('| New papers found on 4 Oct 2026, not yet cited | %d | %d |' % (len(NEW), len(NEW)))
w('')
w('%d works are cited in both Survey 1 and Survey 2 (marked "also S1"); download them once. Full texts are in `github/m/Survey2_fulltexts/` (private: never upload with the submission). `Guru2026` is our own Survey 1 manuscript and is not counted as missing.' % len(set(T1)&set(T2)))
w('')
w('## 1. Literature check of 4 October 2026: papers not yet in Survey 2')
w('')
w('I ran 22 topic searches (plus a look-up of the details of each hit) covering quantum cognition for robots and autonomous agents, quantum-like Bayesian networks, LLM order effects and contextuality, human–AI trust, quantum-inspired RL, projective simulation, quantum-inspired deep learning and NLP, swarms and teams, emotion models, open-system and quantum-walk decision models, and recent reviews. Records already cited were checked by title against refs.bib. Publisher and arXiv pages could not be opened in this environment, so details come from search-result metadata: verify each one before citing.')
w('')
w('Priority A = should be added (clear fit, fills a gap); B = likely add after reading; C = record as an exclusion. Adding any of them changes the counts (67 application, 71 theory studies), the PRISMA flow and the tables, so decide after reading the full texts.')
w('')
w('| # | Priority | Proposed group | Reference | Why it matters |'); w('|---|---|---|---|---|')
for i, (p, gr, c, why) in enumerate(sorted(NEW, key=lambda x: x[0]), 1):
    w('| N%d | %s | %s | %s | %s |' % (i, p, gr, esc(c), esc(why)))
w('')
w('**Cited entries updated**')
w('')
for a, b in UPDATE: w('- %s — %s' % (a, b))
w('')
w('**Found and judged out of scope**')
w('')
for x in CHECKED_OUT: w('- ' + x)
w('')
w('Already cited, confirmed current: Khrennikov2026 (Discover AI), Humr2025, Chella2026 (teleo-reactive robot), Kang2026 (QQ audit of LLMs), Lawless2025, Huang2025b (overview of the research programme), Asano2026 (GKSL dynamics), vanderMeer2025 (trust and quantum random walks), Song2022 (autonomous driving), Ho2022 (affective processes), Daglarli2025, Maksimovic2025, Ried2019, Lanza2020/2021.')
w('')
w('## 2. To download')
w('')
w('### 2a. New papers from the literature check (%d)' % len(NEW))
w('')
for i, (p, gr, c, why) in enumerate(sorted(NEW, key=lambda x: x[0]), 1):
    w('- [ ] N%d (%s) %s' % (i, p, c))
w('- [ ] Maksymov (2026) book *Cognition in Superposition*, Springer, doi:10.1007/978-3-032-25965-3 (chapters 4, 6, 9, 11)')
w('')
w('### 2b. Cited works without a full text in the repository (%d)' % len(missing2))
w('')
w('Save each PDF as `<key>.pdf`. Application studies come first: their full texts are needed to complete the quality appraisal (Q6 reproducibility, currently "?" for 47 studies).')
w('')
for grp in ORDER:
    ks = [k for k in missing2 if idx2.get(k, {}).get('Group') == grp]
    if not ks: continue
    w('**%s (%d)**' % (TITLE[grp], len(ks))); w('')
    for k in ks:
        typ, f = bib2[k]
        o = T1.get(norm(f.get('title','')))
        lv = (ext2.get(k) or th2.get(k) or {}).get('Evidence level', '')
        note = ' — *own manuscript, no download needed*' if k == 'Guru2026' else ''
        w('- [ ] `%s`%s — %s (%s). *%s*. %s. %s%s%s' % (k, (' [%s]' % lv) if lv else '', authors(f.get('author', f.get('editor',''))) or '—', clean(f.get('year','')), clean(f.get('title','')), venue(typ, f) or '—', ident(f), (' — *also needed for Survey 1 (`%s`)*' % o) if o else '', note))
    w('')
w('## 3. All cited works (%d)' % len(bib2))
w('')
w('Group: A application study, T theory and evidence study, Rv review, B background, E5 excluded under E5 (reviewed in Survey 1), M method reference. Level: evidence level E1–E6 (graded studies only). "also S1" = also cited in Survey 1.')
w('')
w('| # | Key | Authors | Year | Title | Venue | DOI / arXiv | Group · Level · Full text |')
w('|---|---|---|---|---|---|---|---|')
for n, k in enumerate(sorted(bib2, key=lambda k: k.lower()), 1):
    typ, f = bib2[k]
    grp = idx2.get(k, {}).get('Group', '?')
    lv = (ext2.get(k) or th2.get(k) or {}).get('Evidence level', '')
    have = 'own manuscript' if k == 'Guru2026' else ('no' if k in missing2 else 'yes')
    o = T1.get(norm(f.get('title','')))
    w(entry_line(n, k, typ, f, '%s%s · %s%s' % (GN.get(grp, grp), (' · ' + lv) if lv else '', have, ' · also S1' if o else '')))
open(R+'m/Survey2_reference_list.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('S2', len(bib2), 'missing', len(missing2), 'graded', sum(1 for k in bib2 if k in ext2 or k in th2))
