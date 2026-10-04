"""Generate Online Resource 1 (supplement.tex) of Survey 2 from the data package.

Run from github/m:  python3 tools/make_supplement.py
Then compile:       cd Survey2_AIR_LaTeX_Overleaf && pdflatex supplement && bibtex supplement && pdflatex supplement && pdflatex supplement
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'Survey2_data_package')
OUT = os.path.join(ROOT, 'Survey2_AIR_LaTeX_Overleaf', 'supplement.tex')

TITLE = ('Quantum Cognition for Robot Decision-Making: A Systematic Review of Quantum-Like Models '
         'for Autonomous Agents')
AUTHORS = 'Yeshwanth Guru and Dev Kunwar Singh Chauhan'

UNI = {'×': r'$\times$', '≈': r'$\approx$', '≤': r'$\leq$', '≥': r'$\geq$',
       'ε': r'$\varepsilon$', '–': '--', '—': '---', '‘': '`', '’': "'",
       '“': '``', '”': "''", '…': r'\ldots{}', '→': r'$\rightarrow$',
       '±': r'$\pm$', '−': '$-$', 'σ': r'$\sigma$', 'γ': r'$\gamma$',
       'θ': r'$\theta$', 'ψ': r'$\psi$', 'ρ': r'$\rho$', '‖': r'$\|$',
       '·': r'$\cdot$', '′': "'", ' ': ' ', ' ': ' ', 'μ': r'$\mu$',
       '⊗': r'$\otimes$', '⟨': r'$\langle$', '⟩': r'$\rangle$', 'π': r'$\pi$'}


def tex(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'), ('^', r'\^{}')]:
        s = s.replace(a, b)
    s = s.replace(r'\textbackslash\{\}', r'\textbackslash{}')
    s = s.replace('|', r'$|$')
    s = s.replace('P\u0304', r'$\bar{P}$')
    return ''.join(UNI.get(c, c) for c in s)


def read(name):
    with open(os.path.join(DATA, name), encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


apps = read('extraction_table.csv')
appr = read('quality_appraisal.csv')
theory = read('theory_evidence_studies.csv')

L = []
w = L.append
w(r'''\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

\usepackage[margin=2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{longtable,booktabs,array,pdflscape,graphicx}
\usepackage[authoryear,round]{natbib}
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}
\renewcommand{\thetable}{S\arabic{table}}
\renewcommand{\thefigure}{S\arabic{figure}}
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
\setlength{\LTcapwidth}{\linewidth}
\begin{document}
\begin{center}
{\Large\bfseries Online Resource 1}\\[4pt]
{\large Supplementary material for ``''' + TITLE + r'''''}\\[4pt]
''' + AUTHORS + r'''\\
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India\\
Artificial Intelligence Review
\end{center}

\noindent This resource contains the data-extraction table of the ''' + str(len(apps)) + r''' application studies (Table~S1), the PRISMA 2020 checklist (Table~S2), the flow of records (Table~S3 and Figure~S1), the quality-appraisal criteria and judgements (Tables~S4 and S5), the search strategy and the record of the targeted search (Table~S6), the studies excluded under criterion E5 (Table~S7), a glossary of symbols (Table~S8) and the classification of the ''' + str(len(theory)) + r''' theory and evidence studies (Table~S9). Section numbers refer to the main article. Tables~S1 and S5 are also provided as CSV files (Online Resources 3 and 4). Evidence levels: E1 conceptual; E2 formal model; E3 human data; E4 simulation or benchmark; E5 physical system; E6 field deployment.
''')

# Table S1
w(r'''
\begin{landscape}
\footnotesize
\begin{longtable}{@{}P{3.0cm}P{2.2cm}P{2.1cm}P{0.6cm}P{4.2cm}P{4.6cm}P{4.4cm}P{1.0cm}@{}}
\caption{Data-extraction table of the application studies ($n = ''' + str(len(apps)) + r'''$): domain, model type, evidence level, task, key result, main limitation and basis of extraction (full text or abstract). $^\dagger$ also discussed in the companion survey.}\label{tab:S1}\\
\toprule
\textbf{Study} & \textbf{Domain} & \textbf{Model type} & \textbf{Level} & \textbf{Task or phenomenon} & \textbf{Key result} & \textbf{Main limitation} & \textbf{Basis} \\ \midrule
\endfirsthead
\toprule
\textbf{Study} & \textbf{Domain} & \textbf{Model type} & \textbf{Level} & \textbf{Task or phenomenon} & \textbf{Key result} & \textbf{Main limitation} & \textbf{Basis} \\ \midrule
\endhead
\bottomrule
\endfoot
''')
for r in apps:
    dag = r'$^\dagger$' if r['Also in companion survey'] == 'Yes' else ''
    w(r'\citet{%s}%s & %s & %s & %s & %s & %s & %s & %s \\' % (
        r['Key'], dag, tex(r['Domain']), tex(r['Model type']), r['Evidence level'],
        tex(r['Task or phenomenon']), tex(r['Key result']), tex(r['Limitation']), r['Basis']))
w(r'''\end{longtable}
\end{landscape}
''')

# Table S2 PRISMA checklist
prisma = [
    ('1', 'Title', 'Title page (identified as a systematic review)'),
    ('2', 'Abstract', 'Abstract (unstructured, as required by the journal)'),
    ('3', 'Rationale', 'Sections 1.1--1.4'),
    ('4', 'Objectives', 'Section 2.1 (RQ1--RQ5)'),
    ('5', 'Eligibility criteria', 'Section 2.3 (I1--I3, E1--E6)'),
    ('6', 'Information sources', 'Section 2.2; Table S6 (sources and dates)'),
    ('7', 'Search strategy', 'Section 2.2; Table S6 (concept blocks of stage 3; exact queries of stage 4)'),
    ('8', 'Selection process', 'Section 2.4'),
    ('9', 'Data collection process', 'Section 2.5'),
    ('10a', 'Data items (outcomes)', 'Section 2.5; Table S1; Online Resource 3'),
    ('10b', 'Data items (other variables)', 'Sections 2.5 and 2.6 (model type, domain, publication status, basis)'),
    ('11', 'Study risk of bias assessment', 'Section 2.5 (criteria Q1--Q7); Tables S4 and S5'),
    ('12', 'Effect measures', 'Not applicable: heterogeneous tasks and metrics; no pooled effect (Section 2.6)'),
    ('13a--f', 'Synthesis methods', 'Narrative synthesis by domain and evidence level (Sections 2.6 and 14.1); meta-analysis, heterogeneity and sensitivity analyses not applicable'),
    ('14', 'Reporting bias assessment', 'Section 2.6 (threats to validity: publication bias)'),
    ('15', 'Certainty assessment', 'Section 2.6 (evidence levels E1--E6, Table 2)'),
    ('16a', 'Study selection', 'Sections 2.2--2.4; Figure S1; Table S3'),
    ('16b', 'Excluded studies', 'Section 2.3; Tables S6 and S7'),
    ('17', 'Study characteristics', 'Table S1; Online Resource 3'),
    ('18', 'Risk of bias in studies', 'Section 14.1; Table S5; Online Resource 4'),
    ('19', 'Results of individual studies', 'Table S1; Sections 7--13'),
    ('20a--d', 'Results of syntheses', 'Sections 5 and 7--13; Section 14.1 and Figure 8'),
    ('21', 'Reporting biases', 'Section 2.6'),
    ('22', 'Certainty of evidence', 'Section 14.1; Table 2'),
    ('23a--d', 'Discussion', 'Sections 14--15 and 18; limitations of the review in Section 2.6'),
    ('24a', 'Registration', 'Section 2 (retrospective OSF registration)'),
    ('24b', 'Protocol', 'Section 2 (OSF registration)'),
    ('24c', 'Amendments', 'Sections 2.2 and 2.3: criterion E5 and the stage 4 search were added after the first corpus was assembled'),
    ('25', 'Support', 'Declarations (no external funding)'),
    ('26', 'Competing interests', 'Declarations'),
    ('27', 'Availability of data, code and other materials', 'Declarations; Online Resources 2--4'),
]
w(r'''
\begin{longtable}{@{}P{1.2cm}P{4.6cm}P{10.6cm}@{}}
\caption{PRISMA 2020 checklist: location of each item in the main article and this resource.}\label{tab:S2}\\
\toprule \textbf{Item} & \textbf{Topic} & \textbf{Location} \\ \midrule \endfirsthead
\toprule \textbf{Item} & \textbf{Topic} & \textbf{Location} \\ \midrule \endhead
\bottomrule \endfoot
''')
for a, b, c in prisma:
    w(r'%s & %s & %s \\' % (a, b, c))
w(r'\end{longtable}')

# Table S3 flow and Figure S1
n_appr = len(appr)
w(r'''
\begin{longtable}{@{}P{9.5cm}P{6.8cm}@{}}
\caption{Flow of records. Counts for stages 1--3 are works retained after verification; the number of records each search returned and the number excluded at each screening step were not logged and cannot be reported.}\label{tab:S3}\\
\toprule \textbf{Stage} & \textbf{Count} \\ \midrule \endfirsthead
\bottomrule \endfoot
Stage 1: curated reading list, checked against publisher, arXiv or repository records & 102 items listed; about 20 corrected, 3 unlocatable items replaced by 2 verified papers, 2 non-existent titles replaced, 2 dropped \\
Stage 2: authors' PDFs identified by first-page text & 31 works added \\
Stage 3: structured searches and citation chasing (two streams) & 74 works added; records not logged \\
Corpus after stages 1--3 & 205 works \\
Stage 4: targeted search (4 October 2026) and companion-survey cross-check & 17 queries; 10 new records + 1 record; 4 included, 2 excluded, 5 not retrieved (Table S6) \\
Works assessed against I1--I3 and E1--E6 & 209 \\
Excluded as primary studies under E5 (cited once; reviewed in the companion survey) & 11 (Table S7) \\
Application studies (I1), graded & ''' + str(len(apps)) + r''' \\
\quad of which appraised against Q1--Q7 (levels E2--E6) & ''' + str(n_appr) + r''' \\
Theory and evidence studies (I2), graded & ''' + str(len(theory)) + r''' \\
Reviews and background works (I3), not graded & 17 and 43 \\
Methodological references & 3 \\
Total works cited & 212 \\
\end{longtable}

\begin{figure}[ht]
\centering
\includegraphics[width=0.92\linewidth]{figures/FigS1_prisma.png}
\caption{Flow of records, following the PRISMA 2020 flow diagram. Stages whose record counts were not logged are marked as such (Table S3).}\label{fig:S1}
\end{figure}
''')

# Table S4 rubric
rubric = [
    ('Q1', 'Model specification', 'State space, state preparation, operators (projectors, instruments, unitaries or Hamiltonians) and free parameters stated.', 'Model only sketched, or parameters not all stated.', 'Model not specified.'),
    ('Q2', 'Classical comparison', 'A classical Bayesian, Markov, utility or neural model evaluated on the same task and data.', 'Classical model discussed but not evaluated on equal terms, or only weak baselines.', 'No classical comparison.'),
    ('Q3', 'Empirical grounding', 'Human behavioural or neural data, or a realistic agent or AI task.', 'Narrow benchmark, aggregate data from a few classic paradigms, or a single small case.', 'Toy example or no data.'),
    ('Q4', 'Parameter discipline', 'Parameters predicted or constrained a priori (e.g., QQ test, phase heuristics), or the model validated on held-out data.', 'Some parameters constrained, others fitted to the data they explain.', 'Free parameters fitted to the data they explain, or no evaluation.'),
    ('Q5', 'Quantitative evaluation', 'Metrics reported with variability (repetitions, confidence intervals or tests).', 'Metrics without variability, or partly qualitative.', 'Qualitative only.'),
    ('Q6', 'Reproducibility', 'Code and data released.', 'Code or data released, or the model fully specified in the paper so that it can be re-implemented.', "Neither released (``available on request'' counts as not met)."),
    ('Q7', 'Critical discussion', 'Limitations and classical alternative explanations discussed in depth.', 'Limitations mentioned briefly.', 'No discussion of limitations.'),
]
w(r'''
\begin{longtable}{@{}P{0.7cm}P{2.6cm}P{4.6cm}P{4.4cm}P{4.0cm}@{}}
\caption{Quality-appraisal criteria for application studies. Each criterion was judged met (M), partly met (P) or not met (N); the judgements were not summed into a score. Q6 cannot be judged from an abstract and is marked ``?'' when the full text was not available.}\label{tab:S4}\\
\toprule \textbf{ID} & \textbf{Criterion} & \textbf{Met (M)} & \textbf{Partly met (P)} & \textbf{Not met (N)} \\ \midrule \endfirsthead
\bottomrule \endfoot
''')
for r in rubric:
    w(r'%s & %s & %s & %s & %s \\' % r)
w(r'\end{longtable}')

# Table S5 appraisal
crit = ['Q1 Model specification', 'Q2 Classical comparison', 'Q3 Empirical grounding', 'Q4 Parameter discipline',
        'Q5 Quantitative evaluation', 'Q6 Reproducibility', 'Q7 Critical discussion']
w(r'''
\begin{longtable}{@{}P{5.2cm}P{1.6cm}cccccccc@{}}
\caption{Quality appraisal of the ''' + str(n_appr) + r''' application studies at levels E2--E6 (the six conceptual E1 studies are not appraised). M = met; P = partly met; N = not met; ? = not assessable without the full text. Basis: source of the judgements.}\label{tab:S5}\\
\toprule \textbf{Study} & \textbf{Basis} & \textbf{Q1} & \textbf{Q2} & \textbf{Q3} & \textbf{Q4} & \textbf{Q5} & \textbf{Q6} & \textbf{Q7} \\ \midrule \endfirsthead
\toprule \textbf{Study} & \textbf{Basis} & \textbf{Q1} & \textbf{Q2} & \textbf{Q3} & \textbf{Q4} & \textbf{Q5} & \textbf{Q6} & \textbf{Q7} \\ \midrule \endhead
\bottomrule \endfoot
''')
for r in appr:
    w(r'\citet{%s} & %s & %s \\' % (r['Study key'], r['Basis'], ' & '.join(r[c] for c in crit)))
w(r'\end{longtable}')
from collections import Counter
cnt = [Counter(r[c] for r in appr) for c in crit]
w(r'\noindent Totals (met / partly met / not met / not assessable): ' + '; '.join(
    '%s %d/%d/%d/%d' % (c.split()[0], k['M'], k['P'], k['N'], k['?']) for c, k in zip(crit, cnt)) + '.')

# Table S6 search
w(r'''
\subsection*{Search strategy}
\noindent\textbf{Stages 1--3.} Sources: Google Scholar, Semantic Scholar, arXiv, PubMed and publisher sites, with backward and forward citation chasing from the main reviews \citep{Pothos2022,Huang2025b,Widdows2021,Meyer2022}. The two search streams covered (a) applications of quantum cognition to robots, agents, human--machine teams and reinforcement learning, and (b) quantum-cognition theory, critiques, machine learning, large language models and neuroscience published from 2016 to 2026. The exact strings and record counts were not logged. To support replication, the following concept blocks reproduce the scope of the two streams; they are a reconstruction, not a log:

\begin{quote}\small
(\texttt{"quantum cognition" OR "quantum-like" OR "quantum probability" OR "quantum decision theory" OR "quantum-inspired" OR "projective simulation"})\\
AND (\texttt{robot* OR agent* OR "human-robot" OR autonomous OR "multi-agent" OR swarm OR "reinforcement learning" OR "machine learning" OR "language model*" OR trust OR automation})\\
\emph{or}, for stream (b), AND (\texttt{"order effect*" OR "conjunction fallacy" OR "disjunction effect" OR "sure-thing" OR interference OR contextuality OR "Bayesian network*" OR critique})
\end{quote}

\noindent\textbf{Stage 4 (4 October 2026).} Exact queries, results and decisions are given in Table~S6.
''')
topic = [
    ('T1', 'quantum-like model human-robot interaction decision-making robot 2024 2025', 'Genoa research-project page (excluded, E6)'),
    ('T2', 'quantum cognition large language model order effects 2025 arXiv quantum probability', 'Kak (2018) and Nebli et al. (2026) (included); arXiv:2510.13894 (not retrieved)'),
    ('T3', 'quantum probability model trust automation human-autonomy teaming 2024 2025 study', 'Flight-test trust case study (excluded, not a quantum model); arXiv:2410.20496 and arXiv:2503.16227 (not retrieved)'),
    ('T4', 'quantum-like Bayesian network decision support autonomous driving or robot 2023 2024 2025', 'No new record'),
    ('T5', 'quantum decision theory artificial agents reinforcement learning quantum-like agent Yukalov 2024 2025', 'No new record'),
    ('T6', 'quantum-inspired cognitive model robot emotion social robot 2024 2025 quantum-like', 'Hoorn and Ho (2019) (included); J. Phys.: Conf. Ser. 2115, 012040 (not retrieved)'),
    ('V1--V11', 'Eleven verification queries (titles, authors and abstracts of the records above)', 'arXiv:2608.14691 seen as a title only (not retrieved)'),
    ('Other', 'Cross-check against the companion survey\'s corpus', 'Essalmi et al. (2026) (included)'),
]
w(r'''
\begin{longtable}{@{}P{1.3cm}P{7.6cm}P{7.4cm}@{}}
\caption{Targeted search of 4 October 2026: queries and decisions. The full log, including the verification queries, is in the method workbook (targeted\_search\_record.md).}\label{tab:S6}\\
\toprule \textbf{\#} & \textbf{Query} & \textbf{New records and decisions} \\ \midrule \endfirsthead
\bottomrule \endfoot
''')
for a, b, c in topic:
    w(r'%s & \texttt{%s} & %s \\' % (a, tex(b), c) if a.startswith('T') else r'%s & %s & %s \\' % (a, b, c))
w(r'\end{longtable}')

# Table S7 E5 exclusions
e5 = [('Chen2020', 'Variational quantum circuits as Q-function approximators'),
      ('Jerbi2021', 'Parametrised quantum policies; learning separations on constructed tasks'),
      ('Skolik2022', 'Variational deep Q-learning (CartPole)'),
      ('Acuto2022', 'Variational quantum soft actor-critic for a simulated arm'),
      ('Sinha2023', 'Quantum critic for self-driving navigation (Nav-Q)'),
      ('Hohenfeld2024', 'Variational deep Q-learning for robot navigation'),
      ('Yun2022', 'Quantum multi-agent reinforcement learning'),
      ('Paparo2014', 'Quantum speed-up of agent deliberation (quantum walks)'),
      ('Chella2022', 'Grover search for robot motion planning'),
      ('Mannone2022', 'Quantum-circuit models of swarm interaction rules'),
      ('Khoshnoud2020', 'Quantum communication for cooperating robots')]
w(r'''
\begin{longtable}{@{}P{4.6cm}P{11.7cm}@{}}
\caption{Studies excluded as primary studies under criterion E5 (quantum computation used only to accelerate a robot or learning task, without a cognitive or decision model). They are reviewed in the companion survey \citep{Guru2026} and cited once in the main article to mark the boundary.}\label{tab:S7}\\
\toprule \textbf{Study} & \textbf{Method} \\ \midrule \endfirsthead
\bottomrule \endfoot
''')
for k, m in e5:
    w(r'\citet{%s} & %s \\' % (k, m))
w(r'\end{longtable}')

# Table S8 glossary
gl = [(r'$|\psi\rangle$, $\langle\psi|$', 'State vector (ket) and its conjugate transpose (bra)'),
      (r'$\langle\phi|\psi\rangle$', 'Inner product'),
      (r'$\rho$', r'Density matrix (mixed state); $\mathrm{tr}\,\rho = 1$, $\rho \succeq 0$'),
      (r'$P_A$', "Projector onto the ``yes'' subspace of question A"),
      (r'$I - P_A$', "Projector onto the ``no'' subspace"),
      (r'$[A, B] = AB - BA$', 'Commutator; zero for compatible questions'),
      (r'$\lVert P|\psi\rangle\rVert^2$', 'Born-rule probability'),
      (r'$U(t) = \exp(-iHt)$', 'Unitary evolution generated by Hamiltonian $H$'),
      (r'$L_k$, $\gamma_k$', 'Lindblad (jump) operators and rates in open-system models'),
      (r'$\otimes$', 'Tensor product of spaces or states'),
      (r'$\theta$', 'Interference phase between two branches'),
      ('QQ', 'Quantum question equality'),
      ('QLBN', 'Quantum-like Bayesian network'),
      ('QRL, QiRL', 'Quantum and quantum-inspired reinforcement learning'),
      ('PQC, VQC', 'Parametrised and variational quantum circuit'),
      ('PS', 'Projective simulation'),
      ('CbD', 'Contextuality-by-default'),
      ('POVM', 'Positive-operator-valued measure (generalised measurement)'),
      ('QPU', 'Quantum processing unit')]
w(r'''
\begin{longtable}{@{}P{4.2cm}P{12.1cm}@{}}
\caption{Glossary of symbols and notation.}\label{tab:S8}\\
\toprule \textbf{Symbol} & \textbf{Meaning} \\ \midrule \endfirsthead
\bottomrule \endfoot
''')
for a, b in gl:
    w(r'%s & %s \\' % (a, b))
w(r'\end{longtable}')

# Table S9 theory
w(r'''
\footnotesize
\begin{longtable}{@{}P{3.6cm}P{0.7cm}P{4.6cm}P{6.2cm}P{1.1cm}@{}}
\caption{Theory and evidence studies ($n = ''' + str(len(theory)) + r'''$), graded on the evidence scale: phenomenon, key result and basis of extraction.}\label{tab:S9}\\
\toprule \textbf{Study} & \textbf{Level} & \textbf{Phenomenon} & \textbf{Key result} & \textbf{Basis} \\ \midrule \endfirsthead
\toprule \textbf{Study} & \textbf{Level} & \textbf{Phenomenon} & \textbf{Key result} & \textbf{Basis} \\ \midrule \endhead
\bottomrule \endfoot
''')
for r in theory:
    w(r'\citet{%s} & %s & %s & %s & %s \\' % (r['Key'], r['Evidence level'], tex(r['Phenomenon']), tex(r['Key result']), r['Basis']))
w(r'''\end{longtable}
\normalsize

\bibliographystyle{plainnat}
\bibliography{refs}
\end{document}
''')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))
print('wrote', OUT)
