"""Draw the schematic figures of Survey 1: taxonomy (fig1), architecture (fig4), latency (fig5).

Run from github/k:  python3 tools/make_schematics.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figstyle import plt, box, arrow, style_axes, INK, MUTED, RULE, GRID, PANEL, COLORS, ACCENT  # noqa: E402

OUT = 'Survey1_CSUR_LaTeX_Overleaf/figures/'

# ---------------- Fig. taxonomy ----------------
COLS = [
    ('Optimization', ['QUBO formulations', 'Quantum annealing', 'QAOA, VQE'],
     ['AGV and fleet routing', 'Scheduling', 'Inverse kinematics']),
    ('Planning', ['Grover search', 'Amplitude amplification', 'Quantum walks'],
     ['Motion planning, MAPF', 'UAV and view planning', 'Localization']),
    ('Learning', ['Variational circuits', 'Quantum kernels', 'Quantum RL'],
     ['Navigation policies', 'Arm, cart-pole control', 'Perception']),
    ('Sensing and\ncommunication', ['Atom interferometry', 'Quantum magnetometry', 'Quantum key distribution'],
     ['GNSS-denied navigation', 'Secure drone links', 'Inertial sensing']),
    ('Decision-making', ['Quantum probability', 'Contextuality', 'Quantum game models'],
     ['Human-robot interaction', 'Driving interaction', 'Affective states']),
]
W, H = 7.9, 3.75
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
box(ax, W / 2 - 1.35, 3.27, 2.7, 0.38, 'Quantum technologies for robotics', fill=PANEL, edge=INK, size=10.5, weight='bold')
cw, gap, x0 = 1.47, 0.09, 0.12
centers = [x0 + i * (cw + gap) + cw / 2 for i in range(5)]
ax.plot([W / 2, W / 2], [3.27, 3.05], color=RULE, lw=0.9)
ax.plot([centers[0], centers[-1]], [3.05, 3.05], color=RULE, lw=0.9)
for i, (name, methods, tasks) in enumerate(COLS):
    x = x0 + i * (cw + gap)
    arrow(ax, [(centers[i], 3.05), (centers[i], 2.86)], lw=0.9)
    box(ax, x, 2.42, cw, 0.44, name, fill=PANEL, edge=INK, size=10, weight='bold')
    box(ax, x, 0.42, cw, 2.0)
    ax.text(x + 0.08, 2.27, 'Quantum methods', fontsize=8.3, color=MUTED, style='italic', va='center')
    for k, m in enumerate(methods):
        ax.text(x + 0.08, 2.05 - k * 0.22, m, fontsize=8.8, color=INK, va='center')
    ax.plot([x + 0.06, x + cw - 0.06], [1.32, 1.32], color=GRID, lw=0.8)
    ax.text(x + 0.08, 1.17, 'Representative tasks', fontsize=8.3, color=MUTED, style='italic', va='center')
    for k, t in enumerate(tasks):
        ax.text(x + 0.08, 0.95 - k * 0.22, t, fontsize=8.8, color=INK, va='center')
ax.text(W / 2, 0.2, 'Applied to every study: quantum or quantum-inspired, NISQ or fault-tolerant, evidence level, '
        'where the quantum part ran, dominant deployment constraint', ha='center', va='center', fontsize=8.5, color=MUTED)
fig.savefig(OUT + 'fig1_taxonomy.png')
plt.close(fig)

# ---------------- Fig. architecture ----------------
W, H = 7.6, 4.3
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
# frames, titles inside with clearance
box(ax, 0.1, 0.25, 3.7, 3.95, fill='#fafaf9', edge=RULE, z=0)
ax.text(0.25, 4.0, 'Robot (classical, onboard)', fontsize=10.5, weight='bold', color=INK, va='center')
box(ax, 4.75, 0.25, 2.75, 3.95, fill='#f4f7fb', edge=RULE, z=0)
ax.text(4.9, 4.0, 'Quantum resources', fontsize=10.5, weight='bold', color=INK, va='center')
ax.text(4.9, 3.74, 'remote (cloud) or edge (on-premise)', fontsize=9, color=MUTED, va='center')
stack = [('Sensors, including quantum sensors', 3.35), ('State estimation (Kalman or particle filter)', 2.65),
         ('Task and motion planning\n0.1–10 Hz, with classical fallback', 1.95),
         ('Control loop or learned policy\n10–1,000 Hz', 1.25), ('Actuators', 0.55)]
bx, bw, bh = 0.4, 3.1, 0.5
for text, yc in stack:
    box(ax, bx, yc - bh / 2, bw, bh, text, size=9.5)
for (_, y1), (_, y2) in zip(stack, stack[1:]):
    arrow(ax, [(bx + bw / 2, y1 - bh / 2), (bx + bw / 2, y2 + bh / 2)], lw=0.9)
qx, qw, qh = 4.95, 2.35, 0.78
quantum = [('(ii) Periodic optimization\nQUBO on an annealer; new plan\nevery few seconds to minutes', 2.95),
           ('(i) Offline training\nQPU trains a compact policy\nthat runs classically', 1.95),
           ('(iii) In-loop query\nQPU called inside every\ncontrol cycle', 0.95)]
for text, yc in quantum:
    box(ax, qx, yc - qh / 2, qw, qh, text, size=9, edge=ACCENT if not text.startswith('(iii)') else RULE,
        ls='-' if not text.startswith('(iii)') else '--')
right = bx + bw
arrow(ax, [(qx, 2.95), (4.25, 2.95), (4.25, 2.05), (right, 2.05)], color=ACCENT, lw=1.2)
arrow(ax, [(qx, 1.95), (4.45, 1.95), (4.45, 1.35), (right, 1.35)], color=ACCENT, lw=1.2)
arrow(ax, [(qx, 0.95), (4.05, 0.95), (4.05, 1.12), (right, 1.12)], color=RULE, lw=1.2, ls=(0, (4, 3)))
# legend
ax.plot([4.95, 5.35], [0.42, 0.42], color=ACCENT, lw=1.2)
ax.text(5.42, 0.42, 'feasible today', fontsize=8.8, va='center', color=INK)
ax.plot([6.3, 6.7], [0.42, 0.42], color=RULE, lw=1.2, ls=(0, (4, 3)))
ax.text(6.77, 0.42, 'not yet', fontsize=8.8, va='center', color=INK)
fig.savefig(OUT + 'fig4_architecture.png')
plt.close(fig)

# ---------------- Fig. latency ----------------
import numpy as np  # noqa: E402

rows = [('Robot control loop (10–1,000 Hz)', 1e-3, 1e-1, 0),
        ('Robot planning and re-planning (0.1–10 Hz)', 1e-1, 10, 0),
        ('Quantum annealer anneal time (tens of µs)', 1e-5, 1e-4, 2),
        ('Cloud QPU queueing (under 1 min to days)', 30, 3 * 86400, 1),
        ('Variational training on a cloud QPU (indicative)', 3600, 30 * 86400, 1)]
labels = ['Robot requirement', 'End-to-end quantum access', 'Quantum hardware operation']
cols = [COLORS[0], COLORS[1], COLORS[2]]
fig, ax = plt.subplots(figsize=(7.4, 2.9))
for i, (name, a, b, c) in enumerate(rows):
    ax.barh(len(rows) - 1 - i, np.log10(b) - np.log10(a), left=np.log10(a), height=0.5, color=cols[c], zorder=3)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1], color=INK)
ticks = [1e-5, 1e-3, 1, 60, 3600, 86400, 30 * 86400]
ax.set_xticks(np.log10(ticks))
ax.set_xticklabels(['10 µs', '1 ms', '1 s', '1 min', '1 h', '1 day', '1 month'])
ax.set_xlim(-5.3, np.log10(30 * 86400) + 0.3)
ax.xaxis.grid(True, color=GRID, lw=0.8)
ax.set_xlabel('Time (log scale)', color=MUTED)
style_axes(ax)
ax.tick_params(axis='y', length=0)
handles = [plt.Rectangle((0, 0), 1, 1, color=cols[k]) for k in (0, 2, 1)]
ax.legend(handles, [labels[k] for k in (0, 2, 1)], loc='upper center', bbox_to_anchor=(0.45, -0.22), ncol=3,
          fontsize=9, handlelength=1.0)
fig.savefig(OUT + 'fig5_latency.png')
plt.close(fig)
print('schematics written')
