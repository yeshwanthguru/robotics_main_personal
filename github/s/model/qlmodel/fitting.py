"""Maximum-likelihood fitting of the question-order models to answer counts.

Data format: {'AB': counts of [yy, yn, ny, nn] with A asked first,
              'BA': counts of [yy, yn, ny, nn] with B asked first (first answer is B)}.
Either order may be missing. Models are specified by an unconstrained parameter vector."""
import numpy as np
from scipy.optimize import minimize
from .quantum_like import QLQuestionModel
from .classical import BayesJoint, Anchoring, Saturated

from scipy.special import expit as sig


def _sat(x):
    def sm(v): e = np.exp(np.r_[v, 0.0] - max(np.max(v), 0)); return e / e.sum()
    return Saturated(sm(x[:3]), sm(x[3:]))


SPECS = {
    'QL':         (3, None),   # angles (a, b, g); the ranks of the two 'yes' subspaces are chosen by likelihood
    'Bayes':      (3, lambda x: BayesJoint(sig(x[0]), sig(x[1]), np.tanh(x[2]))),
    'Anchoring1': (3, lambda x: Anchoring(sig(x[0]), sig(x[1]), np.tanh(x[2]), np.tanh(x[2]))),
    'Anchoring2': (4, lambda x: Anchoring(sig(x[0]), sig(x[1]), np.tanh(x[2]), np.tanh(x[3]))),
    'Saturated':  (6, _sat),
}


def cells(model, order):
    return model.cells(order[0], order[1])


def loglik(model, data):
    ll = 0.0
    for order, n in data.items():
        p = np.clip(cells(model, order), 1e-12, 1)
        ll += float(np.dot(n, np.log(p)))
    return ll


RANKS = [(1, 1), (1, 2), (2, 1), (2, 2)]


def builder(name, ranks=None):
    if name == 'QL':
        return lambda x: QLQuestionModel(x[0], x[1], x[2], ranks)
    return SPECS[name][1]


def fit(name, data, restarts=12, rng=None):
    rng = np.random.default_rng(0) if rng is None else rng
    k = SPECS[name][0]
    best, build = None, None
    for ranks in (RANKS if name == 'QL' else [None]):
        b = builder(name, ranks)
        for _ in range(restarts if name != 'QL' else max(3, restarts // 4)):
            x0 = rng.uniform(0, np.pi, k) if name == 'QL' else rng.normal(0, 1, k)
            r = minimize(lambda x: -loglik(b(x), data), x0, method='Nelder-Mead',
                         options=dict(maxiter=4000, xatol=1e-7, fatol=1e-9))
            if best is None or r.fun < best.fun: best, build = r, b
    n = sum(int(np.sum(v)) for v in data.values())
    ll = -best.fun
    return dict(name=name, x=best.x, model=build(best.x), ll=ll, k=k, bic=k * np.log(n) - 2 * ll, aic=2 * k - 2 * ll)


def sample(model, n_per_order, rng, orders=('AB', 'BA')):
    return {o: rng.multinomial(n_per_order, np.clip(cells(model, o), 0, 1) / np.clip(cells(model, o), 0, 1).sum()) for o in orders}


def qq_test(data):
    """z statistic of the QQ equality from counts in both orders (normal approximation)."""
    ab, ba = np.asarray(data['AB'], float), np.asarray(data['BA'], float)
    p1 = (ab[1] + ab[2]) / ab.sum(); p2 = (ba[1] + ba[2]) / ba.sum()
    se = np.sqrt(p1 * (1 - p1) / ab.sum() + p2 * (1 - p2) / ba.sum())
    return (p1 - p2) / se if se > 0 else 0.0


def kl(p, q):
    p, q = np.clip(p, 1e-12, 1), np.clip(q, 1e-12, 1)
    return float(np.sum(p * np.log(p / q)))
