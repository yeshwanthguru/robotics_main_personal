"""Regenerate the data-driven figures of Survey 1 from extraction_table.csv.

fig7_years.png    primary studies by publication year and technology type
fig2_evidence.png evidence levels by technology type (reviews excluded)
fig6_prisma.png   PRISMA 2020 flow diagram (screening counts left blank)
Run from github/k:  python3 tools/make_figures.py
"""
import collections
import csv
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = 'Survey1_CSUR_LaTeX_Overleaf/figures/'
FOUNDATIONAL = 96
CATS = ['Quantum computation (incl. cognition models)', 'Quantum-inspired (classical hardware)',
        'Quantum sensing', 'Quantum communication', 'Review']
COLORS = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#b4b4b0']
INK, MUTED, GRID, AXIS = '#222222', '#555555', '#e4e4e0', '#b8b8b4'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})

rows = list(csv.DictReader(open('extraction_table.csv', encoding='utf-8-sig')))


def category(r):
    if r['Evidence level'] == 'Review':
        return 'Review'
    t = r['Quantum type'].lower()
    if t.startswith('quantum-inspired'):
        return CATS[1]
    if 'sensing' in t:
        return CATS[2]
    if 'communication' in t:
        return CATS[3]
    return CATS[0]


def style(ax):
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    for side in ('left', 'bottom'):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=MUTED)
    ax.set_axisbelow(True)


# --- publication years ---
bins = ['2006–2017'] + [str(y) for y in range(2018, 2027)]
counts = {c: [0] * len(bins) for c in CATS}
for r in rows:
    y = int(re.search(r'\[(\d{4})', r['Study']).group(1))
    counts[category(r)][bins.index('2006–2017' if y <= 2017 else str(y))] += 1
fig, ax = plt.subplots(figsize=(10, 4.6), dpi=220)
bottom = [0] * len(bins)
for c, col in zip(CATS, COLORS):
    ax.bar(bins, counts[c], bottom=bottom, color=col, width=0.62, edgecolor='white', linewidth=1.5, label=c, zorder=3)
    bottom = [a + b for a, b in zip(bottom, counts[c])]
for i, t in enumerate(bottom):
    if t:
        ax.text(i, t + 0.3, str(t), ha='center', va='bottom', color=INK)
ax.set_ylabel('Number of primary studies', color=MUTED)
ax.set_xlabel('Publication year', color=MUTED)
ax.set_ylim(0, max(bottom) + 3)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
style(ax)
ax.legend(loc='upper left', frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(OUT + 'fig7_years.png')
plt.close(fig)

# --- evidence levels ---
levels = ['L1 Theoretical', 'L2 Simulation', 'L3 QPU / hardware\nexperiment', 'L4 Robot-in-the-loop\n(simulated)',
          'L5 Physical robot /\nplatform demonstration', 'L6 End-to-end\ndeployment']
studies = [r for r in rows if r['Evidence level'] != 'Review']
ev = {c: [0] * 6 for c in CATS[:4]}
for r in studies:
    ev[category(r)][int(r['Evidence level'][1]) - 1] += 1
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
y = list(range(6))[::-1]
left = [0] * 6
for c, col in zip(CATS[:4], COLORS[:4]):
    ax.barh(y, ev[c], left=left, color=col, height=0.58, edgecolor='white', linewidth=1.5, label=c, zorder=3)
    left = [a + b for a, b in zip(left, ev[c])]
for yi, t in zip(y, left):
    ax.text(t + 0.4, yi, str(t), va='center', color=INK, fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(levels, color=MUTED)
ax.set_xlabel(f'Number of primary robotics studies (n = {len(studies)}; '
              f'{len(rows) - len(studies)} reviews excluded)', color=MUTED)
ax.set_xlim(0, max(left) + 3)
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
style(ax)
ax.legend(loc='lower right', frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(OUT + 'fig2_evidence.png')
plt.close(fig)

# --- PRISMA flow ---
n_rev = len(rows) - len(studies)
fig, ax = plt.subplots(figsize=(8.5, 7.5), dpi=200)
ax.set_xlim(0, 17)
ax.set_ylim(0, 15)
ax.axis('off')
NAVY, BLUE, GREY = '#21375f', '#2a78d6', '#9a9a96'


def box(x, y, w, h, text, edge):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.25',
                                fc='white', ec=edge, lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=11, color=INK, linespacing=1.4)


def arrow(x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='-|>', color='#555555', lw=2))


for (y0, h, label) in [(11.7, 2.8, 'Identification'), (5.9, 5.5, 'Screening'), (0.3, 5.3, 'Included')]:
    ax.add_patch(plt.Rectangle((0.2, y0), 0.9, h, color=NAVY))
    ax.text(0.65, y0 + h / 2, label, rotation=90, ha='center', va='center', color='white', fontsize=12, weight='bold')
box(1.7, 12.0, 6.8, 2.0, 'Records identified from databases\n(IEEE Xplore, ACM DL, Scopus, WoS,\nSpringerLink, ScienceDirect, arXiv)\nn = ____', BLUE)
box(9.8, 11.8, 6.9, 2.4, 'Duplicates removed n = ____\nAdded by snowballing n = ____\nAdded by web search (Oct 2026) n = 12', GREY)
box(1.7, 8.9, 6.8, 1.9, 'Records screened\n(title and abstract)\nn = ____', BLUE)
box(9.8, 8.9, 6.9, 1.9, 'Records excluded\nn = ____', GREY)
box(1.7, 6.2, 6.8, 1.9, 'Reports assessed for eligibility\n(full text)\nn = ____', BLUE)
box(9.8, 5.9, 6.9, 2.5, 'Reports excluded, with reasons:\nmetaphorical "quantum" n = ____\nno robotic relevance n = ____\nduplicate / earlier version n = ____\nother n = ____', GREY)
box(1.7, 0.7, 6.8, 2.6, f'Primary studies included\nn = {len(rows)}\n({len(studies)} studies + {n_rev} reviews;\n{FOUNDATIONAL} foundational refs cited separately)', BLUE)
arrow(5.1, 12.0, 5.1, 10.85)
arrow(5.1, 8.9, 5.1, 8.15)
arrow(5.1, 6.2, 5.1, 3.35)
for yy in (13.0, 9.85, 7.15):
    arrow(8.5, yy, 9.75, yy)
fig.tight_layout()
fig.savefig(OUT + 'fig6_prisma.png')
plt.close(fig)
print('figures written')
