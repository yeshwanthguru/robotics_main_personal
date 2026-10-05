"""Shows that, with the question order fixed (A then B), the first-position rate of B is not
identifiable under the quantum-like model: several parameter sets reproduce the same A-first answers
exactly but imply different B-first rates. Run from github/model: python3 tools/identifiability.py"""
import sys, os, json
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.domains import DOMAINS, ql_mean
from qlmodel.quantum_like import QLQuestionModel

out = {}
for d in DOMAINS:
    m = ql_mean(d); ab = m.cells('A', 'B'); res = {}
    for ranks in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        sols = set()
        for s in range(100):
            r = least_squares(lambda x: QLQuestionModel(*x, ranks=ranks).cells('A', 'B')[:3] - ab[:3], np.random.default_rng(s).uniform(0, np.pi, 3))
            if r.cost < 1e-12: sols.add(round(QLQuestionModel(*r.x, ranks=ranks).first_position('B'), 4))
        res[str(ranks)] = sorted(sols)
    out[d] = dict(true_piB=round(m.first_position('B'), 4), solutions_by_ranks=res)
    print(d, out[d])
json.dump(out, open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results', 'identifiability.json'), 'w'), indent=1)
