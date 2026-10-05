"""Experiment 3: which questioning design recovers the first-position ('unprimed') answer rates?
Each design spends 400 people who answer both questions (see qlmodel/planner.py). Score: root mean
square error of (pi_A, pi_B) against the generator's true first-position rates, over repetitions.
Output: results/exp3_planning.json"""
import sys, os, itertools
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.domains import DOMAINS, generator
from qlmodel.planner import estimate
from common import GENERATORS, WORKERS, REPS, save, seed

N = 400
DESIGNS = [('fixed-AB', None, 0), ('probe', 'QL', 0.1), ('probe', 'Anchoring2', 0.1), ('probe', 'Bayes', 0.1),
           ('probe', 'QL', 0.3), ('split-first', None, 0.5)]


def job(args):
    d, g, sd, rep = args
    gen = generator(d, g, sd=sd); truth = gen.rates()[:2]
    out = {}
    for design, model, f in DESIGNS:
        rng = np.random.default_rng(seed(d, g, sd, rep, design, model, f))
        est = np.array(estimate(design, model, gen, N, rng, f=f))
        out['%s|%s|%.1f' % (design, model, f)] = (est - truth).tolist()
    return d, g + '|sd=%.1f' % sd, out


if __name__ == '__main__':
    jobs = list(itertools.product(DOMAINS, GENERATORS, [0.0, 0.1], range(REPS)))
    with Pool(WORKERS) as p: out = p.map(job, jobs, chunksize=4)
    res = {}
    for d, g, o in out:
        r = res.setdefault(d, {}).setdefault(g, {})
        for k, e in o.items(): r.setdefault(k, []).append(e)
    summary = {}
    for d, rd in res.items():
        for g, r in rd.items():
            for k, errs in r.items():
                e = np.array(errs)
                summary.setdefault(d, {}).setdefault(g, {})[k] = dict(rmse=float(np.sqrt(np.mean(e ** 2))), bias_A=float(e[:, 0].mean()),
                                                                  bias_B=float(e[:, 1].mean()), rmse_B=float(np.sqrt(np.mean(e[:, 1] ** 2))))
    save('exp3_planning.json', summary)
