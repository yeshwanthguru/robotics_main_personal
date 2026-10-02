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

# ---------------- Adapted method figures (drawn from the papers' descriptions) ----------------
from figstyle import ACCENT as BLUE  # noqa: E402
SOFT = '#f4f7fb'


def note(ax, x, y, text, size=8.3, ha='center', color=MUTED, style='italic'):
    ax.text(x, y, text, ha=ha, va='center', fontsize=size, color=color, style=style, linespacing=1.2)


# Fig. QUBO fleet-routing pipeline (Ohzeki 2019, Clark 2019, Quang 2025, Leib 2023)
W, H = 7.8, 2.45
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
steps = [('Fleet state', 'robots, tasks,\nmap, time window', ''),
         ('Candidate routes', 'k classical routes\nper robot', 'Ohzeki 2019; Clark 2019'),
         ('QUBO', 'one route per robot\n+ conflict penalties', ''),
         ('Decompose', 'sub-QUBOs that\nfit the device', 'Quang 2025'),
         ('Solve', 'annealer, digital\nannealer, or MIP', 'Leib 2023 compares'),
         ('Check and repair', 'discard infeasible\nsamples; fallback', 'Ohzeki 2019')]
bw, gap, y0, bh = 1.13, 0.17, 1.2, 0.95
xs = [0.1 + i * (bw + gap) for i in range(len(steps))]
for i, ((t, d, src), x) in enumerate(zip(steps, xs)):
    hot = t in ('QUBO', 'Solve')
    box(ax, x, y0, bw, bh, fill=SOFT if hot else 'white', edge=BLUE if hot else RULE)
    ax.text(x + bw / 2, y0 + bh - 0.2, t, ha='center', va='center', fontsize=9.2, weight='bold', color=INK)
    ax.text(x + bw / 2, y0 + 0.36, d, ha='center', va='center', fontsize=8.4, color=INK, linespacing=1.2)
    if src:
        note(ax, x + bw / 2, y0 + bh + 0.13, src, size=8)
    if i:
        arrow(ax, [(xs[i - 1] + bw, y0 + bh / 2), (x, y0 + bh / 2)], lw=0.9)
arrow(ax, [(xs[-1] + bw / 2, y0), (xs[-1] + bw / 2, 0.78), (xs[0] + bw / 2, 0.78), (xs[0] + bw / 2, y0)], lw=0.9)
ax.text((xs[0] + xs[-1] + bw) / 2, 0.66, 'plans dispatched to the robots; the cycle is re-solved every period',
        ha='center', va='top', fontsize=8.5, color=INK)
ax.text(W / 2, 0.2, r'QUBO: $\min_{x}\ \sum_{r,k} c_{rk}\,x_{rk} \;+\; A\sum_{r}(1-\sum_{k}x_{rk})^{2} \;+\; B\sum_{\mathrm{conflicts}} x_{rk}\,x_{r^{\prime}k^{\prime}}$,  $x_{rk}\in\{0,1\}$',
        ha='center', va='center', fontsize=9.2, color=INK)
fig.savefig(OUT + 'fig8_qubo_pipeline.png')
plt.close(fig)

# Fig. Grover-based planning and localization (Chella 2022, Chella 2023, Antero 2025, Lathrop 2023)
W, H = 7.6, 3.3
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
wy = [2.75, 2.35, 1.95]
labels = ['candidate register\n(paths or poses)', '', 'ancilla and\noracle qubit']
for y in wy:
    ax.plot([1.45, 6.75], [y, y], color=RULE, lw=0.9, zorder=1)
ax.text(1.35, 2.55, 'candidate register\n(paths or poses)', ha='right', va='center', fontsize=8.6, color=INK, linespacing=1.2)
ax.text(1.35, 1.95, 'oracle qubit', ha='right', va='center', fontsize=8.6, color=INK)
box(ax, 1.65, 2.2, 0.55, 0.75, r'$H^{\otimes n}$', size=10)
box(ax, 2.55, 1.75, 1.35, 1.2, 'Oracle $U_\\omega$\nmarks valid\ncandidates', fill=SOFT, edge=BLUE, size=9)
box(ax, 4.15, 2.2, 1.15, 0.75, 'Diffusion\n(amplify)', size=9)
ax.add_patch(plt.Rectangle((2.45, 1.62), 2.95, 1.48, fc='none', ec=RULE, lw=0.8, ls=(0, (3, 2))))
ax.text(3.92, 3.18, r'repeat $\approx\frac{\pi}{4}\sqrt{N/S}$ times', ha='center', va='center', fontsize=8.8, color=INK)
box(ax, 5.65, 2.2, 0.6, 0.75, 'Measure', size=9)
ax.text(6.85, 2.55, 'plan\nor pose', ha='left', va='center', fontsize=9, color=INK)
box(ax, 0.3, 0.1, 3.45, 0.98, fill='white', edge=RULE)
ax.text(0.42, 0.9, 'Planning oracle (Chella 2022, 2023)', fontsize=8.8, weight='bold', color=INK, va='center')
ax.text(0.42, 0.45, 'apply reversible move blocks M for each\nstep of the plan, test whether the goal cell is\nreached (T), mark, and uncompute', fontsize=8.4, color=INK, va='center', linespacing=1.2)
box(ax, 3.95, 0.1, 3.35, 0.98, fill='white', edge=RULE)
ax.text(4.07, 0.9, 'Localization oracle (Antero 2025)', fontsize=8.8, weight='bold', color=INK, va='center')
ax.text(4.07, 0.45, 'compare the local sensor pattern with the\ncostmap at each candidate cell and mark the\ncells where it matches', fontsize=8.4, color=INK, va='center', linespacing=1.2)
ax.plot([3.0, 2.0], [1.75, 1.08], color=RULE, lw=0.7, ls=':')
ax.plot([3.45, 5.6], [1.75, 1.08], color=RULE, lw=0.7, ls=':')
fig.savefig(OUT + 'fig9_grover.png')
plt.close(fig)

# Fig. Variational quantum policy loop (Hohenfeld 2024, Sinha 2023, Acuto 2022, Dragan 2025, Sun 2025, Ngo 2026)
W, H = 7.6, 3.95
fig = plt.figure(figsize=(W, H + 0.5))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(-0.5, H); ax.axis('off')
yc = 2.55
box(ax, 0.12, yc - 0.52, 1.3, 1.04, 'Robot and\nenvironment', size=9.5)
box(ax, 1.95, 1.65, 3.25, 1.75, fill=SOFT, edge=BLUE)
ax.text(3.57, 3.22, 'Parameterized quantum circuit', ha='center', va='center', fontsize=9.3, weight='bold', color=INK)
for y in [2.8, 2.55, 2.3]:
    ax.plot([2.25, 4.95], [y, y], color=RULE, lw=0.8, zorder=1)
    ax.text(2.13, y, r'$|0\rangle$', ha='right', va='center', fontsize=8.5, color=INK)
box(ax, 2.35, 2.16, 0.5, 0.78, r'$V(\theta_0)$', size=8.8)
box(ax, 3.05, 2.16, 0.62, 0.78, r'$U_{in}(s)$', size=8.8)
box(ax, 3.72, 2.16, 0.6, 0.78, r'$W(\theta_l)$', size=8.8)
ax.add_patch(plt.Rectangle((2.98, 2.09), 1.42, 0.92, fc='none', ec=RULE, lw=0.8, ls=(0, (3, 2)), zorder=4))
ax.text(3.69, 1.9, r'repeated $L$ times (data re-uploading)', ha='center', va='center', fontsize=8, color=MUTED)
box(ax, 4.5, 2.16, 0.5, 0.78, r'$\langle Z\rangle$', size=8.8)
box(ax, 5.6, yc - 0.52, 1.85, 1.04, 'Scale outputs to\nQ-values or a policy;\nchoose action $a_t$', size=8.8)
arrow(ax, [(1.42, yc), (1.95, yc)], lw=0.9)
ax.text(1.68, yc + 0.14, r'$s_t$', ha='center', fontsize=9, color=INK)
arrow(ax, [(5.2, yc), (5.6, yc)], lw=0.9)
arrow(ax, [(6.52, yc + 0.52), (6.52, 3.68), (0.77, 3.68), (0.77, yc + 0.52)], lw=0.9)
ax.text(3.6, 3.79, r'action $a_t$; reward $r_t$ and next state $s_{t+1}$', ha='center', va='center', fontsize=8.6, color=INK)
box(ax, 2.6, 0.98, 1.95, 0.45, r'Classical optimizer updates $\theta$', size=8.8)
arrow(ax, [(3.57, 1.43), (3.57, 1.65)], color=BLUE, lw=1.0)
arrow(ax, [(6.52, yc - 0.52), (6.52, 1.2), (4.55, 1.2)], lw=0.9)
ax.text(5.55, 1.08, 'loss from rewards', ha='center', va='top', fontsize=8.2, color=MUTED)
rows = [('the circuit is the Q-network', 'Hohenfeld 2024, simulated Turtlebot'),
        ('only the critic is quantum; the deployed policy runs classically', 'Sinha 2023, Nav-Q'),
        ('circuits form both actor and critic', 'Acuto 2022; Drăgan 2025'),
        ('a simulated circuit controls a physical cart-pole', 'Sun 2025'),
        ('the circuit runs on a quantum processor', 'Ngo 2026; Altrabulsi 2026')]
ax.text(0.15, 0.75, 'Where the circuit sits in the studies', fontsize=8.8, weight='bold', color=INK, va='center')
for i, (a, b) in enumerate(rows):
    yy = 0.53 - i * 0.2
    ax.text(0.15, yy, f'\u2022 {a}', fontsize=8.2, color=INK, va='center')
    ax.text(4.55, yy, b, fontsize=8.2, color=MUTED, va='center', style='italic')
fig.savefig(OUT + 'fig10_vqc_policy.png')
plt.close(fig)

# Fig. Quantum-probability order effect (Busemeyer 2012; Pothos 2013; Widdows 2023)
import numpy as np  # noqa: E402,F811
th_psi, th_a, th_b = np.deg2rad(20), np.deg2rad(0), np.deg2rad(55)
u = lambda t: np.array([np.cos(t), np.sin(t)])  # noqa: E731
psi, a, b = u(th_psi), u(th_a), u(th_b)
fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0))
for ax, (first, second, n1, n2) in zip(axes, [(a, b, 'A', 'B'), (b, a, 'B', 'A')]):
    p1 = first * (psi @ first)
    p2 = second * (p1 @ second)
    prob = float(p2 @ p2)
    for v, nm in [(a, 'A'), (b, 'B')]:
        ax.plot([0, 1.15 * v[0]], [0, 1.15 * v[1]], color=RULE, lw=0.9)
        ax.text(1.2 * v[0], 1.2 * v[1], nm, fontsize=10, color=INK, ha='center', va='center')
    ax.annotate('', xy=psi, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=INK, lw=1.2))
    ax.text(psi[0] + 0.04, psi[1] + 0.06, r'$\psi$', fontsize=11, color=INK)
    ax.plot([psi[0], p1[0]], [psi[1], p1[1]], color=MUTED, lw=0.8, ls=':')
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=MUTED, lw=0.8, ls=':')
    ax.annotate('', xy=p2, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.6))
    ax.plot(*p1, 'o', color=MUTED, ms=3.5)
    ax.set_title(f'{n1} then {n2}:  Pr = {prob:.2f}', fontsize=10, color=INK)
    ax.set_xlim(-0.1, 1.3); ax.set_ylim(-0.1, 1.15); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout()
fig.savefig(OUT + 'fig11_order_effect.png')
plt.close(fig)
print('adapted figures written')
