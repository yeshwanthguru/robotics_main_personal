"""Shared figure style for Survey 1: Linux Biolinum (the ACM sans), thin rules, square boxes."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FONT = 'Linux Biolinum O'
INK, MUTED, RULE, GRID, PANEL = '#1f1f1f', '#4d4d4d', '#7a7a7a', '#e2e2df', '#f2f2f0'
# categorical order is fixed: computation, quantum-inspired, sensing, communication, review
COLORS = ['#3b6fa8', '#c96a3d', '#2f9c74', '#d6a338', '#b1b1ac']
ACCENT = COLORS[0]
plt.rcParams.update({
    'font.family': FONT, 'font.size': 10, 'axes.linewidth': 0.8, 'axes.edgecolor': RULE,
    'xtick.color': MUTED, 'ytick.color': MUTED, 'xtick.major.width': 0.8, 'ytick.major.width': 0.8,
    'legend.frameon': False, 'savefig.dpi': 300, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.04,
})


def style_axes(ax):
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    ax.set_axisbelow(True)


def box(ax, x, y, w, h, text='', fill='white', edge=RULE, lw=0.8, size=9.5, weight='normal', ls='-', color=INK,
        z=2):
    ax.add_patch(plt.Rectangle((x, y), w, h, fc=fill, ec=edge, lw=lw, ls=ls, zorder=z))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=size, weight=weight,
                color=color, linespacing=1.25, zorder=3)


def arrow(ax, pts, color=RULE, lw=1.0, ls='-'):
    """Orthogonal polyline through pts with an arrowhead on the last segment."""
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=5,
            solid_capstyle='butt')
    ax.annotate('', xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle='-|>,head_length=0.45,head_width=0.22', color=color, lw=lw, ls='-',
                                shrinkA=0, shrinkB=0), zorder=6)
