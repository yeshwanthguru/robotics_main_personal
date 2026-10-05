"""Draws every figure of Survey 3 at its printed size (IEEEtran: one column 3.5 in, two columns 7.16 in).
Run from github/s after tools/make_data_package.py and the routing simulation:
    python3 tools/make_figures.py
Inputs: tools/data/package_counts.json, Survey3_data_package/extraction_table.csv,
        tools/data/routing_results.json (written by Survey3_TNNLS_Supplementary_routing_sim.py)."""
import csv, json, os
from collections import Counter
import numpy as np
from figstyle import *
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(HERE) + '/'
FIG = S + 'Survey3_TNNLS_LaTeX_Overleaf/figures/'
os.makedirs(FIG, exist_ok=True)
CNT = json.load(open(HERE + '/data/package_counts.json'))
EXT = list(csv.DictReader(open(S + 'Survey3_data_package/extraction_table.csv', encoding='utf-8-sig')))
SIM = json.load(open(HERE + '/data/routing_results.json'))
LEVELS = ['E2', 'E3', 'E4', 'E5', 'R', 'S']
LCOL = {'E2': '#dde7f0', 'E3': '#9fbad3', 'E4': '#5a86ad', 'E5': '#2c5d8a', 'R': '#e6e6e6', 'S': '#bdbdbd'}
LNAME = {'E2': 'E2 algorithmic', 'E3': 'E3 simulation', 'E4': 'E4 real robot (lab)', 'E5': 'E5 real robot (extensive)',
         'R': 'Review', 'S': 'Software or dataset'}


def save(fig, name):
    fig.savefig(FIG + name, dpi=DPI, bbox_inches='tight', pad_inches=0.02)
    plt.close(fig); print('wrote', name)


# ---------------------------------------------------------------- Fig. 1 architecture
def fig_architecture():
    fig, ax = canvas(2.75)
    mods = [('M1 Vision perception', 'epistemic uncertainty'), ('M2 Reinforcement learning', 'policy variance'),
            ('M3 Imitation learning', 'behavioral fidelity'), ('M4 Fault adaptation', 'recovery-success rate')]
    y0, h, gap = 0.80, 0.135, 0.035
    for i, (m, s) in enumerate(mods):
        y = y0 - i * (h + gap)
        box(ax, 0.01, y, 0.20, h, m + '\n' + 'signal: ' + s, fs=7.2)
        box(ax, 0.26, y + 0.02, 0.12, h - 0.04, 'calibration\nmap $g_%d$' % (i + 1), fc=PALE, fs=7)
        arrow(ax, 0.21, y + h / 2, 0.26, y + h / 2)
        arrow(ax, 0.38, y + h / 2, 0.43, 0.555)
    # optional fifth signal (companion model)
    box(ax, 0.01, 0.04, 0.20, 0.10, 'Human model (companion paper)\nsignal: response uncertainty', fs=6.6, ls='--', ec=MID)
    ax.plot([0.21, 0.405, 0.405], [0.09, 0.09, 0.46], ls='--', color=MID, lw=0.7)
    arrow(ax, 0.405, 0.46, 0.43, 0.46, ls='--', color=MID)
    box(ax, 0.43, 0.43, 0.15, 0.25, 'calibrated\nconfidences $c_t$\n+ context $x_t$\n+ budget $b_t$', fc=BLUE_PALE, fs=7.2)
    box(ax, 0.63, 0.43, 0.17, 0.25, r'orchestrator $\pi_\theta$' + '\n(meta-learned gate)\nchooses $S_t$ to\nmaximize $c-\\lambda\\,$cost', fs=7.2, lw=1.0)
    arrow(ax, 0.58, 0.555, 0.63, 0.555)
    box(ax, 0.85, 0.43, 0.14, 0.25, 'selected\nmodality runs\non the robot', fs=7.2)
    arrow(ax, 0.80, 0.555, 0.85, 0.555)
    box(ax, 0.63, 0.80, 0.17, 0.12, 'safety shield:\nfixed fallback (stop, ask)', fc=PALE, fs=6.8)
    arrow(ax, 0.715, 0.80, 0.715, 0.68)
    box(ax, 0.43, 0.06, 0.56, 0.22, '', fc='white')
    ax.text(0.71, 0.235, 'background learning between episodes (on the robot or a local computer)', ha='center', fontsize=7.2, style='italic')
    for j, t in enumerate(['replay buffer\n$(x_t, c_t, S_t, r_t)$', 'recalibrate\n$g_1,\\ldots,g_K$', 'LoRA / adapter\nupdate of $\\pi_\\theta$',
                           'meta-learned prior\nand dual step on $\\lambda$']):
        box(ax, 0.445 + j * 0.137, 0.08, 0.125, 0.12, t, fc=PALE, fs=6.6)
    arrow(ax, 0.92, 0.43, 0.92, 0.28)
    ax.text(0.925, 0.355, 'outcome $r_t$', fontsize=6.8, ha='left', va='center')
    arrow(ax, 0.62, 0.28, 0.68, 0.43, color=BLUE)
    save(fig, 'Fig1_architecture.png')


# ---------------------------------------------------------------- Fig. 2 PRISMA flow
def fig_prisma():
    fig, ax = canvas(3.45, COLWIDTH)
    st = CNT
    def b(x, y, w, h, t, **k): box(ax, x, y, w, h, t, fs=6.6, **k)
    for y, lab in [(0.79, 'Identification'), (0.47, 'Screening'), (0.10, 'Included')]:
        ax.text(0.015, y, lab, rotation=90, ha='center', va='center', fontsize=7, weight='bold')
    b(0.05, 0.84, 0.29, 0.13, 'Stage 1: initial\nreading list\n(n = 108)')
    b(0.36, 0.84, 0.30, 0.13, 'Stage 2: structured\nsearches, Sep. 2026\n(hit counts not logged)')
    b(0.68, 0.84, 0.31, 0.13, 'Stage 3: targeted\nsearch, 4 Oct. 2026\n(7 new records)')
    b(0.05, 0.60, 0.61, 0.15, 'Records checked against arXiv or publisher pages;\n30 bibliographic details corrected\n(n = 108 + 72 = 180 eligible)')
    arrow(ax, 0.195, 0.84, 0.195, 0.75); arrow(ax, 0.51, 0.84, 0.51, 0.75)
    b(0.68, 0.60, 0.31, 0.15, 'Excluded: 3\n(talk page; not\nembodied; LLM only)', fc=PALE)
    b(0.68, 0.38, 0.31, 0.15, 'Candidates awaiting\nfull-text screening: 4', fc=PALE)
    arrow(ax, 0.835, 0.84, 0.835, 0.75); arrow(ax, 0.835, 0.60, 0.835, 0.53)
    b(0.05, 0.38, 0.61, 0.15, 'Title, abstract and record screened against\nI1–I3 and X1–X5; one structured write-up per work\n(full text 13, abstract 162, standard reference 5)')
    arrow(ax, 0.355, 0.60, 0.355, 0.53)
    lv = st['levels']
    b(0.05, 0.06, 0.94, 0.21, 'Included in the synthesis: n = %d\nE2 %d, E3 %d, E4 %d, E5 %d, E6 0; reviews %d; software or datasets %d\n'
      'Quality appraisal (Q1–Q7): %d primary studies at E2–E5\nEdge class and confidence-signal class coded for all non-review works'
      % (st['n'], lv['E2'], lv['E3'], lv['E4'], lv['E5'], lv['R'], lv['S'], st['n_appraised']), fc=BLUE_PALE)
    arrow(ax, 0.355, 0.38, 0.355, 0.30)
    save(fig, 'Fig2_prisma.png')


# ---------------------------------------------------------------- Fig. 3 evidence by topic
TOPICS = ['LLM planners and orchestrators', 'VLA and robot foundation models', 'Perception and epistemic uncertainty',
          'Reinforcement learning and policy variance', 'Imitation learning and behavioral fidelity',
          'Fault detection, adaptation and recovery', 'Meta-learning', 'Uncertainty fusion and calibration',
          'On-device adaptation and continual learning', 'Adaptive computation, mixture of experts and routing',
          'Platforms, benchmarks and evaluation', 'Safe learning']


def fig_evidence():
    fig, ax = plt.subplots(figsize=(TEXTWIDTH, 2.55))
    data = CNT['by_topic_level']
    y = np.arange(len(TOPICS))[::-1]
    left = np.zeros(len(TOPICS))
    for L in LEVELS:
        v = np.array([data[t].get(L, 0) for t in TOPICS])
        ax.barh(y, v, left=left, color=LCOL[L], edgecolor=INK, lw=0.4, height=0.68, label=LNAME[L])
        for yi, li, vi in zip(y, left, v):
            if vi >= 2: ax.text(li + vi / 2, yi, str(vi), ha='center', va='center', fontsize=6.6,
                                color='white' if L in ('E4', 'E5') else INK)
        left += v
    for yi, tot in zip(y, left): ax.text(tot + 0.3, yi, 'n = %d' % tot, va='center', fontsize=6.8)
    ax.set_yticks(y); ax.set_yticklabels(TOPICS, fontsize=7.4)
    ax.set_xlabel('Number of works'); ax.set_xlim(0, 27)
    ax.legend(ncol=6, fontsize=6.8, frameon=False, loc='lower center', bbox_to_anchor=(0.38, 1.0), handlelength=1.2, columnspacing=1.0)
    ax.tick_params(axis='y', length=0)
    save(fig, 'Fig3_evidence.png')


# ---------------------------------------------------------------- Fig. 4 edge class and signal class by level
def fig_edge_signal():
    fig, axs = plt.subplots(1, 2, figsize=(TEXTWIDTH, 1.85), gridspec_kw=dict(wspace=0.75))
    lv = ['E2', 'E3', 'E4', 'E5']
    edge = ['Pi-class or embedded CPU', 'Embedded GPU', 'Workstation GPU', 'Datacenter or cloud', 'Not stated']
    sig = ['Conformal or calibrated', 'Epistemic uncertainty', 'Failure, anomaly or novelty score', 'Policy variance or entropy',
           'Routing score or predicted quality', 'None']
    for ax, col, cats, title in [(axs[0], 'Edge class', edge, '(a) Inference platform as published'),
                                 (axs[1], 'Confidence signal class', sig, '(b) Confidence signal provided or used')]:
        M = np.array([[sum(1 for r in EXT if r['Evidence level'] == L and r[col] == c) for L in lv] for c in cats])
        ax.imshow(M, cmap='Blues', vmin=0, vmax=max(M.max(), 1) * 1.6, aspect='auto')
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                ax.text(j, i, str(M[i, j]) if M[i, j] else '–', ha='center', va='center', fontsize=7,
                        color='white' if M[i, j] > M.max() * 0.75 else INK)
        ax.set_xticks(range(len(lv))); ax.set_xticklabels(lv); ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats, fontsize=7)
        ax.set_title(title, fontsize=7.6, loc='left')
        for s in ax.spines.values(): s.set_visible(False)
        ax.tick_params(length=0)
        ax.set_xticks(np.arange(-0.5, len(lv)), minor=True); ax.set_yticks(np.arange(-0.5, len(cats)), minor=True)
        ax.grid(which='minor', color='white', lw=1.2); ax.tick_params(which='minor', length=0)
    save(fig, 'Fig4_edge_signal.png')


# ---------------------------------------------------------------- Fig. 5 model size
def fig_size():
    fig, ax = plt.subplots(figsize=(COLWIDTH, 1.75))
    items = [('ACT (LeRobot paper)', 52e6), ('SmolVLA', 450e6), ('OpenVLA', 7e9), ('RT-2-X', 55e9), ('PaLM-E', 562e9)]
    lab = ['52M', '450M', '7B', '55B', '562B']
    y = np.arange(len(items))
    ax.barh(y, [v for _, v in items], color=[BLUE_PALE, BLUE_PALE, '#9fbad3', LIGHT, LIGHT], edgecolor=INK, lw=0.5, height=0.6)
    for yi, (n, v), l in zip(y, items, lab): ax.text(v * 1.25, yi, l, va='center', fontsize=7)
    ax.set_xscale('log'); ax.set_xlim(1e7, 8e12)
    ax.set_yticks(y); ax.set_yticklabels([n for n, _ in items], fontsize=7.2)
    ax.axvline(2e9, color=RUST, lw=0.9, ls='--')
    ax.text(2.6e9, 0.5, '4 GB (Raspberry Pi 5) holds the\n16-bit weights of 2B parameters', color=RUST, fontsize=6.4, va='center')
    ax.set_xlabel('Parameters (log scale)'); ax.tick_params(axis='y', length=0)
    save(fig, 'Fig5_model_size.png')


# ---------------------------------------------------------------- Fig. 6 routing simulation
def fig_sim():
    fig, axs = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.05), gridspec_kw=dict(wspace=0.32))
    ax = axs[0]
    for kind, c, m, lab in [('calibrated', BLUE, 'o', 'Gate, calibrated'), ('overconfident', RUST, 's', 'Gate, miscalibrated')]:
        sw = np.array(SIM['sweep'][kind])
        ax.plot(sw[:, 2], sw[:, 1], color=c, marker=m, ms=3.2, lw=0.9, label=lab)
    rc = SIM['Gate on recalibrated confidence']; ax.plot(rc['cost'], rc['success'], marker='^', color=GREEN, ms=5, ls='none', label='Gate, recalibrated')
    for name, mk in [('Fixed single modality', 'x'), ('Random modality', '+')]:
        ax.plot(SIM[name]['cost'], SIM[name]['success'], marker=mk, color=MID, ms=5, ls='none', label=name)
    ax.axhline(SIM['Oracle (true success prob.)']['success'], color=INK, lw=0.6, ls=':')
    ax.text(2.0, 0.858, 'oracle', fontsize=6.6)
    ax.set_xlabel('Mean compute cost per step'); ax.set_ylabel('Success rate'); ax.set_ylim(0.44, 0.9); ax.set_xlim(0.9, 2.65)
    ax.legend(fontsize=6.3, frameon=False, loc='upper left', bbox_to_anchor=(0.0, 0.92)); ax.set_title('(a) Cost penalty sweep', fontsize=7.6, loc='left')
    ax = axs[1]
    cur = SIM['meta']['curves']
    sty = {'Raw confidence (no recalibration)': (MID, '--'), 'Online recalibration from scratch': (RUST, '-'),
           'Meta-learned prior + online update': (BLUE, '-')}
    for n, v in cur.items():
        v = np.array(v); k = 15; sm = np.convolve(v, np.ones(k) / k, mode='valid')
        ax.plot(np.arange(len(sm)) + k, sm, color=sty[n][0], ls=sty[n][1], lw=1.0, label=n)
    ax.axhline(SIM['meta']['oracle'], color=INK, lw=0.6, ls=':'); ax.text(240, SIM['meta']['oracle'] + 0.004, 'oracle', fontsize=6.6)
    ax.set_xlabel('Steps on a new task'); ax.set_ylabel('Success rate (15-step mean)'); ax.set_ylim(0.72, 0.87)
    ax.legend(fontsize=6.3, frameon=False, loc='lower right'); ax.set_title('(b) Adapting to a new task', fontsize=7.6, loc='left')
    save(fig, 'Fig6_routing_sim.png')


if __name__ == '__main__':
    fig_architecture(); fig_prisma(); fig_evidence(); fig_edge_signal(); fig_size(); fig_sim()
