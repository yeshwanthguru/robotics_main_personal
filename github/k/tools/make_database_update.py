"""Writes k/Survey1_method_workbook/Survey1_database_update.csv: rows to add to, correct in, or flag as
candidates in the authors' literature database. Run: python3 github/k/tools/make_database_update.py"""
import sys, csv, re, unicodedata
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from biblib import *
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/'
b1 = parse(R+'k/Survey1_CSUR_LaTeX_Overleaf/refs.bib'); b2 = parse(R+'m/Survey2_AIR_LaTeX_Overleaf/refs.bib')
def norm(t): return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', clean(t)).encode('ascii','ignore').decode().lower())[:60]
T2 = {norm(f.get('title','')) for k,(t,f) in b2.items()}
idx = {r['Citation key']: r for r in csv.DictReader(open(R+'k/Survey1_fulltexts/index.csv', encoding='utf-8-sig'))}
col = [c for c in next(iter(idx.values())) if c.startswith('Source')][0]
ext = list(csv.DictReader(open(R+'k/Survey1_data_package/extraction_table.csv', encoding='utf-8-sig')))
def asc(s): return unicodedata.normalize('NFKD', clean(s).replace('ı','i')).encode('ascii','ignore').decode().lower()
def ext_row(k):
    f = b1[k][1]; first = re.sub(r'[^a-z]','', asc(f['author'].split(' and ')[0].split(',')[0])); y = clean(f.get('year',''))
    for e in ext:
        m = re.match(r'(.+?)\s*\[(\d{4})', e['Study'])
        if m and re.sub(r'[^a-z]','', asc(m.group(1).split()[0])) == first and m.group(2) == y: return e
    return None
def full_authors(a):
    ps = [p.strip() for p in re.split(r'\s+and\s+', clean(a))]
    out = []
    for p in ps:
        if p.lower() == 'others': out.append('et al.'); continue
        if ',' in p: last, first = [x.strip() for x in p.split(',', 1)]
        else: parts = p.split(); last, first = parts[-1], ' '.join(parts[:-1])
        ini = ''.join(w[0] + '.' for w in re.split(r'[\s\-]+', first) if w)
        out.append('%s, %s' % (last, ini) if ini else last)
    if len(out) > 6: out = out[:3] + ['et al.']
    return ', '.join(out)
def url(f):
    i = ident(f)
    if i.startswith('doi:'): return 'https://doi.org/' + i[4:]
    if i.startswith('arXiv:'): return 'https://arxiv.org/abs/' + i[6:]
    return '' if i == '—' else i
# key: (Category, Robotics Function, Type, Relevance, Final outline section)
NEW = {
 'Bang2026': ('Quantum Optimization','Multi-Robot Coordination','Quantum','LLM front end turns natural-language instructions into QUBO constraints for multi-drone task assignment (CVaR-QAOA)','Multi-Agent Pathfinding and UAV Navigation'),
 'Dragan2025': ('Quantum ML, RL & Agents','Localisation & Navigation','Quantum','Continuous-action quantum RL (hybrid DDPG) for robot navigation; far fewer trainable weights (this is the row you had as Hohenfeld 2023)','Quantum Reinforcement Learning'),
 'Essalmi2026': ('Quantum Cognition in Robotics','Cognition & Decision','Quantum-inspired','Multi-player, multi-strategy quantum game for interaction-aware decisions in automated driving','Robotic and Human-Machine Applications'),
 'Lathrop2023': ('General Quantum Robotics','Planning & Control','Quantum','Sampling-based motion planners recast as Grover-type quantum search','Motion Planning and Swarm Planning'),
 'Liu2021': ('Quantum Sensing & Metrology','Communication & Security','Quantum','Entanglement distribution with drones as mobile relay nodes (field experiment)','Quantum Communication between Robots'),
 'Mannone2025b': ('Multi-Robot / Swarm Robotics','Multi-Robot Coordination','Quantum','Density-matrix model of micro/nano robot swarms (published version of arXiv:2509.08002, your "Micro-nano robotic networks" row)','Quantum Swarm Robotics (supplement)'),
 'Ngo2026': ('Quantum ML, RL & Agents','Planning & Control','Quantum','Single-qubit actor-critic policy controls a cart-pole on a real superconducting QPU','Quantum Reinforcement Learning'),
 'OsabaDrone2025': ('Quantum Optimization','Multi-Robot Coordination','Quantum','Drone routing with QAOA clustering plus quantum-annealer routing (Q4DR)','Multi-Agent Pathfinding and UAV Navigation'),
 'Park2023': ('Quantum ML, RL & Agents','Multi-Robot Coordination','Quantum','Quantum multi-agent actor-critic for cooperative multi-UAV mobile access','Quantum Reinforcement Learning'),
 'Park2024': ('Quantum ML, RL & Agents','Multi-Robot Coordination','Quantum','Quantum multi-agent RL for autonomous mobility cooperation','Quantum Reinforcement Learning'),
 'Roh2025': ('Quantum Machine Learning','Perception','Quantum','Fast quantum CNN for low-complexity object detection in autonomous driving','Supervised Quantum Machine Learning'),
 'Sun2025': ('Quantum ML, RL & Agents','Planning & Control','Quantum','Simulated VQC policy controls a physical cart-pole in real time','Quantum Reinforcement Learning'),
 'Templier2022': ('Quantum Sensing & Metrology','Localisation & Navigation','Quantum','Hybrid three-axis quantum accelerometer triad tracks vector acceleration','Quantum Navigation Sensors'),
 'Tian2023': ('Quantum Sensing & Metrology','Communication & Security','Quantum','Drone-based quantum key distribution field demonstration','Quantum Communication between Robots'),
 'Udekwe2025': ('General Quantum Robotics','Foundations','Quantum','Review of quantum optimisation, search and ML for robotics (competing survey)','Related Surveys and Positioning'),
 'Wang2023': ('Quantum Sensing & Metrology','Localisation & Navigation','Quantum','NV-diamond magnetometry for magnetic map-matching navigation without GNSS','Quantum Navigation Sensors'),
 'Windmann2023': ('Quantum Optimization','Planning & Control','Quantum','QAOA on IBM hardware for job scheduling in automated storage and retrieval systems','Multi-Robot Fleets and Automated Guided Vehicles'),
 'Yu2025': ('Quantum Optimization','Perception','Quantum','Hybrid quantum-classical next-best-view planning (CVPR 2026)','Perception-Driven Planning and Localization'),
 'Babbush2018': ('Quantum Hardware & NISQ','Foundations','Quantum','Linear-T-complexity circuits; basis for fault-tolerant resource counts','A Worked Resource Estimate'),
 'Babbush2021': ('Quantum Hardware & NISQ','Foundations','Quantum','Quadratic speed-ups are unlikely to pay off after error correction','A Worked Resource Estimate'),
 'Begusic2024': ('Quantum Hardware & NISQ','Foundations','Classical baseline','Classical simulation reproduces the 2023 "utility" experiment — limits of quantum-advantage claims','Quantum Computing Essentials'),
 'Benkner2021': ('Quantum Computer Vision','Perception','Quantum','Q-Match: shape matching with quantum annealing','Quantum Computer Vision (supplement)'),
 'Birdal2021': ('Quantum Computer Vision','Perception','Quantum','Quantum permutation synchronisation on an annealer','Quantum Computer Vision (supplement)'),
 'Bluvstein2024': ('Quantum Hardware & NISQ','Hardware','Quantum','Logical quantum processor on neutral-atom arrays','Quantum Computing Essentials; Historical Evolution'),
 'Bravyi2024': ('Quantum Hardware & NISQ','Hardware','Quantum','High-threshold, low-overhead qLDPC quantum memory','Quantum Computing Essentials; Hardware Constraints'),
 'Busemeyer1993': ('Quantum Cognition (Foundations)','Cognition & Decision','Classical baseline','Decision field theory — classical dynamic decision model contrasted with quantum models','Quantum Cognition: Motivation and Formalism'),
 'Doan2022': ('Quantum Computer Vision','Perception','Quantum','Hybrid quantum-classical robust fitting','Quantum Computer Vision (supplement)'),
 'Dobler2025': ('Hybrid Quantum-Classical','Foundations','Quantum','Survey of integrating QPUs into HPC systems — where the QPU sits in the robot stack','Where the Quantum Processor Sits in the Robot'),
 'Finzgar2022': ('Review Methodology','Methodology','Quantum','QUARK application-level benchmarking framework (includes a robot-path problem)','Cross-Cutting Challenges'),
 'GarciaPineda2026': ('General Quantum Robotics','Foundations','Quantum','Systematic review of AI and quantum computing integration','Related Surveys and Positioning'),
 'Geiger2011': ('Quantum Sensing & Metrology','Localisation & Navigation','Quantum','Airborne atom interferometry detects inertial effects (first flight test)','Quantum Navigation Sensors; Historical Evolution'),
 'Golyanik2020': ('Quantum Computer Vision','Perception','Quantum','Quantum annealing for point-set correspondence','Quantum Computer Vision (supplement)'),
 'GoogleQAI2025': ('Quantum Hardware & NISQ','Hardware','Quantum','Quantum error correction below the surface-code threshold (Willow)','Quantum Computing Essentials; Hardware Constraints'),
 'Kaldari2025': ('Quantum ML, RL & Agents','Learning','Quantum','Recent review of quantum reinforcement learning','Related Surveys and Positioning'),
 'KimY2023': ('Quantum Hardware & NISQ','Foundations','Quantum','IBM "utility before fault tolerance" experiment','Quantum Computing Essentials'),
 'King2025': ('Quantum Hardware & NISQ','Foundations','Quantum','Beyond-classical quantum simulation on an annealer','Historical Evolution'),
 'Kruse2024': ('Quantum ML, RL & Agents','Learning','Quantum','VQC design for quantum RL in continuous environments','Quantum Reinforcement Learning'),
 'Meli2022': ('Quantum Computer Vision','Perception','Quantum','Iterative quantum approach for point-set transformation estimation','Quantum Computer Vision (supplement)'),
 'Neukart2017': ('Quantum Optimization','Planning & Control','Quantum','Traffic-flow optimisation on a D-Wave annealer (early application)','Historical Evolution; Methods'),
 'Rieffel2015': ('Quantum Optimization','Planning & Control','Quantum','Programming a quantum annealer for operational planning problems','Historical Evolution; Methods'),
 'RodriguezDiaz2025': ('Quantum Machine Learning','Learning','Quantum','ACM CSUR survey of quantum machine learning','Related Surveys and Positioning'),
 'Wang2024': ('Quantum Machine Learning','Learning','Quantum','Review of QML from NISQ to fault tolerance','Related Surveys and Positioning'),
 'Yarkoni2022': ('Quantum Optimization','Planning & Control','Quantum','Review of quantum annealing for industry applications','Methods'),
 'Zaech2022': ('Quantum Computer Vision','Perception','Quantum','Adiabatic quantum computing for multi-object tracking','Quantum Computer Vision (supplement)'),
 'Zhuang2024': ('General Quantum Robotics','Foundations','Quantum','Survey of quantum computing in intelligent transportation systems','Related Surveys and Positioning'),
}
COLS = ['Action','Category','Author','Year','Title','Venue','Relevance','Status','URL','Importance','Robotics Function','Type','Serves','Gap Relevance','Evidence Type','Open Question / Limitation (for survey)','Outline §','Read status','Key takeaway / notes','Read for Survey §','Survey read role','Final outline §','Curation note','In other survey?']
rows = []
for k, (cat, fn, typ, rel, sec) in NEW.items():
    t, f = b1[k]
    e = ext_row(k) if idx[k]['Group'] == 'primary' else None
    have = idx[k][col] != 'MISSING'
    rows.append({'Action': 'ADD (cited in Survey 1)', 'Category': cat, 'Author': full_authors(f.get('author','')), 'Year': clean(f.get('year','')),
        'Title': clean(f.get('title','')), 'Venue': venue(t, f), 'Relevance': rel, 'Status': 'Verify access', 'URL': url(f), 'Importance': '',
        'Robotics Function': fn, 'Type': typ, 'Serves': 'Survey 1', 'Gap Relevance': '',
        'Evidence Type': ('%s; %s' % (e['Evidence level'], e['Quantum execution'])) if e else ('Primary study' if idx[k]['Group']=='primary' else 'Background / reference'),
        'Open Question / Limitation (for survey)': (e['Limitation'] if e else ''), 'Outline §': '', 'Read status': 'Read (used in Survey 1)' if have else 'To read',
        'Key takeaway / notes': (e['Key result'] if e else ''), 'Read for Survey §': '', 'Survey read role': 'Core' if idx[k]['Group']=='primary' else 'Context',
        'Final outline §': sec, 'Curation note': 'Added 2026-10-04 — cited in Survey 1 as `%s`; PDF %s' % (k, 'in Survey1_fulltexts' if have else 'NOT in repo (download)'),
        'In other survey?': 'Shared with S2' if norm(f.get('title','')) in T2 else 'Unique'})
CORR = [
 ('Masood, A., Gao, F., Liu, C., et al.','2018','A robot SLAM improved by quantum-behaved particle swarm optimization','Authors → Zuo, T., Min, H., Tang, Q., Tao, Q. (Zuo2018)'),
 ('Heimann, D., Hohenfeld, H., Wiebe, F., Kirchner, F.','2022','Quantum deep reinforcement learning for robot navigation tasks','Published version: Hohenfeld, H., Heimann, D., Wiebe, F., Kirchner, F. (2024), IEEE Access (Hohenfeld2024)'),
 ('Hohenfeld, H., Heimann, D., Wiebe, F., Kirchner, F.','2023','Continuous quantum RL for navigation','Wrong authors/year: Drăgan, T.-A., Künzner, A., Wille, R., Lorenz, J. M. (2025), Continuous Quantum Reinforcement Learning for Robot Navigation, ICAART 2025 (Dragan2025) — replaced by the ADD row'),
 ('Mannone, M., et al.','2025','Micro-nano robotic networks based on density matrices','Preprint arXiv:2509.08002; published as Mannone et al. (2026), Density Matrix-Based Dynamics for Quantum Robotic Swarms, RAS 200:105418 (Mannone2025b) — replaced by the ADD row'),
 ('Tang, E.','2020','Quantum-inspired classical algorithm for recommendation systems','Year → 2019 (STOC 2019) (Tang2019)'),
 ('Brassard, G., Hoyer, P., Mosca, M., Tapp, A.','2000','Quantum amplitude amplification','Cited version: Quantum amplitude amplification and estimation, 2002, Contemporary Mathematics 305 (Brassard2002)'),
 ('Benioff, P.','2001','Space searches with a quantum robot','Year → 2002 (book chapter, Quantum Computation and Information) (Benioff2002)'),
 ('Raghuvanshi, et al.','','Quantum robots for teenagers','Year → 2007; venue ISMVL 2007 (Raghuvanshi2007)'),
 ('QUADRI Project (ACM UMAP)','2025','Quantum-enhanced social robotics: the QUADRI project','Author → De Carolis, B., et al. (DeCarolis2025)'),
 ('(authors to confirm)','2025','Quantum-assisted automatic path-planning for robotic quality inspection','Authors → Osaba, E., et al. (Osaba2025)'),
 ('(authors to confirm)','2025','Drone- and vehicle-based quantum key distribution','Authors → Conrad, A., et al. (Conrad2025)'),
 ('Lawless, W.F.','2020','Quantum-like interdependence theory advances autonomous human–machine teams (A-HMTs)','Serves → Survey 2 only (cited in Survey 2 as Lawless2020, not in Survey 1)'),
]
for k in ['Chella2022','Khoshnoud2020','Mannone2022','Daglarli2025','Lawless2023','Dong2006','Benioff1998']:
    t, f = b1[k]
    CORR.append((full_authors(f.get('author','')), clean(f.get('year','')), clean(f.get('title','')), 'In other survey? → Shared with S2 (also cited in Survey 2)'))
for a, y, ti, note in CORR:
    rows.append({c: '' for c in COLS} | {'Action': 'CORRECT existing row', 'Author': a, 'Year': y, 'Title': ti, 'Curation note': note})
CAND = [
 ('Quantum Optimization','Tang, et al.','2024','Quantum computing for several AGV scheduling models','Scientific Reports, 14, 12205','Coherent Ising machine applied to AGV scheduling models','Multi-Robot Coordination','Quantum-inspired'),
 ('Quantum Sensing & Metrology','Liu, H.-Y., et al.','2020','Drone-based entanglement distribution towards mobile quantum networks','National Science Review','Entanglement distribution via drones (precursor of Liu2021)','Communication & Security','Quantum'),
 ('Quantum Sensing & Metrology','(authors to confirm)','2025','NV-centre magnetometers for GPS-denied UAV control','Research Square (preprint)','NV-centre magnetometry for UAV navigation','Localisation & Navigation','Quantum'),
]
for cat, a, y, ti, v, rel, fn, typ in CAND:
    rows.append({c: '' for c in COLS} | {'Action': 'CANDIDATE – pending professor', 'Category': cat, 'Author': a, 'Year': y, 'Title': ti, 'Venue': v, 'Relevance': rel,
        'Robotics Function': fn, 'Type': typ, 'Serves': 'Survey 1', 'Read status': 'To read', 'Curation note': 'Not cited in Survey 1; PDF not in repo; listed in candidate_studies_assessment.md §5', 'In other survey?': 'Unique'})
out = R + 'k/Survey1_method_workbook/Survey1_database_update.csv'
with open(out, 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(rows)
import collections; print(collections.Counter(r['Action'] for r in rows), len(NEW))
