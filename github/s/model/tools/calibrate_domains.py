"""Finds the population parameters of the domain generators (qlmodel/domains.py) from target
first- and second-position 'yes' rates. Run from github/s/model: python3 tools/calibrate_domains.py
Targets are illustrative: object clarification copies the size of the Clinton-Gore order effect
(Moore, 2002); trust and hand-over has a smaller assimilation effect; preference elicitation has a
contrast effect (the first-asked option makes the second look better)."""
import sys, os, itertools
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.quantum_like import QLQuestionModel
from qlmodel.classical import Anchoring

TARGETS = {'object_clarification': (0.50, 0.68, 0.57, 0.60),     # pA first, pB first, pA second, pB second
           'trust_handover': (0.62, 0.80, 0.68, 0.75),
           'preference_elicitation': (0.55, 0.62, 0.47, 0.69)}


def marg(m):
    ab, ba = m.cells('A', 'B'), m.cells('B', 'A')
    return np.array([ab[0] + ab[1], ba[0] + ba[1], ba[0] + ba[2], ab[0] + ab[2]])


if __name__ == '__main__':
    for d, t in TARGETS.items():
        t = np.array(t); best = None
        for ranks in itertools.product((1, 2), repeat=2):
            for s in range(60):
                r = least_squares(lambda x: marg(QLQuestionModel(*x, ranks=ranks)) - t, np.random.default_rng(s).uniform(0, np.pi, 3))
                if best is None or r.cost < best[0].cost: best = (r, ranks)
        r, ranks = best
        print(d, 'QL angles', np.round(r.x, 4).tolist(), 'ranks', ranks, 'rates', np.round(marg(QLQuestionModel(*r.x, ranks=ranks)), 3).tolist())
        ra = least_squares(lambda y: marg(Anchoring(t[0], t[1], y[0], y[1])) - t, [0.1, 0.1], bounds=([-0.95] * 2, [0.95] * 2))
        print('   anchoring weights', np.round(ra.x, 4).tolist(), 'rates', np.round(marg(Anchoring(t[0], t[1], *ra.x)), 3).tolist())
