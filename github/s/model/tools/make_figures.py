"""Draws the figures of the model paper from results/*.json (IEEEtran sizes: one column 3.5 in,
two columns 7.16 in). Run from github/s/model after experiments/run_all.py:
    python3 tools/make_figures.py"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, ROOT)
from figstyle import *
from qlmodel.domains import DOMAINS, generator

RES = os.path.join(ROOT, 'results'); FIG = os.path.join(ROOT, 'paper', 'figures')
os.makedirs(FIG, exist_ok=True)
load = lambda n: json.load(open(os.path.join(RES, n)))
DLAB = {d: DOMAINS[d]['label'] for d in DOMAINS}
GCOL = {'QL': BLUE, 'Bayes': MID, 'Anchoring': RUST, 'Mixture': GREEN}


def save(fig, name):
    fig.savefig(os.path.join(FIG, name), dpi=DPI, bbox_inches='tight', pad_inches=0.02); plt.close(fig); print('wrote', name)


def fig_framework():
    fig, ax = canvas(1.9)
    box(ax, 0.01, 0.55, 0.20, 0.38, 'Person\nbelief state $\\psi$\n(order-sensitive)', fc=PALE, fs=7.4)
    box(ax, 0.30, 0.55, 0.22, 0.38, 'Questions asked by\nthe robot (order A, B)\nand robot outcomes', fs=7.4)
    box(ax, 0.61, 0.55, 0.17, 0.38, 'Human model\nQL, Bayes,\nanchoring;\ntrust dynamics', fc=BLUE_PALE, fs=7.4)
    box(ax, 0.84, 0.55, 0.15, 0.38, 'Predicted\nanswers and\ntheir\nuncertainty', fs=7.4)
    arrow(ax, 0.21, 0.74, 0.30, 0.74); arrow(ax, 0.52, 0.74, 0.61, 0.74); arrow(ax, 0.78, 0.74, 0.84, 0.74)
    box(ax, 0.30, 0.05, 0.48, 0.30, 'Uses: choose the question order; correct for order effects;\ndecide when to ask about trust; feed the predictive uncertainty\nto the orchestrator of Survey 3 as a fifth confidence signal', fs=7.2)
    arrow(ax, 0.915, 0.55, 0.78, 0.25, rad=-0.2)
    box(ax, 0.01, 0.05, 0.20, 0.30, 'Execution:\nCPU (analytic),\nquantum circuits\n(simulator, cloud)', fc=PALE, fs=7.0)
    arrow(ax, 0.21, 0.20, 0.30, 0.20, ls='--', color=MID)
    save(fig, 'Fig1_framework.png')


def fig_order_effects():
    fig, axs = plt.subplots(1, 3, figsize=(TEXTWIDTH, 1.75), sharey=True, gridspec_kw=dict(wspace=0.08))
    for ax, d in zip(axs, DOMAINS):
        x = np.arange(4); w = 0.26
        for i, g in enumerate(['QL', 'Anchoring', 'Bayes']):
            r = generator(d, g, sd=0).rates()
            ax.bar(x + (i - 1) * w, r, w, color=GCOL[g], edgecolor=INK, lw=0.4, label=g)
        ax.set_xticks(x); ax.set_xticklabels(['A first', 'B first', 'A second', 'B second'], fontsize=6.6)
        ax.set_title(DLAB[d], fontsize=7.6, loc='left'); ax.set_ylim(0, 1)
    axs[0].set_ylabel("P('yes')")
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, ['QL generator', 'Anchoring generator', 'Bayes generator'], fontsize=6.6, frameon=False, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 0.98))
    save(fig, 'Fig2_order_effects.png')


def fig_recovery():
    r = load('exp1_model_recovery.json'); truth = {'QL': 'QL', 'Bayes': 'Bayes', 'Anchoring': 'Anchoring2'}
    fig, axs = plt.subplots(1, 2, figsize=(TEXTWIDTH, 1.85), sharey=True, gridspec_kw=dict(wspace=0.1))
    for ax, sd in zip(axs, ['sd=0.0', 'sd=0.1']):
        for g, t in truth.items():
            ns = sorted(int(n) for n in r[next(iter(r))][g][sd])
            acc = [np.mean([r[d][g][sd][str(n)]['selected'][t] / r[d][g][sd][str(n)]['reps'] for d in r]) for n in ns]
            ax.plot(ns, acc, marker='o', ms=3, color=GCOL[g], label='%s generator' % g)
        qq = [np.mean([r[d]['Anchoring'][sd][str(n)]['qq_reject'] / r[d]['Anchoring'][sd][str(n)]['reps'] for d in r]) for n in ns]
        ax.plot(ns, qq, ls='--', color=RUST, lw=0.9, label='QQ test rejects (anchoring)')
        ax.set_xscale('log'); ax.set_xticks(ns); ax.set_xticklabels(ns); ax.set_ylim(0, 1.02)
        ax.set_xlabel('People per question order')
        ax.set_title('(a) Homogeneous population' if sd == 'sd=0.0' else '(b) Individual differences (sd 0.1)', fontsize=7.6, loc='left')
    axs[0].set_ylabel('Proportion correct (BIC)'); axs[1].legend(fontsize=6.3, frameon=False, loc='lower right')
    save(fig, 'Fig3_recovery.png')


def fig_cross_order():
    r = load('exp2_cross_order.json'); models = ['QL', 'Bayes', 'Anchoring1', 'Anchoring2']
    mc = {'QL': BLUE, 'Bayes': MID, 'Anchoring1': '#d9a07e', 'Anchoring2': RUST}
    conds = ['sd=0.0|N=400', 'sd=0.0|N=4000', 'sd=0.1|N=400', 'sd=0.1|N=4000']
    fig, axs = plt.subplots(1, 4, figsize=(TEXTWIDTH, 1.9), sharey=True, gridspec_kw=dict(wspace=0.08))
    for ax, cond in zip(axs, conds):
        gens = ['QL', 'Bayes', 'Anchoring', 'Mixture']; x = np.arange(len(gens)); w = 0.2
        for i, m in enumerate(models):
            v = [np.mean([r[d]['%s|%s' % (g, cond)][m]['median'] for d in r]) for g in gens]
            ax.bar(x + (i - 1.5) * w, v, w, color=mc[m], edgecolor=INK, lw=0.4, label=m)
        ax.set_xticks(x); ax.set_xticklabels(gens, fontsize=6.6, rotation=20); ax.set_yscale('log')
        s, n = cond.split('|'); ax.set_title('%s, %s' % ('no ind. diff.' if s == 'sd=0.0' else 'ind. diff.', n.replace('N=', 'N = ')), fontsize=7.2, loc='left')
    axs[0].set_ylabel('KL divergence, B-first\nanswers (median)')
    h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, fontsize=6.6, frameon=False, ncol=4, loc='lower center', bbox_to_anchor=(0.5, 1.0))
    save(fig, 'Fig4_cross_order.png')


def fig_planning():
    r = load('exp3_planning.json')
    designs = [('fixed-AB|None|0.0', 'Fixed order AB'), ('probe|QL|0.1', 'Probe 10% + QL'), ('probe|QL|0.3', 'Probe 30% + QL'),
               ('probe|Anchoring2|0.1', 'Probe 10% + anchoring'), ('probe|Bayes|0.1', 'Probe 10% + Bayes'), ('split-first|None|0.5', 'Split, first answers')]
    gens = ['QL', 'Bayes', 'Anchoring', 'Mixture']
    fig, axs = plt.subplots(1, 2, figsize=(TEXTWIDTH, 1.9), sharey=True, gridspec_kw=dict(wspace=0.08))
    cols = ['#bdbdbd', BLUE, '#9fbad3', RUST, MID, GREEN]
    for ax, sd in zip(axs, ['sd=0.0', 'sd=0.1']):
        x = np.arange(len(gens)); w = 0.13
        for i, ((k, lab), c) in enumerate(zip(designs, cols)):
            v = [np.mean([r[d]['%s|%s' % (g, sd)][k]['rmse_B'] for d in r]) for g in gens]
            ax.bar(x + (i - 2.5) * w, v, w, color=c, edgecolor=INK, lw=0.4, label=lab)
        ax.set_xticks(x); ax.set_xticklabels([g + ' gen.' for g in gens], fontsize=6.8)
        ax.set_title('(a) Homogeneous population' if sd == 'sd=0.0' else '(b) Individual differences (sd 0.1)', fontsize=7.6, loc='left')
    axs[0].set_ylabel('RMSE of $\\pi_B$ (400 people)')
    h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, fontsize=6.6, frameon=False, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.0))
    save(fig, 'Fig5_planning.png')


def fig_trust():
    r = load('exp4_trust.json'); ns = ['100', '400', '1600']
    fig, axs = plt.subplots(1, 3, figsize=(TEXTWIDTH, 1.8), gridspec_kw=dict(wspace=0.45))
    ax = axs[0]
    for i, g in enumerate(['Markov', 'OpenSystem']):
        t = r['truth'][g]; ax.bar(np.array([0, 1]) + (i - 0.5) * 0.35, [t['final_C0'], t['final_C1']], 0.35,
                                  color=MID if g == 'Markov' else BLUE, edgecolor=INK, lw=0.4, label=g.replace('OpenSystem', 'Open system'))
    ax.set_xticks([0, 1]); ax.set_xticklabels(['final query\nonly', 'query also\nafter 3rd'], fontsize=6.8); ax.set_ylim(0.5, 0.8)
    ax.set_ylabel('P(trust) after 6th'); ax.legend(fontsize=6.2, frameon=False); ax.set_title('(a) Query effect', fontsize=7.6, loc='left')
    ax = axs[1]
    for g in ['Markov', 'OpenSystem']:
        acc = [r['recovery'][g][n][g] / sum(r['recovery'][g][n].values()) for n in ns]
        ax.plot([int(n) for n in ns], acc, marker='o', ms=3, color=MID if g == 'Markov' else BLUE, label=g.replace('OpenSystem', 'Open system') + ' gen.')
    ax.set_xscale('log'); ax.set_xticks([100, 400, 1600]); ax.set_xticklabels(ns); ax.set_ylim(0, 1.02)
    ax.set_xlabel('People per condition'); ax.set_ylabel('Correct (BIC)'); ax.legend(fontsize=6.2, frameon=False); ax.set_title('(b) Model recovery', fontsize=7.6, loc='left')
    ax = axs[2]
    for m, c in (('Markov', MID), ('OpenSystem', BLUE)):
        v = [r['transfer_error']['OpenSystem'][n][m]['rmse'] for n in ns]
        ax.plot([int(n) for n in ns], v, marker='s', ms=3, color=c, label=m.replace('OpenSystem', 'Open system') + ' model')
    ax.axhline(abs(r['truth']['OpenSystem']['query_effect']), color=INK, ls=':', lw=0.6)
    ax.set_xscale('log'); ax.set_xticks([100, 400, 1600]); ax.set_xticklabels(ns); ax.set_xlabel('People in condition C1')
    ax.set_ylabel('RMSE of predicted\nP(trust) without query'); ax.legend(fontsize=6.2, frameon=False); ax.set_title('(c) Transfer, open-system gen.', fontsize=7.6, loc='left')
    save(fig, 'Fig6_trust.png')


def fig_circuits():
    r = load('exp6_circuits.json')['questions']
    labels = ['Aer ideal', 'Braket ideal', 'Braket depolarizing 0.5%', 'Aer FakeTorino dynamic', 'Aer FakeTorino deferred', 'Aer FakeBrisbane dynamic', 'Braket depolarizing 2%']
    short = ['Aer ideal', 'Braket ideal', 'Braket dep. 0.5%', 'FakeTorino dyn.', 'FakeTorino def.', 'FakeBrisbane dyn.', 'Braket dep. 2%']
    fig, axs = plt.subplots(1, 2, figsize=(TEXTWIDTH, 1.9), gridspec_kw=dict(wspace=0.3))
    y = np.arange(len(labels))[::-1]
    for i, d in enumerate(DOMAINS):
        tv = [0.5 * (r[d][l]['tvd_AB'] + r[d][l]['tvd_BA']) for l in labels]; qq = [r[d][l]['qq'] for l in labels]
        c = [BLUE, RUST, GREEN][i]
        axs[0].plot(tv, y + (i - 1) * 0.18, 'o', ms=3.2, color=c, label=DLAB[d])
        axs[1].plot(qq, y + (i - 1) * 0.18, 's', ms=3.2, color=c, label=DLAB[d])
    for ax in axs: ax.set_yticks(y); ax.set_yticklabels(short, fontsize=6.8)
    axs[1].axvline(0, color=INK, lw=0.6, ls=':'); axs[1].set_yticklabels([])
    axs[0].set_xlabel('Total variation distance to the analytic model'); axs[1].set_xlabel('QQ value from circuit output')
    h, l = axs[0].get_legend_handles_labels(); fig.legend(h, l, fontsize=6.6, frameon=False, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.0)); axs[0].set_title('(a) Distortion of answer distributions', fontsize=7.6, loc='left')
    axs[1].set_title('(b) QQ equality under noise', fontsize=7.6, loc='left')
    save(fig, 'Fig7_circuits.png')


if __name__ == '__main__':
    fig_framework(); fig_order_effects()
    for f in (fig_recovery, fig_cross_order, fig_planning, fig_trust, fig_circuits):
        try: f()
        except FileNotFoundError as e: print('skipped', f.__name__, '(missing', os.path.basename(e.filename) + ')')
