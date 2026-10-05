"""Generates the supplementary material of Survey 3 (supplement.tex) from the data package.
Run from github/s:  python3 tools/make_supplement.py
Then compile:       cd Survey3_TNNLS_LaTeX_Overleaf && pdflatex supplement && bibtex supplement && pdflatex supplement && pdflatex supplement"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from make_data_package import BIB, TOPIC
from biblib import clean
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'Survey3_data_package')
OUT = os.path.join(ROOT, 'Survey3_TNNLS_LaTeX_Overleaf', 'supplement.tex')


def tex(s):
    """Escape plain text for LaTeX (same rules as the Survey 2 generator)."""
    UNI = {'×': r'$\times$', '≈': r'$\approx$', '≤': r'$\leq$', '≥': r'$\geq$', 'ε': r'$\varepsilon$', '–': '--', '—': '---',
           '‘': '`', '’': "'", '“': '``', '”': "''", '…': r'\ldots{}', '→': r'$\rightarrow$', '±': r'$\pm$', '−': '$-$',
           'σ': r'$\sigma$', 'γ': r'$\gamma$', 'θ': r'$\theta$', 'π': r'$\pi$', 'λ': r'$\lambda$', 'μ': r'$\mu$', '·': r'$\cdot$',
           'α': r'$\alpha$', 'β': r'$\beta$', 'τ': r'$\tau$', '³': r'$^3$', '²': r'$^2$', ' ': ' ', ' ': ' ', 'ö': r'\"o',
           'é': r"\'e", 'ü': r'\"u', 'ø': r'{\o}', 'è': r'\`e', 'ä': r'\"a', 'ł': r'{\l}', '∼': r'$\sim$', '≥': r'$\geq$'}
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}'),
                 ('~', r'\textasciitilde{}'), ('^', r'\^{}')]:
        s = s.replace(a, b)
    s = s.replace(r'\textbackslash\{\}', r'\textbackslash{}').replace('|', r'$|$').replace('<', r'$<$').replace('>', r'$>$')
    return ''.join(UNI.get(c, c) for c in s).replace('$$', ' ')


def read(name):
    with open(os.path.join(DATA, name), encoding='utf-8-sig') as f: return list(csv.DictReader(f))


def short_name(key):
    """Author text without the year, for 'Author et al. [n]'."""
    f = BIB[key][1]; names = []
    for p in re.split(r'\s+and\s+', clean(f.get('author', ''))):
        if p.lower() == 'others': names.append(None); continue
        names.append(p.split(',')[0].strip() if ',' in p else p.split()[-1])
    if not names: return clean(f.get('title', key))
    if len(names) == 1 and names[0]: return names[0]
    if len(names) == 2 and all(names): return '%s and %s' % tuple(names)
    return names[0] + ' et al.'


def cite_text(txt):
    parts = re.split(r'((?:\[CITE:\w+\]\s*)+)', txt); out = []
    for i, part in enumerate(parts):
        keys = re.findall(r'\[CITE:(\w+)\]', part)
        if keys:
            prev = ''.join(parts[:i]).rstrip()
            if (prev == '' or prev.endswith('.')) and len(keys) == 1:
                out.append(tex(short_name(keys[0])) + r'~\cite{%s}' % keys[0])
            else:
                out.append(r'~\cite{%s}' % ','.join(keys))
            if part.endswith(' '): out.append(' ')
        else: out.append(tex(part))
    return ''.join(out).replace(' ~\\cite', '~\\cite')


ext = read('extraction_table.csv'); appr = read('quality_appraisal.csv'); summ = {r['Key']: r for r in read('study_summaries.csv')}
TOP = list(TOPIC.values())
L = []; w = L.append
w(r'''\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathptmx}
\usepackage[margin=2cm]{geometry}
\usepackage{amsmath}
\usepackage{longtable,booktabs,array}
\usepackage{cite}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}
\begin{document}
\begin{center}
{\Large\bfseries Supplementary Material}\\[4pt]
{\large Meta-Learning Orchestration of Learning Modalities on Resource-Constrained Robots: A Systematic Review}\\[4pt]
Yeshwanth Guru and Dev Kunwar Singh Chauhan\\
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India
\end{center}

\noindent Contents: S1 PRISMA 2020 checklist; S2 search strategy; S3 corrections to the initial list; S4 evidence, edge and signal coding of the 180 works; S5 quality appraisal; S6 study summaries. All tables are generated from the data package (Data Availability of the article).
''')

# S1 PRISMA checklist
items = [('Title', 'Identify the report as a systematic review', 'Title'),
         ('Abstract', 'Structured summary', 'Abstract'),
         ('Rationale', 'Rationale in the context of existing knowledge', 'Sections I-A, I-E'),
         ('Objectives', 'Explicit research questions', 'Section I-D (RQ1--RQ5)'),
         ('Eligibility criteria', 'Inclusion and exclusion criteria', 'Section II-A'),
         ('Information sources', 'Sources and date last searched', 'Section II-B; S2'),
         ('Search strategy', 'Full search strategy', 'S2 (stage-2 strings not logged; concept blocks given)'),
         ('Selection process', 'Screening method and reviewers', 'Sections II-A, II-F'),
         ('Data collection process', 'Extraction method', 'Section II-C'),
         ('Data items', 'Variables extracted', 'Section II-C; codebook of the data package'),
         ('Study risk of bias', 'Appraisal method', 'Section II-E; S5'),
         ('Effect measures', 'Not applicable (no pooled effect)', '--'),
         ('Synthesis methods', 'Narrative synthesis and counts', 'Section II-F'),
         ('Reporting bias assessment', 'Discussed as a threat to validity', 'Section II-F'),
         ('Certainty assessment', 'Evidence levels E1--E6', 'Section II-D'),
         ('Study selection', 'Flow of records', 'Section II-B; Fig. 2'),
         ('Study characteristics', 'Characteristics of each work', 'S4; data package'),
         ('Risk of bias in studies', 'Appraisal results', 'Table II; S5'),
         ('Results of syntheses', 'Synthesis by topic and RQ', 'Sections III--XV'),
         ('Discussion', 'Interpretation, limitations, implications', 'Sections II-F, XV--XVII'),
         ('Registration and protocol', 'Registration', 'Section II (OSF, retrospective)'),
         ('Support', 'Funding', 'Acknowledgment'),
         ('Competing interests', 'Declarations', 'Cover letter'),
         ('Availability of data and code', 'Data and code', 'Data Availability; supplementary code')]
w(r'\section*{S1 PRISMA 2020 checklist}')
w(r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{4cm}>{\raggedright\arraybackslash}p{6.5cm}>{\raggedright\arraybackslash}p{5.5cm}@{}}')
w(r'\toprule \textbf{Item} & \textbf{Requirement} & \textbf{Location} \\ \midrule \endhead')
for a, b, c in items: w('%s & %s & %s \\\\' % (tex(a), tex(b), tex(c)))
w(r'\bottomrule\end{longtable}')

# S2 search strategy
ss = open(os.path.join(DATA, 'search_strings.md'), encoding='utf-8').read()
blocks = re.search(r'```\n(.*?)```', ss, re.S).group(1)
w(r'\section*{S2 Search strategy}')
w(r'Stage 1: curated reading list of 108 works, each checked against its arXiv or publisher record (corrections in S3). '
  r'Stage 2 (September 2026): structured searches of arXiv, the proceedings of CoRL, RSS, ICRA, IROS, NeurIPS, ICML and ICLR, '
  r'and publisher sites, in ten topic streams, with backward citation chasing from the included reviews; 72 works added. '
  r'The exact strings and hit counts were not logged; the concept blocks below reconstruct their scope.')
w(r'{\scriptsize\begin{verbatim}' + '\n' + blocks + r'\end{verbatim}}')
w(r'Stage 3 (4 October 2026): targeted web search on the title topic (five topic and four verification queries). '
  r'Seven new records: three excluded (talk page; non-embodied agent; LLM-only compute allocation) and four recorded as '
  r'candidates for full-text screening (uncertainty-based LLM routing, arXiv:2502.11021; a systematic survey of efficient VLAs, '
  r'arXiv:2510.17111; budgeted skill practice, arXiv:2608.13415; online metareasoning, AAMAS 2026). None was added to the corpus.')

# S3 corrections
osf = open(os.path.join(ROOT, 'Survey3_method_workbook', 'OSF_protocol.md'), encoding='utf-8').read()
corr = [l[2:] for l in osf.split('## 6.')[1].splitlines() if l.startswith('- ')]
w(r'\section*{S3 Corrections to the initial list}')
w(r'\begin{itemize}\setlength{\itemsep}{0pt}')
for c in corr: w(r'\item ' + tex(c))
w(r'\end{itemize}')

# S4 coding of all works
w(r'\section*{S4 Evidence level, edge class and confidence-signal class of the 180 works}')
w(r'Edge class: P Pi-class or embedded CPU; J embedded GPU; W workstation GPU; D datacenter or cloud; U not stated. '
  r'Signal class: C conformal or calibrated; E epistemic uncertainty; F failure, anomaly or novelty score; V policy variance or entropy; '
  r'Q routing score or predicted quality; N none. Basis: F full text, A abstract, S standard reference. Reviews are not coded.')
EC = {'Pi-class or embedded CPU': 'P', 'Embedded GPU': 'J', 'Workstation GPU': 'W', 'Datacenter or cloud': 'D', 'Not stated': 'U', 'Not applicable': '--'}
SC = {'Conformal or calibrated': 'C', 'Epistemic uncertainty': 'E', 'Failure, anomaly or novelty score': 'F', 'Policy variance or entropy': 'V',
      'Routing score or predicted quality': 'Q', 'None': 'N', 'Not applicable': '--'}
for t in TOP:
    rows = [r for r in ext if r['Topic'] == t]
    w(r'\subsection*{%s (%d)}' % (tex(t), len(rows)))
    w(r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{4.0cm}cccc>{\raggedright\arraybackslash}p{7.6cm}@{}}')
    w(r'\toprule \textbf{Work} & \textbf{Level} & \textbf{Edge} & \textbf{Signal} & \textbf{Basis} & \textbf{Key result} \\ \midrule \endhead')
    for r in rows:
        w(r'%s~\cite{%s} & %s & %s & %s & %s & %s \\' % (tex(r['Study']), r['Key'], r['Evidence level'], EC[r['Edge class']],
                                                       SC[r['Confidence signal class']], r['Basis'][0], tex(r['Key result'])))
    w(r'\bottomrule\end{longtable}')

# S5 appraisal
w(r'\section*{S5 Quality appraisal of the 161 primary studies}')
w(r'Q1 method specification; Q2 baseline comparison; Q3 physical validation; Q4 compute reporting; Q5 quantitative evaluation; '
  r'Q6 code or model release; Q7 confidence signal. M met, P partly met, N not met, ? not assessable without the full text. '
  r'Coded by the rules of the codebook from the extraction fields; to be confirmed against the full texts.')
w(r'\begin{longtable}{@{}>{\raggedright\arraybackslash}p{5.5cm}cccccccc@{}}')
w(r'\toprule \textbf{Work} & \textbf{Level} & \textbf{Q1} & \textbf{Q2} & \textbf{Q3} & \textbf{Q4} & \textbf{Q5} & \textbf{Q6} & \textbf{Q7} \\ \midrule \endhead')
name = {r['Key']: r['Study'] for r in ext}
for r in appr:
    q = [r[c] for c in list(r)[3:]]
    w(r'%s~\cite{%s} & %s & %s \\' % (tex(name[r['Study key']]), r['Study key'], r['Evidence level'], ' & '.join(q)))
w(r'\bottomrule\end{longtable}')

# S6 summaries
w(r'\section*{S6 Study summaries}')
w(r'One summary per included work, grouped by topic. The level and the basis of each summary are given in brackets; '
  r'summaries based on an abstract should be read with that limitation, and figures not given in the abstract are not quoted.')
for t in TOP:
    w(r'\subsection*{%s}' % tex(t))
    for r in ext:
        if r['Topic'] == t:
            sm = summ[r['Key']]
            w(r'\paragraph{%s (%s; %s).} %s' % (tex(r['Study']), r['Evidence level'], sm['Basis'].lower(), cite_text(sm['Summary_keyed'])) + '\n')

w(r'''
\bibliographystyle{IEEEtran}
\bibliography{refs}
\end{document}
''')
open(OUT, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', OUT)
