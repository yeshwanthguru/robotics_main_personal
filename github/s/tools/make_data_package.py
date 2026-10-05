"""Builds the Survey 3 data package (github/s/Survey3_data_package) from the structured paper write-ups
(tools/data/writeups.json) and the bibliography. Run from github/s:  python3 tools/make_data_package.py

Outputs
  extraction_table.csv   one row per included work (180)
  quality_appraisal.csv  criteria Q1-Q7 for the 161 primary studies at levels E2-E5
  study_summaries.csv    one-paragraph summary per work, plain and with [CITE:key] tokens
The edge class and the confidence-signal class are hand-coded (data/edge_coding.txt,
data/signal_coding.txt). Criteria Q1-Q7 are coded by the explicit rules below, applied to the write-ups
rather than the full texts; ambiguous cases resolve to the lower code. All rules are listed in codebook.md."""
import csv, json, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from biblib import parse, clean
S = os.path.dirname(HERE) + '/'
G = os.path.dirname(os.path.dirname(HERE)) + '/'
OUT = S + 'Survey3_data_package/'
os.makedirs(OUT, exist_ok=True)

W = json.load(open(HERE + '/data/writeups.json', encoding='utf-8'))
BIB = parse(S + 'Survey3_TNNLS_LaTeX_Overleaf/refs.bib')

TOPIC = {'3': 'LLM planners and orchestrators', '4': 'VLA and robot foundation models',
         '5': 'Perception and epistemic uncertainty', '6': 'Reinforcement learning and policy variance',
         '7': 'Imitation learning and behavioral fidelity', '8': 'Fault detection, adaptation and recovery',
         '9': 'Meta-learning', '10': 'Uncertainty fusion and calibration', '11': 'On-device adaptation and continual learning',
         '12': 'Adaptive computation, mixture of experts and routing', '13': 'Platforms, benchmarks and evaluation',
         '14': 'Safe learning'}
LEVEL = {'E2': 'E2', 'E3': 'E3', 'E4': 'E4', 'E5': 'E5', 'Review': 'R', 'Software/tool': 'S'}


def topic(e): return TOPIC[e['section'].split()[0]]
def level(e): return LEVEL[e['level'].split()[0]]


def study_name(key):
    f = BIB[key][1]
    names = []
    for p in re.split(r'\s+and\s+', clean(f.get('author', ''))):
        if p.lower() == 'others': names.append(None); continue
        names.append(p.split(',')[0].strip() if ',' in p else p.split()[-1])
    y = clean(f.get('year', ''))
    if not names: return '%s (%s)' % (clean(f.get('title', key))[:40], y)
    if len(names) == 1 and names[0]: return '%s (%s)' % (names[0], y)
    if len(names) == 2 and all(names): return '%s and %s (%s)' % (names[0], names[1], y)
    return '%s et al. (%s)' % (names[0], y)


def plain(txt):
    """Replace [CITE:key] tokens by author-year text, or by the year alone when the authors are named just before."""
    def rep(m):
        k = m.group(1); name = study_name(k); surname = name.split()[0].rstrip(',')
        before = txt[max(0, m.start() - 80):m.start()]
        ends = [x.end() for x in re.finditer(r'(?<!\bal)(?<!\be\.g)(?<!\bi\.e)\. ', before)]
        before = before[ends[-1]:] if ends else before
        return name[name.rfind('('):] if surname in before else name
    return re.sub(r'\[CITE:(\w+)\]', rep, txt)


def ident(key):
    f = BIB[key][1]
    if f.get('doi'): return 'https://doi.org/' + clean(f['doi'])
    blob = ' '.join(f.get(k, '') for k in ('eprint', 'journal', 'note', 'url', 'howpublished'))
    m = re.search(r'(\d{4}\.\d{4,5})', blob)
    if m: return 'https://arxiv.org/abs/' + m.group(1)
    if f.get('url'): return clean(f['url'])
    return ''


def pubstatus(key):
    t, f = BIB[key]
    blob = (f.get('journal', '') + f.get('note', '') + f.get('howpublished', '')).lower()
    if t == 'article' and 'arxiv' not in blob: return 'Journal article'
    if t == 'inproceedings': return 'Conference paper'
    if t in ('misc', 'software') and 'github' in (f.get('url', '') + f.get('howpublished', '')).lower(): return 'Software'
    if 'arxiv' in blob or t == 'misc': return 'Preprint'
    return {'book': 'Book', 'incollection': 'Book chapter', 'phdthesis': 'Thesis', 'techreport': 'Report'}.get(t, 'Other')


# companion surveys: matched by normalised title
def norm(t): return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', clean(t)).encode('ascii', 'ignore').decode().lower())[:60]
T1 = {norm(f.get('title', '')) for _, f in parse(G + 'k/Survey1_CSUR_LaTeX_Overleaf/refs.bib').values()}
T2 = {norm(f.get('title', '')) for _, f in parse(G + 'm/Survey2_AIR_LaTeX_Overleaf/refs.bib').values()}
def companion(key):
    t = norm(BIB[key][1].get('title', ''))
    return ', '.join(n for n, T in (('Survey 1', T1), ('Survey 2', T2)) if t in T) or 'No'


# ---------- coding rules -------------------------------------------------------------------------------
def load_codes(name):
    out = {}
    for line in open(HERE + '/data/' + name, encoding='utf-8'):
        if line.strip() and not line.startswith('#'):
            k, c = line.split(); out[k] = c
    return out
EDGE = load_codes('edge_coding.txt'); SIG = load_codes('signal_coding.txt')
EDGE_NAME = {'P': 'Pi-class or embedded CPU', 'J': 'Embedded GPU', 'W': 'Workstation GPU', 'D': 'Datacenter or cloud', 'U': 'Not stated'}
SIG_NAME = {'C': 'Conformal or calibrated', 'E': 'Epistemic uncertainty', 'F': 'Failure, anomaly or novelty score',
            'V': 'Policy variance or entropy', 'Q': 'Routing score or predicted quality', 'N': 'None'}


def edge_class(e):
    """Inference platform as published (hand-coded from the edge-footprint field; see data/edge_coding.txt)."""
    return 'Not applicable' if level(e) == 'R' else EDGE_NAME[EDGE[e['key']]]


def signal_class(e):
    """Confidence signal provided or used (hand-coded; see data/signal_coding.txt)."""
    return 'Not applicable' if level(e) == 'R' else SIG_NAME[SIG[e['key']]]


NUM = r'\d+(\.\d+)?\s*(%|percent|percentage points|times|x\b|×|ms|Hz|GB|MB|KB|s\b|tokens)|\d+(\.\d+)?\s*(of|out of)\s*\d+|from \d|to \d+(\.\d+)?%'
CMP = r'outperform|than|baseline|compared|relative to|\bover\b|beat|exceed|surpass|vs\.?|versus|match(es|ing)? (the )?(full|state|prior|baseline)|improv'
NOABS = r'no numbers|not given in the abstract|no (success|task) rates|figures are not|not reported'


def appraise(e):
    f = e['fields']; L = level(e)
    method, res, setup = f.get('Method', ''), f.get('Key result', ''), f.get('Setup and data', '')
    alltxt = ' '.join(f.values()) + ' ' + e['summary']
    q = {}
    # Q1 method specified: a concrete method description of at least 12 words
    n = len(method.split()); q['Q1'] = 'M' if n >= 12 else ('P' if n >= 5 else 'N')
    # Q2 comparison with a named baseline or prior method
    if re.search(NOABS, res, re.I) and not re.search(CMP, res, re.I): q['Q2'] = '?'
    elif re.search(CMP, res, re.I): q['Q2'] = 'M' if re.search(NUM, res) else 'P'
    else: q['Q2'] = 'N'
    # Q3 physical validation, from the evidence level and the setup
    if L == 'E5': q['Q3'] = 'M'
    elif L == 'E4': q['Q3'] = 'M' if re.search(r'real|physical|hardware|robot', setup, re.I) else 'P'
    elif re.search(r'real[- ](robot|world|hardware)|physical robot', setup + res, re.I): q['Q3'] = 'P'
    else: q['Q3'] = 'N'
    # Q4 compute or latency reported by the authors (numbers on time, memory, parameters or energy)
    comp = (r'\d[\d.,]*\s*(ms|Hz|GB|MB|KB|GFLOPs|FLOPs|TOPS|tokens per second|parameters|B parameters|M parameters)\b'
            r'|\b\d[\d.]*B\b|\d[\d.]*\s*(x|×|times)\s*[\w-]*\s*(lower|less|fewer|reduction|throughput|speed-?up|memory|compute|cost)'
            r'|\d[\d.]*%\s*(lower|less|reduc\w*|fewer)?\s*(compute|cost|memory|inference|latency|FLOPs)'
            r'|(memory|latency|compute|cost|inference time|speed-?up|throughput|FLOPs)[^.;]{0,40}\d[\d.]*\s*(x|×|times|%)')
    if re.search(comp, res + ' ' + e['summary'], re.I): q['Q4'] = 'M'
    elif re.search(r'latency|memory|compute|efficien|real-time|onboard|on-board|FLOP|throughput|cost', res + ' ' + method, re.I): q['Q4'] = 'P'
    else: q['Q4'] = 'N'
    # Q5 quantitative result reported
    if re.search(NUM, res) or re.search(r'\d+(\.\d+)?%', e['summary']): q['Q5'] = 'M'
    elif re.search(NOABS, res + e['summary'], re.I): q['Q5'] = '?'
    else: q['Q5'] = 'P'
    # Q6 code or models released (only stated releases count; otherwise not assessable)
    q['Q6'] = 'M' if re.search(r'open[- ]source|code (is |was )?(released|available|public)|released (code|models?|weights)|publicly available|open (model|weights|release)|github', alltxt, re.I) else '?'
    # Q7 exposes a confidence or reliability signal that an orchestrator could read
    c = SIG[e['key']]
    q['Q7'] = 'M' if c in 'CEFV' else ('P' if c == 'Q' else 'N')
    return q


# ---------- write ------------------------------------------------------------------------------------
def w(name, header, rows):
    with open(OUT + name, 'w', encoding='utf-8-sig', newline='') as fh:
        wr = csv.writer(fh); wr.writerow(header); wr.writerows(rows)
    print('wrote', name, len(rows))


ext, app, summ = [], [], []
for e in W:
    k = e['key']; f = e['fields']; L = level(e)
    ext.append([study_name(k), k, topic(e), e['role'].capitalize(), L, e['src'], pubstatus(k), e['basis'],
                plain(f.get('Task', '')), plain(f.get('Method', '')), plain(f.get('Setup and data', '')),
                plain(f.get('Key result', '')), plain(f.get('Limitation', '')), plain(f.get('Edge footprint', '')),
                edge_class(e), signal_class(e),
                plain(f.get('Role in the framework', '')), companion(k), ident(k)])
    if L in ('E2', 'E3', 'E4', 'E5'):
        q = appraise(e)
        app.append([k, L, e['basis']] + [q['Q%d' % i] for i in range(1, 8)])
    summ.append([k, study_name(k), topic(e), L, e['basis'], plain(e['summary']), e['summary'], e['note']])

w('extraction_table.csv', ['Study', 'Key', 'Topic', 'Role', 'Evidence level', 'Source stream', 'Publication status', 'Basis',
                           'Task', 'Method', 'Setup and data', 'Key result', 'Limitation', 'Edge footprint (as published)',
                           'Edge class', 'Confidence signal class', 'Role in the framework', 'Also in companion survey',
                           'DOI or identifier'], ext)
w('quality_appraisal.csv', ['Study key', 'Evidence level', 'Basis', 'Q1 Method specification', 'Q2 Baseline comparison',
                            'Q3 Physical validation', 'Q4 Compute reporting', 'Q5 Quantitative evaluation',
                            'Q6 Code or model release', 'Q7 Confidence signal'], app)
w('study_summaries.csv', ['Key', 'Study', 'Topic', 'Evidence level', 'Basis', 'Summary', 'Summary_keyed', 'Verification_note'], summ)

# ---------- counts used in the manuscript ----------------------------------------------------------------
st = {}
st['n'] = len(W)
st['levels'] = Counter(level(e) for e in W)
st['by_topic_level'] = {t: dict(Counter(level(e) for e in W if topic(e) == t)) for t in TOPIC.values()}
st['basis'] = Counter(e['basis'] for e in W)
st['source'] = Counter(e['src'] for e in W)
st['role'] = Counter(e['role'] for e in W)
st['edge'] = Counter(r[14] for r in ext)
st['edge_by_level'] = {L: dict(Counter(r[14] for r in ext if r[4] == L)) for L in ('E2', 'E3', 'E4', 'E5')}
st['signal'] = Counter(r[15] for r in ext)
st['companion'] = Counter(r[17] for r in ext)
st['status'] = Counter(r[6] for r in ext)
st['appraisal'] = {'Q%d' % i: dict(Counter(r[2 + i] for r in app)) for i in range(1, 8)}
st['n_appraised'] = len(app)
st['years'] = Counter(clean(BIB[e['key']][1].get('year', '')) for e in W)
json.dump(st, open(HERE + '/data/package_counts.json', 'w'), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in st.items() if k not in ('by_topic_level', 'years')}, indent=0, sort_keys=True))
