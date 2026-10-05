"""Figure style of the model paper (IEEEtran journal, as Survey 3): drawn at the printed size (column 252 pt = 3.5 in,
text width 516 pt = 7.16 in, body 10 pt),
Times-like text (STIX) to match the IEEEtran manuscript, thin dark outlines, white or light-grey fills and a
restrained, print- and colour-blind-safe palette."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

TEXTWIDTH = 516 / 72.27          # inches (two columns)
COLWIDTH = 252 / 72.27           # inches (one column)
DPI = 600

INK = '#1a1a1a'                  # text and outlines
MID = '#6b6b6b'                  # secondary lines
LIGHT = '#d9d9d9'                # light grey fill
PALE = '#f2f2f2'                 # very light grey fill
BLUE = '#2c5d8a'                 # single accent (muted navy)
BLUE_PALE = '#dde7f0'
RUST = '#a3542a'                 # second accent, used sparingly
GREEN = '#4f7f52'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'axes.unicode_minus': False,
    'font.size': 8.5,
    'axes.labelsize': 8.5,
    'axes.titlesize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'lines.linewidth': 1.1,
    'axes.edgecolor': INK,
    'axes.labelcolor': INK,
    'xtick.color': INK,
    'ytick.color': INK,
    'text.color': INK,
    'savefig.dpi': DPI,
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})


def box(ax, x, y, w, h, text, fc='white', ec=INK, lw=0.7, fs=8, weight='normal', ls='-', align='center'):
    """Rectangle with centred (or left-aligned) text; coordinates in axes units of the canvas."""
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, ls=ls, joinstyle='miter'))
    if align == 'left':
        ax.text(x + 0.012, y + h / 2, text, ha='left', va='center', fontsize=fs, weight=weight, linespacing=1.15)
    else:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, weight=weight, linespacing=1.15)


def arrow(ax, x1, y1, x2, y2, ls='-', lw=0.7, color=INK, rad=0.0, head=6):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=head, lw=lw, color=color,
                                 linestyle=ls, connectionstyle=f'arc3,rad={rad}', shrinkA=0, shrinkB=0))


def canvas(height_in, width_in=TEXTWIDTH):
    fig = plt.figure(figsize=(width_in, height_in))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    return fig, ax
