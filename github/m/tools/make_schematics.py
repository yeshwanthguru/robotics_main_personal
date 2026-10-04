"""Draws the conceptual and worked-example figures of Survey 2 (Figures 1-6, 8 and 9) in a plain journal
style; Figure 7 and Figure S1 are drawn by make_figures.py. Each figure is drawn at the width at which
main.tex includes it, so the 7.5-9 pt labels print at their nominal size.

Numerical content comes from Online Resource 2 (Survey2_AIR_Online_Resource_2_code.py); Figure 9 reads
the 30-seed runs saved in Survey2_data_package/figure_data/rl_experiment_steps.npz (created with the
rl_experiment() function of Online Resource 2; the summary values are those of Table C1).

Run from github/m:  python3 tools/make_schematics.py
"""
import importlib.util
import os

import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, Polygon

from figstyle import (BLUE, BLUE_PALE, INK, LIGHT, MID, PALE, RUST, TEXTWIDTH, arrow, box, canvas, plt)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIG = os.path.join(ROOT, 'Survey2_AIR_LaTeX_Overleaf', 'figures')
spec = importlib.util.spec_from_file_location('or2', os.path.join(ROOT, 'Survey2_AIR_Online_Resource_2_code.py'))
OR2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OR2)


def save(fig, name):
    fig.savefig(os.path.join(FIG, name), facecolor='white')
    plt.close(fig)


# ----------------------------------------------------------------------------- Figure 1: eras
def fig1_eras():
    eras = [
        ('1925–2000', 'Era 1  Classical foundations and early quantum ideas',
         ['von Neumann (1932): Hilbert-space formalism', 'Savage (1954): sure-thing principle',
          'Tversky and Kahneman (1974, 1983): heuristics, conjunction fallacy',
          'Shafir and Tversky (1992): disjunction effect']),
        ('2000–2010', 'Era 2  Quantum probability enters cognitive science',
         ['Khrennikov (1999, 2010): quantum-like information spaces', 'Aerts et al. (2000, 2009): quantum structure in concepts',
          'Busemeyer et al. (2006): quantum dynamics of decision', 'Pothos and Busemeyer (2009): sure-thing violations']),
        ('2011–2015', 'Era 3  The Busemeyer–Bruza framework',
         ['Busemeyer and Bruza (2012): the textbook framework', 'Busemeyer et al. (2011): conjunction and disjunction errors',
          'Pothos and Busemeyer (2013): BBS target article', 'Wang et al. (2014): QQ equality in 70 surveys']),
        ('2016–2020', 'Era 4  First robotics and AI connections',
         ['Moreira and Wichert (2016): quantum-like Bayesian networks', 'Li et al. (2019): quantum-inspired neural matching',
          'Lanza et al. (2020): quantum-like robot perception', 'Lawless (2020): quantum-like human–machine teams']),
        ('2021–2026', 'Era 5  Autonomous systems, HRI and LLMs',
         ['Song et al. (2022): quantum cognition in autonomous driving', 'Roeder et al. (2023): quantum model of trust in AI',
          'Widdows et al. (2023): cognitive models as quantum circuits', 'Lo et al. (2025): quantum-like contextuality in LLMs']),
    ]
    fig, ax = canvas(4.15, TEXTWIDTH)
    n = len(eras)
    top, bottom = 0.985, 0.015
    h = (top - bottom) / n
    xline = 0.165
    ax.plot([xline, xline], [bottom + 0.02, top - 0.02], color=INK, lw=0.8)
    for i, (years, title, items) in enumerate(eras):
        y0 = top - (i + 1) * h
        if i % 2 == 0:
            ax.add_patch(plt.Rectangle((0, y0), 1, h, fc=PALE, ec='none'))
        yc = y0 + h * 0.62
        ax.text(xline - 0.025, yc, years, ha='right', va='center', fontsize=8.5, weight='bold')
        ax.plot([xline], [yc], marker='s', ms=4.2, mfc='white', mec=INK, mew=0.8)
        ax.text(xline + 0.03, y0 + h * 0.83, title, ha='left', va='center', fontsize=8.5, weight='bold')
        for j, it in enumerate(items):
            ax.text(xline + 0.045, y0 + h * (0.64 - 0.155 * j), '– ' + it, ha='left', va='center', fontsize=7.6)
    save(fig, 'Fig1_eras.png')


# ----------------------------------------------------------------------------- Figure 2: order geometry
def fig2_order():
    tpsi, tA, tB = np.deg2rad(20), np.deg2rad(0), np.deg2rad(55)   # Example 1 of Online Resource 2
    p = OR2.order_effect()
    u = lambda t: np.array([np.cos(t), np.sin(t)])
    psi, a, b = u(tpsi), u(tA), u(tB)
    w = 0.62 * TEXTWIDTH
    fig = plt.figure(figsize=(w, w * 0.92))
    ax = fig.add_axes([0.02, 0.17, 0.96, 0.81]); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=MID, lw=0.5, ls=(0, (1, 2))))
    for t, lab, off in [(tA, r'$A = \mathrm{yes}$', (0.04, -0.09)), (tB, r'$B = \mathrm{yes}$', (-0.05, 0.05))]:
        d = u(t)
        ax.plot([-1.1 * d[0], 1.12 * d[0]], [-1.1 * d[1], 1.12 * d[1]], color=INK, lw=0.6)
        ax.text(1.12 * d[0] + off[0], 1.12 * d[1] + off[1], lab, fontsize=8.5, ha='left' if t == tA else 'center')
    ax.annotate('', xy=psi, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', lw=1.2, color=INK, mutation_scale=9))
    ax.text(psi[0] + 0.04, psi[1] + 0.04, r'$|\psi\rangle$', fontsize=10)
    # A then B (solid)
    pa = (psi @ a) * a; pab = (pa @ b) * b
    ax.plot([psi[0], pa[0]], [psi[1], pa[1]], color=BLUE, lw=0.9)
    ax.plot([pa[0], pab[0]], [pa[1], pab[1]], color=BLUE, lw=0.9)
    # B then A (dashed)
    pb = (psi @ b) * b; pba = (pb @ a) * a
    ax.plot([psi[0], pb[0]], [psi[1], pb[1]], color=RUST, lw=0.9, ls=(0, (4, 2)))
    ax.plot([pb[0], pba[0]], [pb[1], pba[1]], color=RUST, lw=0.9, ls=(0, (4, 2)))
    for q, c in [(pa, BLUE), (pab, BLUE), (pb, RUST), (pba, RUST)]:
        ax.plot(*q, marker='o', ms=3, color=c)
    ax.set_xlim(-1.15, 1.45); ax.set_ylim(-1.15, 1.25)
    ax2 = fig.add_axes([0, 0, 1, 0.16]); ax2.axis('off'); ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
    ax2.plot([0.08, 0.17], [0.72, 0.72], color=BLUE, lw=0.9)
    ax2.text(0.19, 0.72, r'$A$ then $B$:  $\|P_B P_A \psi\|^2 = %.2f$' % p['AyBy'], va='center', fontsize=8)
    ax2.plot([0.08, 0.17], [0.32, 0.32], color=RUST, lw=0.9, ls=(0, (4, 2)))
    ax2.text(0.19, 0.32, r'$B$ then $A$:  $\|P_A P_B \psi\|^2 = %.2f$' % p['ByAy'], va='center', fontsize=8)
    save(fig, 'Fig2_order_geometry.png')


# ----------------------------------------------------------------------------- Figure 3: Bloch sphere
def fig3_bloch():
    w = 0.55 * TEXTWIDTH
    fig = plt.figure(figsize=(w, w * 0.95))
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0]); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=INK, lw=0.7))
    ax.add_patch(Arc((0, 0), 2, 0.55, theta1=180, theta2=360, ec=INK, lw=0.6))
    ax.add_patch(Arc((0, 0), 2, 0.55, theta1=0, theta2=180, ec=MID, lw=0.5, ls=(0, (2, 2))))
    # A basis (z axis) and B basis (x axis, drawn in projection)
    ax.plot([0, 0], [-1, 1], color=INK, lw=0.6)
    ax.plot([-1, 1], [0, 0], color=INK, lw=0.6)
    for (x, y), lab, ha, va in [((0, 1.05), r'$|0\rangle$  (yes to $A$)', 'center', 'bottom'),
                                ((0, -1.05), r'$|1\rangle$  (no to $A$)', 'center', 'top'),
                                ((1.05, 0), r'$|{+}\rangle$', 'left', 'center'),
                                ((-1.05, 0), r'$|{-}\rangle$', 'right', 'center')]:
        ax.text(x, y, lab, ha=ha, va=va, fontsize=8.5)
    ax.text(1.05, -0.13, '(yes to $B$)', ha='left', va='center', fontsize=7.5)
    th = np.deg2rad(50)   # polar angle of the illustrated state
    s = np.array([np.sin(th) * 0.92, np.cos(th)])
    ax.annotate('', xy=s, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', lw=1.2, color=BLUE, mutation_scale=9))
    ax.text(s[0] + 0.05, s[1] + 0.03, r'$|\psi\rangle$', fontsize=10, color=BLUE)
    ax.plot([s[0], s[0]], [s[1], 0], color=MID, lw=0.5, ls=(0, (2, 2)))
    ax.plot([0, s[0]], [s[1], s[1]], color=MID, lw=0.5, ls=(0, (2, 2)))
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=90 - np.degrees(th) * 0.95, theta2=90, ec=INK, lw=0.6))
    ax.text(0.09, 0.3, r'$\theta$', fontsize=9)
    ax.text(0, -1.42, r'$p(\mathrm{yes\ to\ }A) = \cos^2(\theta/2)$', ha='center', fontsize=8.5)
    ax.set_xlim(-1.55, 1.75); ax.set_ylim(-1.55, 1.35)
    save(fig, 'Fig3_bloch.png')


# ----------------------------------------------------------------------------- Figure 4: interference
def fig4_interference():
    r = OR2.interference()
    vals = [0.97, 0.84, r['observed'], r['classical']]
    labels = ['Opponent\nknown to\ndefect', 'Opponent\nknown to\ncooperate', 'Opponent\nunknown\n(observed)',
              'Classical\nprediction (total\nprobability)']
    w = 0.75 * TEXTWIDTH
    fig, ax = plt.subplots(figsize=(w, w * 0.56))
    fig.subplots_adjust(left=0.12, right=0.86, bottom=0.25, top=0.96)
    ax.axhspan(0.84, 0.97, color=PALE, zorder=0)
    ax.text(3.42, 0.905, 'classically\nadmissible\nrange', fontsize=7, va='center', ha='left', color=MID, clip_on=False)
    styles = [dict(fc=LIGHT, ec=INK), dict(fc=LIGHT, ec=INK), dict(fc=BLUE, ec=INK), dict(fc='white', ec=INK, hatch='////')]
    for i, (v, st) in enumerate(zip(vals, styles)):
        ax.bar(i, v, width=0.58, lw=0.6, zorder=2, **st)
        ax.text(i, v + 0.015, f'{v:.3g}' if i < 3 else f'{v:.3f}', ha='center', va='bottom', fontsize=7.8)
    ax.text(2, 0.30, 'interfer-\nence\n$%.3f$\n($\\theta \\approx %d^\\circ$)' % (r['interference'], round(r['theta_deg'])),
            ha='center', va='center', fontsize=7.0, color='white', zorder=3)
    ax.set_xticks(range(4)); ax.set_xticklabels(labels, fontsize=7.2)
    ax.set_ylim(0, 1.05); ax.set_xlim(-0.5, 3.4)
    ax.set_ylabel('$p$(player defects)')
    ax.tick_params(axis='x', length=0)
    save(fig, 'Fig4_interference.png')


# ----------------------------------------------------------------------------- Figure 5: framework
def fig5_framework():
    rows = [('Superposition\n(indefinite state)', 'Ambiguity, constructed\npreference', 'Perception and belief\n(§6.1, §11)'),
            ('Non-commuting\nprojectors', 'Question-order and\ncontext effects', 'Sequential queries, HRI,\nLLM prompts (§6, §9.3)'),
            ('Interference\n(complex amplitudes)', 'Sure-thing violations,\ndisjunction effect', 'Decision under uncertainty,\nfusion (§6.3, §7.3)'),
            ('Incompatible\ntensor structure', 'Conjunction fallacy,\nconcept combination', 'Classification, semantics\n(§8, §9)'),
            ('Unitary and open-system\n(Lindblad) dynamics', 'Oscillating preference,\ntrust evolution', 'RL, planning, trust-aware\nautonomy (§7, §10, §19)')]
    fig, ax = canvas(3.25)
    xs, w = [0.01, 0.355, 0.70], 0.29
    heads = ['QP principle', 'Cognitive phenomenon', 'Agent or AI function']
    for x, hd in zip(xs, heads):
        ax.text(x + w / 2, 0.955, hd, ha='center', va='center', fontsize=8, weight='bold')
    ax.plot([0.01, 0.99], [0.915, 0.915], color=INK, lw=0.6)
    bh, gap, y = 0.135, 0.04, 0.765
    for r in rows:
        for x, txt, fc in zip(xs, r, [PALE, 'white', BLUE_PALE]):
            box(ax, x, y, w, bh, txt, fc=fc, fs=7.4)
        arrow(ax, xs[0] + w + 0.008, y + bh / 2, xs[1] - 0.008, y + bh / 2)
        arrow(ax, xs[1] + w + 0.008, y + bh / 2, xs[2] - 0.008, y + bh / 2)
        y -= bh + gap
    save(fig, 'Fig5_framework.png')


# ----------------------------------------------------------------------------- Figure 6: architecture
def fig6_architecture():
    fig, ax = canvas(2.6)
    box(ax, 0.01, 0.40, 0.15, 0.17, 'Sensors and\nhuman input', fc=PALE, fs=7.4)
    box(ax, 0.22, 0.58, 0.20, 0.17, 'Classical perception\n(DL, filtering)', fs=7.4)
    box(ax, 0.22, 0.20, 0.20, 0.17, 'Context encoder\n(task, order,\nhistory)', fs=7.4)
    box(ax, 0.48, 0.33, 0.22, 0.31, 'Quantum-like\ndecision module\n' + r'state $|\psi\rangle$ or $\rho$;' + '\nprojectors or\ninstruments',
        fc=BLUE_PALE, lw=1.0, fs=7.4)
    box(ax, 0.77, 0.58, 0.22, 0.17, 'Action selection\n(classical planner\nor RL)', fs=7.4)
    box(ax, 0.77, 0.20, 0.22, 0.17, 'Explanation and\nescalation to\na human', fs=7.4)
    arrow(ax, 0.16, 0.50, 0.22, 0.64); arrow(ax, 0.16, 0.47, 0.22, 0.30)
    arrow(ax, 0.42, 0.665, 0.48, 0.58); arrow(ax, 0.42, 0.285, 0.48, 0.39)
    arrow(ax, 0.70, 0.58, 0.77, 0.665); arrow(ax, 0.70, 0.39, 0.77, 0.285)
    ax.annotate('', xy=(0.88, 0.58), xytext=(0.88, 0.37), arrowprops=dict(arrowstyle='<|-|>', lw=0.7, color=INK, mutation_scale=6))
    arrow(ax, 0.88, 0.75, 0.085, 0.57, ls=(0, (3, 2)), rad=0.33, color=MID)
    ax.text(0.48, 0.955, 'feedback from the environment and the human updates the state (open-system dynamics)',
            ha='center', va='center', fontsize=7.2, style='italic', color=MID)
    ax.text(0.5, 0.07, 'Runs on classical hardware; a quantum-circuit back end is optional (Widdows et al. 2023).',
            ha='center', va='center', fontsize=7.2)
    save(fig, 'Fig6_architecture.png')


# ----------------------------------------------------------------------------- Figure 8: decision guide
def fig8_guide():
    w = 0.95 * TEXTWIDTH
    fig, ax = canvas(2.95, w)

    def diamond(xc, yc, dx, dy, text):
        ax.add_patch(Polygon([(xc, yc + dy), (xc + dx, yc), (xc, yc - dy), (xc - dx, yc)], closed=True, fc=PALE, ec=INK, lw=0.7))
        ax.text(xc, yc, text, ha='center', va='center', fontsize=7.0, linespacing=1.1)

    diamond(0.27, 0.83, 0.25, 0.135, 'Does the target\nbehaviour show order,\ncontext or interference\neffects?')
    box(ax, 0.62, 0.765, 0.36, 0.13, 'Classical probability (Bayes nets,\nKalman filter, POMDP, deep RL)', fs=7.0)
    arrow(ax, 0.52, 0.83, 0.62, 0.83); ax.text(0.56, 0.85, 'no', ha='center', va='bottom', fontsize=7.6, style='italic')
    diamond(0.27, 0.47, 0.25, 0.135, 'Are the effects replicable,\nand is the goal to\npredict or align\nwith humans?')
    arrow(ax, 0.27, 0.695, 0.27, 0.605); ax.text(0.285, 0.65, 'yes', ha='left', va='center', fontsize=7.6, style='italic')
    box(ax, 0.62, 0.405, 0.36, 0.13, 'Effects weak or not replicable:\nclassical noise models (PT+N)\nmay suffice', fs=7.0)
    arrow(ax, 0.52, 0.47, 0.62, 0.47); ax.text(0.56, 0.49, 'no', ha='center', va='bottom', fontsize=7.6, style='italic')
    box(ax, 0.02, 0.13, 0.44, 0.13, 'Predict or align with humans: quantum-like\nmodel (QLBN, QP trust model)', fc=BLUE_PALE, fs=7.0)
    box(ax, 0.54, 0.13, 0.44, 0.13, 'Maximise task reward only:\ntest against classical baselines first', fs=7.0)
    arrow(ax, 0.235, 0.355, 0.235, 0.26); arrow(ax, 0.33, 0.365, 0.66, 0.26)
    ax.text(0.22, 0.305, 'yes', ha='right', va='center', fontsize=7.6, style='italic')
    ax.text(0.53, 0.335, 'yes, but reward only', ha='left', va='bottom', fontsize=7.6, style='italic')
    ax.text(0.5, 0.045, 'Hybrid rule: keep a classical core and add a quantum-like module only where human-facing\n'
            'judgements are sequential, ambiguous or context-dependent (Section 14.4).', ha='center', va='center', fontsize=7.0)
    save(fig, 'Fig8_decision_guide.png')


# ----------------------------------------------------------------------------- Figure 9: RL experiment
def fig9_rl():
    d = np.load(os.path.join(ROOT, 'Survey2_data_package', 'figure_data', 'rl_experiment_steps.npz'))
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, TEXTWIDTH * 0.43), sharey=True)
    fig.subplots_adjust(left=0.12, right=0.985, bottom=0.30, top=0.91, wspace=0.08)
    style = {'eps': (INK, '-', r'$\varepsilon$-greedy Q-learning'), 'softmax': (MID, (0, (4, 2)), 'Softmax Q-learning'),
             'qrl': (BLUE, '-', 'Quantum-inspired RL')}
    for ax, noise, title in zip(axes, ('0.0', '0.5'), ('Deterministic reward', r'Noisy reward ($\sigma = 0.5$)')):
        for kind in ('eps', 'softmax', 'qrl'):
            runs = d[f'{kind}_{noise}']
            ma = np.array([np.convolve(r, np.ones(10) / 10, 'valid') for r in runs])
            x = np.arange(10, runs.shape[1] + 1)
            med, q1, q3 = np.median(ma, 0), np.percentile(ma, 25, 0), np.percentile(ma, 75, 0)
            c, ls, lab = style[kind]
            ax.fill_between(x, q1, q3, color=c, alpha=0.12, lw=0)
            ax.plot(x, med, color=c, ls=ls, lw=1.0, label=lab)
        ax.axhline(10, color=MID, lw=0.5, ls=(0, (1, 2)))
        ax.set_title(title); ax.set_xlabel('Episode'); ax.set_ylim(0, 205); ax.set_xlim(0, 305)
    axes[0].set_ylabel('Steps to goal (median)')
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc='lower center', ncol=3, frameon=False, bbox_to_anchor=(0.55, 0.0), handlelength=2.2, fontsize=7.5)
    save(fig, 'Fig9_rl.png')


if __name__ == '__main__':
    fig1_eras(); fig2_order(); fig3_bloch(); fig4_interference(); fig5_framework(); fig6_architecture(); fig8_guide()
    if os.path.exists(os.path.join(ROOT, 'Survey2_data_package', 'figure_data', 'rl_experiment_steps.npz')):
        fig9_rl()
    print('figures written to', FIG)
