"""Experiment 5: the models against two published order and interference effects.
(a) Clinton-Gore: fit each model's four marginal rates (first and second position for both
    questions) by least squares; the Bayes model predicts no order effect.
(b) Prisoner's dilemma: the classical law of total probability bounds P(defect | unknown) between
    the two known-opponent rates; the quantum-like law with an interference term reaches the
    observed rate for an interference phase computed in closed form.
Only aggregate proportions are available, so no likelihoods or BIC are computed.
Output: results/exp5_literature.json"""
import sys, os, itertools
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.quantum_like import QLQuestionModel, interference_total_probability
from qlmodel.classical import BayesJoint, Anchoring
from literature_data import CLINTON_GORE as CG, PRISONERS_DILEMMA as PD
from common import save

t = np.array([CG['pA_first'], CG['pB_first'], CG['pA_second'], CG['pB_second']])


def rates(m):
    ab, ba = m.cells('A', 'B'), m.cells('B', 'A')
    return np.array([ab[0] + ab[1], ba[0] + ba[1], ba[0] + ba[2], ab[0] + ab[2]])


res = {'clinton_gore': {'observed': t.tolist()}}
best = None
for ranks in itertools.product((1, 2), repeat=2):
    for s in range(60):
        r = least_squares(lambda x: rates(QLQuestionModel(*x, ranks=ranks)) - t, np.random.default_rng(s).uniform(0, np.pi, 3))
        if best is None or r.cost < best[0].cost: best = (r, ranks)
r, ranks = best
res['clinton_gore']['QL'] = dict(params=r.x.tolist(), ranks=list(ranks), k=3, fitted=rates(QLQuestionModel(*r.x, ranks=ranks)).tolist())
for name, k, build, x0 in [('Anchoring1', 3, lambda y: Anchoring(y[0], y[1], y[2], y[2]), [0.5, 0.6, 0.1]),
                           ('Anchoring2', 4, lambda y: Anchoring(y[0], y[1], y[2], y[3]), [0.5, 0.6, 0.1, 0.1]),
                           ('Bayes', 3, lambda y: BayesJoint(y[0], y[1], y[2]), [0.5, 0.6, 0.0])]:
    lo = [0.01, 0.01] + [-0.99] * (k - 2); hi = [0.99, 0.99] + [0.99] * (k - 2)
    rr = least_squares(lambda y: rates(build(y)) - t, x0, bounds=(lo, hi))
    res['clinton_gore'][name] = dict(params=rr.x.tolist(), k=k, fitted=rates(build(rr.x)).tolist())
for name, v in res['clinton_gore'].items():
    if name != 'observed': v['sse'] = float(np.sum((np.array(v['fitted']) - t) ** 2))

p1, p2, obs = PD['defect_given_defect'], PD['defect_given_cooperate'], PD['defect_unknown']
c = 0.5   # belief that the opponent defects when the move is unknown
cos_phase = (obs - c * p1 - (1 - c) * p2) / (2 * np.sqrt(c * p1 * (1 - c) * p2))
res['prisoners_dilemma'] = dict(observed=PD, classical_range=[min(p1, p2), max(p1, p2)], belief_c=c,
                                cos_phase=float(cos_phase), phase_rad=float(np.arccos(cos_phase)),
                                ql_prediction=float(interference_total_probability(p1, p2, c, np.arccos(cos_phase))),
                                note='One interference parameter is solved from one number, so this shows that the quantum-like law can '
                                     'represent the effect, not that it predicts it.')
save('exp5_literature.json', res)
print(json.dumps(res, indent=1) if False else {k: (v['fitted'], round(v['sse'], 6)) for k, v in res['clinton_gore'].items() if k != 'observed'})
print(res['prisoners_dilemma'])
