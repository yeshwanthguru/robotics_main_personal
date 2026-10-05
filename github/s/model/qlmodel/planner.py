"""Question planning for a robot that must learn what people think before its own questions
influence them.

The target is the pair of first-position 'yes' rates (pi_A, pi_B): the answers that each question
gets when it is asked first. Each person answers both questions, so every design spends the same
number of people. Designs (every person answers both questions; n people per design):
  fixed-AB      everyone answers A then B; pi_A from the first answers and pi_B from the
                second answers (what a robot that ignores order effects would do). With the order
                fixed, pi_B is not identifiable under the QL model: two parameter sets reproduce the
                same AB answers but imply different pi_B (tools/identifiability.py);
  probe         a fraction f of people answer B first (default f = 0.1), the rest A first; a
                model fitted to all answers gives both rates; the probe resolves the ambiguity;
  split-first   half AB, half BA; each rate from first answers only (model-free, no model risk).
The functions return estimates; experiments/exp3_planning.py scores them.
"""
import numpy as np
from .fitting import fit


def estimate(design, model_name, gen, n, rng, f=0.1):
    if design == 'fixed-AB':
        c = rng.multinomial(n, gen.cells('A', 'B'))
        return (c[0] + c[1]) / n, (c[0] + c[2]) / n
    if design == 'split-first':
        h = n // 2
        ab, ba = rng.multinomial(h, gen.cells('A', 'B')), rng.multinomial(n - h, gen.cells('B', 'A'))
        return (ab[0] + ab[1]) / h, (ba[0] + ba[1]) / (n - h)
    nb = max(1, int(round(f * n)))
    data = {'AB': rng.multinomial(n - nb, gen.cells('A', 'B')), 'BA': rng.multinomial(nb, gen.cells('B', 'A'))}
    m = fit(model_name, data, restarts=8, rng=rng)['model']
    return float(m.cells('A', 'B')[:2].sum()), float(m.cells('B', 'A')[:2].sum())
