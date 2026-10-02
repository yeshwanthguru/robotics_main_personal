"""Regenerate the data-driven figures of Survey 1 from extraction_table.csv.

fig7_years.png    primary studies by publication year and technology type
fig2_evidence.png evidence levels by technology type (reviews excluded)
fig6_prisma.png   PRISMA 2020 flow diagram (screening counts left blank)
Run from github/k:  python3 tools/make_figures.py
"""
import collections
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figstyle import plt, style_axes, INK, MUTED, GRID, COLORS  # noqa: E402

OUT = 'Survey1_CSUR_LaTeX_Overleaf/figures/'
FOUNDATIONAL = 94
CATS = ['Quantum computation (incl. cognition models)', 'Quantum-inspired (classical hardware)',
        'Quantum sensing', 'Quantum communication', 'Review']

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
    style_axes(ax)


# --- publication years: one bar per year from the first primary study, eras shaded ---
first = min(int(re.search(r'\[(\d{4})', r['Study']).group(1)) for r in rows)
yrs = list(range(first, 2027))
counts = {c: [0] * len(yrs) for c in CATS}
for r in rows:
    counts[category(r)][yrs.index(int(re.search(r'\[(\d{4})', r['Study']).group(1)))] += 1
fig, ax = plt.subplots(figsize=(10, 4.6), dpi=220)
for (a, b, label), fill in zip([(1994, 2005, 'Algorithms'), (2006, 2015, 'Early hardware'), (2016, 2026, 'NISQ era')],
                               ['#f4f4f2', '#fbfbfa', '#f4f4f2']):
    lo, hi = max(a, first) - first - 0.5, b - first + 0.5
    ax.axvspan(lo, hi, color=fill, zorder=0)
    ax.text((lo + hi) / 2, 1.0, label, transform=ax.get_xaxis_transform(), ha='center', va='bottom',
            fontsize=10.5, color='#2b2b2b', weight='bold')
bottom = [0] * len(yrs)
x = list(range(len(yrs)))
for c, col in zip(CATS, COLORS):
    nz = [i for i in x if counts[c][i]]
    ax.bar(nz, [counts[c][i] for i in nz], bottom=[bottom[i] for i in nz], color=col, width=0.72,
           edgecolor='white', linewidth=1.2, label=c, zorder=3)
    bottom = [a + b for a, b in zip(bottom, counts[c])]
for i, t in enumerate(bottom):
    if t:
        ax.text(i, t + 0.3, str(t), ha='center', va='bottom', color=INK, fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels([str(y) if (y - first) % 2 == 0 or y >= 2016 else '' for y in yrs], rotation=90, fontsize=9.5)
ax.set_xlim(-0.6, len(yrs) - 0.4)
ax.set_ylabel('Number of primary studies', color=MUTED)
ax.set_xlabel('Publication year', color=MUTED)
ax.set_ylim(0, max(bottom) + 3)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
style(ax)
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.93), frameon=True, facecolor='white', edgecolor='none', fontsize=9.5)
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
    ax.barh(y, ev[c], left=left, color=col, height=0.58, edgecolor='white', linewidth=0.8, label=c, zorder=3)
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
fig = plt.figure(figsize=(7.4, 5.0))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 7.4)
ax.set_ylim(0, 5.0)
ax.axis('off')
EDGE, SIDE = '#3a3a3a', '#e6e6e3'


def box(x, y, w, h, text, edge=EDGE):
    ax.add_patch(plt.Rectangle((x, y), w, h, fc='white', ec=edge, lw=0.9))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=9.5, color=INK, linespacing=1.35)


def arrow(x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>,head_length=0.4,head_width=0.2', color='#4a4a4a', lw=0.9))


for (y0, h, label) in [(3.75, 1.15, 'Identification'), (1.45, 2.2, 'Screening'), (0.1, 1.25, 'Included')]:
    ax.add_patch(plt.Rectangle((0.08, y0), 0.32, h, fc=SIDE, ec='none'))
    ax.text(0.24, y0 + h / 2, label, rotation=90, ha='center', va='center', fontsize=9.5, color=INK, weight='bold')
box(0.6, 3.85, 3.0, 0.95, 'Records identified from databases\n(IEEE Xplore, ACM DL, Scopus, WoS,\nSpringerLink, ScienceDirect, arXiv)\nn = ____')
box(4.2, 3.85, 3.1, 0.95, 'Duplicates removed n = ____\nAdded by snowballing n = ____\nAdded by targeted search n = 12', edge='#8a8a8a')
box(0.6, 2.75, 3.0, 0.7, 'Records screened (title and abstract)\nn = ____')
box(4.2, 2.75, 3.1, 0.7, 'Records excluded\nn = ____', edge='#8a8a8a')
box(0.6, 1.55, 3.0, 0.8, 'Reports assessed for eligibility\n(full text)\nn = ____')
box(4.2, 1.45, 3.1, 1.0, 'Reports excluded, with reasons:\nmetaphorical "quantum" n = ____\nno robotic relevance n = ____\nduplicate or earlier version n = ____', edge='#8a8a8a')
box(0.6, 0.2, 3.0, 1.0, f'Primary studies included: n = {len(rows)}\n({len(studies)} studies and {n_rev} reviews)\n'
    f'Foundational works cited: {FOUNDATIONAL}')
arrow(2.1, 3.85, 2.1, 3.45)
arrow(2.1, 2.75, 2.1, 2.35)
arrow(2.1, 1.55, 2.1, 1.2)
for yy in (4.32, 3.1, 1.95):
    arrow(3.6, yy, 4.2, yy)
fig.savefig(OUT + 'fig6_prisma.png')
plt.close(fig)

# --- timeline (Fig. 1): every milestone corresponds to a reference cited in Section 2.3 or later ---
QC = [
    (1982, 'Feynman: quantum simulation proposed'),
    (1985, 'Deutsch: universal quantum computer'),
    (1992, 'Deutsch–Jozsa: exponential separation'),
    (1994, 'Shor: factoring and discrete logarithms'),
    (1996, 'Grover: quadratic-speed-up search'),
    (2002, 'Amplitude amplification and estimation'),
    (2009, 'HHL linear-systems algorithm'),
    (2011, 'D-Wave: programmable quantum annealing'),
    (2014, 'VQE and QAOA: variational algorithms'),
    (2016, 'Public cloud access to gate-based QPUs'),
    (2018, 'NISQ era named (Preskill)'),
    (2019, 'Sycamore: beyond-classical sampling'),
    (2021, 'Dynamic circuits with real-time feedback'),
]
C, I, S, M, R = CATS[0], CATS[1], CATS[2], CATS[3], CATS[4]
ROB = [
    (1998, C, 'Benioff: concept of a quantum robot'),
    (2002, C, 'Benioff: no Grover gain for a moving robot'),
    (2002, I, 'Quantum-inspired evolutionary algorithm'),
    (2006, C, 'Dong et al.: quantum robot architecture'),
    (2008, C, 'Quantum reinforcement learning'),
    (2011, S, 'Atom-interferometer accelerometer flies'),
    (2012, I, 'Quantum-inspired RL drives a physical robot'),
    (2015, C, 'Planning mapped to a quantum annealer'),
    (2017, C, 'Annealer traffic-flow optimization'),
    (2017, R, 'First quantum-robotics book'),
    (2018, S, 'Hybrid quantum accelerometer (Kalman)'),
    (2018, I, 'Quantum-behaved PSO improves FastSLAM'),
    (2019, C, 'Annealer AGV control; 200-robot routing'),
    (2020, M, 'Photonic links on aerial and ground robots'),
    (2020, C, 'Annealer point-set registration (vision)'),
    (2021, C, 'qRobot: warehouse robot calls cloud QPUs'),
    (2021, M, 'Entanglement distributed between drones'),
    (2022, C, 'Grover motion planner; quantum SAC arm'),
    (2022, S, 'Three-axis hybrid quantum accelerometer'),
    (2023, C, 'Quantum swarm planning; solver benchmarks'),
    (2024, C, 'Variational deep Q-learning navigation'),
    (2024, M, 'Drone-based quantum key distribution'),
    (2025, C, '1,000-AGV routing; hybrid MAPF; 64-qubit IK'),
    (2025, C, 'Quantum policy balances physical cart-pole'),
    (2025, S, 'Quantum magnetic navigation flight trials'),
    (2025, M, 'Drone- and vehicle-based QKD'),
    (2026, C, 'Q-SpiRL policy executed on IBM hardware'),
    (2026, C, 'Control agent runs on a superconducting QPU'),
]
ERAS = [(1982, 1993, 'Theoretical\nfoundations'), (1994, 2005, 'Algorithms'),
        (2006, 2015, 'Early\nhardware'), (2016, 2026, 'NISQ era')]
ERA_FILL = ['#f4f4f2', '#fbfbfa', '#f4f4f2', '#fbfbfa']
NAVY_INK = '#2b2b2b'
years = sorted({y for y, _ in QC} | {y for y, _, _ in ROB})
LINE = 0.2
FS = 9.0
W = 7.6
heights = {y: max(sum(1 for q in QC if q[0] == y), sum(1 for r in ROB if r[0] == y)) * LINE + 0.065 for y in years}
total = sum(heights.values())
fig = plt.figure(figsize=(W, total + 0.55), dpi=250)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(-total - 0.05, 0.5)
ax.axis('off')
top = {}
yc = 0.0
for y in years:
    top[y] = yc
    yc -= heights[y]
XE, XY = 0.16, 3.55
XQ, XR = XY - 0.42, XY + 0.62
for (a, b, label), fill in zip(ERAS, ERA_FILL):
    ys = [y for y in years if a <= y <= b]
    y0, y1 = top[ys[0]], top[ys[-1]] - heights[ys[-1]]
    ax.add_patch(plt.Rectangle((0, y1), W, y0 - y1, color=fill, zorder=0))
    ax.text(XE, (y0 + y1) / 2, label, rotation=90, ha='center', va='center', fontsize=FS,
            color=NAVY_INK, weight='bold', linespacing=1.0)
ax.plot([XY, XY], [0.05, -total], color='#c9c9c4', lw=1.0, zorder=1)
for y in years:
    t = top[y] - 0.03
    ax.text(XY, t - LINE / 2, str(y), ha='center', va='center', fontsize=FS, weight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.22', fc='white', ec='#c9c9c4', lw=0.7), zorder=3)
    for k, (_, txt) in enumerate([q for q in QC if q[0] == y]):
        yy = t - LINE / 2 - k * LINE
        ax.plot(XQ + 0.12, yy, 'o', color=NAVY_INK, ms=4.5, zorder=3)
        ax.text(XQ, yy, txt, ha='right', va='center', fontsize=FS, color=INK)
    for k, (_, cat, txt) in enumerate([r for r in ROB if r[0] == y]):
        yy = t - LINE / 2 - k * LINE
        ax.plot(XR - 0.13, yy, 'o', color=COLORS[CATS.index(cat)], ms=5.5, zorder=3, mec='white', mew=0.8)
        ax.text(XR, yy, txt, ha='left', va='center', fontsize=FS, color=INK)
ax.text(XQ, 0.27, 'Quantum computing', ha='right', va='center', fontsize=FS + 1.5, weight='bold', color=NAVY_INK)
ax.text(XR, 0.27, 'Quantum robotics', ha='left', va='center', fontsize=FS + 1.5, weight='bold', color=NAVY_INK)
handles = [plt.Line2D([], [], marker='o', ls='', color=COLORS[i], ms=5.5, label=CATS[i].split(' (')[0])
           for i in range(4)] + [plt.Line2D([], [], marker='o', ls='', color=COLORS[4], ms=5.5, label='Review / book')]
ax.legend(handles=handles, loc='lower left', bbox_to_anchor=(0.06, 0.01), frameon=True, facecolor='white',
          edgecolor='#d8d8d4', fontsize=FS - 0.7, title='Robotics milestones', title_fontsize=FS - 0.7)
fig.savefig(OUT + 'fig3_timeline.png')
plt.close(fig)
print('timeline written')
