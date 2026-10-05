"""Experiment 1: can the models be told apart from answer counts?
For each domain, generator and sample size (people per order), simulate answers in both orders, fit
the QL, Bayes and two-weight anchoring models, and select the model with the lowest BIC. Also run
the QQ test (two-sided, alpha = 0.05). Populations are homogeneous (sd = 0) or heterogeneous
(individual parameters spread with sd = 0.1). Output: results/exp1_model_recovery.json"""
import sys, os, itertools
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.domains import DOMAINS, generator
from qlmodel.fitting import fit, qq_test
from common import GENERATORS, CANDIDATES, WORKERS, REPS, save, seed

NS = [100, 400, 1600]
SDS = [0.0, 0.1]   # individual differences: none, or parameter spread 0.1


def job(args):
    d, g, sd, n, rep = args
    gen = generator(d, g, sd=sd)
    rng = np.random.default_rng(seed(d, g, sd, n, rep))
    data = {o: rng.multinomial(n, gen.cells(o[0], o[1])) for o in ('AB', 'BA')}
    fits = {m: fit(m, data, restarts=8, rng=rng) for m in CANDIDATES}
    best = min(fits, key=lambda m: fits[m]['bic'])
    return d, g, sd, n, best, abs(qq_test(data)) > 1.96


if __name__ == '__main__':
    jobs = list(itertools.product(DOMAINS, GENERATORS, SDS, NS, range(REPS)))
    with Pool(WORKERS) as p: out = p.map(job, jobs, chunksize=4)
    res = {}
    for d, g, sd, n, best, rej in out:
        r = res.setdefault(d, {}).setdefault(g, {}).setdefault('sd=%.1f' % sd, {}).setdefault(str(n), {'selected': {m: 0 for m in CANDIDATES}, 'qq_reject': 0, 'reps': 0})
        r['selected'][best] += 1; r['qq_reject'] += int(rej); r['reps'] += 1
    save('exp1_model_recovery.json', res)
