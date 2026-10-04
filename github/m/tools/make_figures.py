"""Regenerate the data-driven figures of Survey 2 from the data package.

Fig7_evidence.png  evidence levels of the graded studies by domain (main article, Figure 7)
FigS1_prisma.png   flow of records (Online Resource 1, Figure S1)

Run from github/m:  python3 tools/make_figures.py
"""
import csv
import os
from collections import Counter, defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'Survey2_data_package')
FIG = os.path.join(ROOT, 'Survey2_AIR_LaTeX_Overleaf', 'figures')

LEVELS = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
LABELS = ['E1 Conceptual', 'E2 Formal model', 'E3 Human data', 'E4 Simulation/benchmark',
          'E5 Physical system', 'E6 Field deployment']
COLORS = ['#c9d1dc', '#5f6b7a', '#2b7bd6', '#1db07a', '#ec6b35', '#e8a000']
INK = '#1f2933'

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.edgecolor': '#8a94a3',
                     'axes.labelcolor': INK, 'xtick.color': INK, 'ytick.color': INK})


def read(name):
    with open(os.path.join(DATA, name), encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def evidence_figure():
    apps = read('extraction_table.csv')
    theory = read('theory_evidence_studies.csv')
    order = ['Decision models and networks', 'ML, NLP and IR', 'Deep learning and LLMs',
             'Reinforcement learning and agent learning', 'Robots and embodied agents',
             'Multi-agent systems and teams', 'Human-AI trust']
    short = {'Decision models and networks': 'Decision models\n& networks',
             'ML, NLP and IR': 'ML, NLP & IR',
             'Deep learning and LLMs': 'Deep learning\n& LLMs',
             'Reinforcement learning and agent learning': 'Reinforcement &\nagent learning',
             'Robots and embodied agents': 'Robots & embodied\nagents',
             'Multi-agent systems and teams': 'Multi-agent\nsystems & teams',
             'Human-AI trust': 'Human–AI trust'}
    counts = defaultdict(Counter)
    for r in apps:
        counts[r['Domain']][r['Evidence level']] += 1
    rows = [('Theory & evidence\nstudies (n = %d)' % len(theory), Counter(r['Evidence level'] for r in theory))]
    rows += [('%s (n = %d)' % (short[d], sum(counts[d].values())), counts[d]) for d in order]
    fig, ax = plt.subplots(figsize=(8.6, 4.9), dpi=300)
    y = list(range(len(rows)))[::-1]
    for yi, (_, c) in zip(y, rows):
        left = 0
        for lv, col in zip(LEVELS, COLORS):
            n = c.get(lv, 0)
            if n:
                ax.barh(yi, n, left=left, color=col, height=0.62, edgecolor='white', linewidth=0.6)
                if n >= 2:
                    ax.text(left + n / 2, yi, str(n), ha='center', va='center', fontsize=8.5,
                            color=INK if lv in ('E1', 'E6') else 'white')
                left += n
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9)
    ax.set_xlabel('Number of studies')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axhline(y[0] - 0.5, color='#8a94a3', lw=0.6, ls=':')
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in COLORS]
    ax.legend(handles, LABELS, loc='lower right', frameon=False, fontsize=8.5)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'Fig7_evidence.png'))
    plt.close(fig)


def box(ax, x, y, w, h, text, fc='#ffffff', ec='#5f6b7a', fs=7.8, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.006,rounding_size=0.01',
                                fc=fc, ec=ec, lw=0.9))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, color=INK,
            fontweight='bold' if bold else 'normal', wrap=True)


def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>', color='#5f6b7a', lw=0.9, shrinkA=0, shrinkB=0))


def prisma_figure():
    apps = read('extraction_table.csv')
    theory = read('theory_evidence_studies.csv')
    fig, ax = plt.subplots(figsize=(8.6, 7.6), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    side = '#eef2f6'
    # Stage labels
    for yy, lab in [(0.84, 'Identification'), (0.56, 'Screening and\neligibility'), (0.17, 'Included')]:
        ax.text(0.015, yy, lab, rotation=90, ha='center', va='center', fontsize=9, fontweight='bold', color=INK)
    # Identification
    box(ax, 0.05, 0.86, 0.20, 0.11, 'Stage 1\nCurated reading list\n(n = 102 items,\nverified and corrected)')
    box(ax, 0.27, 0.86, 0.20, 0.11, 'Stage 2\nAuthors’ PDFs, identified\nby first-page text\n(n = 31 works added)')
    box(ax, 0.49, 0.86, 0.22, 0.11, 'Stage 3\nStructured searches and\ncitation chasing\n(n = 74 works added;\nrecords not logged)')
    box(ax, 0.73, 0.86, 0.25, 0.11, 'Stage 4 (4 October 2026)\nTargeted search: 17 queries,\n10 new records; companion-\nsurvey cross-check: 1 record')
    box(ax, 0.05, 0.71, 0.42, 0.08, 'Corpus after stages 1–3\n(n = 205 works)')
    for x in (0.15, 0.37):
        arrow(ax, x, 0.86, x, 0.79)
    arrow(ax, 0.60, 0.86, 0.47, 0.775)
    box(ax, 0.62, 0.71, 0.36, 0.08, 'Stage 4 records assessed (n = 11)\nExcluded: E6 project web page (1);\nnot a quantum model (1); not retrieved (5)', fc=side)
    arrow(ax, 0.855, 0.86, 0.855, 0.79)
    # Screening and eligibility
    box(ax, 0.05, 0.50, 0.42, 0.13, 'Works assessed for eligibility against\nI1–I3 and E1–E6\n(n = 205 + 4 = 209)')
    arrow(ax, 0.26, 0.71, 0.26, 0.63)
    arrow(ax, 0.62, 0.73, 0.47, 0.615)
    ax.text(0.515, 0.685, '4 included', fontsize=7.8, color=INK, ha='center', rotation=37)
    box(ax, 0.55, 0.47, 0.43, 0.19, 'Excluded as primary studies under E5\n(quantum computation used only as an\naccelerator; reviewed in the companion\nsurvey; cited once to mark the boundary)\n(n = 11)', fc=side)
    arrow(ax, 0.47, 0.565, 0.55, 0.565)
    # Included
    n_app, n_th = len(apps), len(theory)
    box(ax, 0.05, 0.28, 0.42, 0.12, 'Application studies (I1)\n(n = %d)\ngraded E1–E6; %d appraised (Q1–Q7)' % (
        n_app, sum(1 for r in apps if r['Evidence level'] != 'E1')), fc='#e3eefb', ec='#2b7bd6', bold=False)
    box(ax, 0.05, 0.12, 0.42, 0.12, 'Theory and evidence studies (I2)\n(n = %d)\ngraded E1–E6' % n_th, fc='#e3eefb', ec='#2b7bd6')
    box(ax, 0.55, 0.12, 0.43, 0.28, 'Not graded\nReviews (n = 17)\nBackground works (n = 43)\nMethod references (n = 3)\n\nTotal works cited: 212', fc=side)
    arrow(ax, 0.26, 0.50, 0.26, 0.40)
    arrow(ax, 0.48, 0.52, 0.55, 0.37)
    ax.text(0.05, 0.04, 'Counts for stages 1–3 are works added after verification; the number of records each search '
            'returned and\nexcluded at each screening step was not logged (Online Resource 1, Table S3).',
            fontsize=7.6, color='#3e4c59', va='bottom')
    fig.savefig(os.path.join(FIG, 'FigS1_prisma.png'), bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    evidence_figure()
    prisma_figure()
    print('figures written to', FIG)
