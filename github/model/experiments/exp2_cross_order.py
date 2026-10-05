"""Experiment 2: predicting answers in an order that was hardly observed.
Training data: N people (N = 400 or 4000) answer A then B, plus a probe of 10% as many people who answer B then A.
Each model is fitted to the training data and predicts the B-first answer distribution; the score
is the Kullback-Leibler divergence from the generator's true B-first distribution to the prediction
(lower is better). Output: results/exp2_cross_order.json"""
import sys, os, itertools
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.domains import DOMAINS, generator
from qlmodel.fitting import fit, kl
from common import GENERATORS, WORKERS, REPS, save, seed

NS = [400, 4000]
SDS = [0.0, 0.1]
MODELS = ['QL', 'Bayes', 'Anchoring1', 'Anchoring2', 'Saturated']


def job(args):
    d, g, sd, N, rep = args
    gen = generator(d, g, sd=sd)
    rng = np.random.default_rng(seed(d, g, sd, N, rep, 'e2'))
    data = {'AB': rng.multinomial(N, gen.cells('A', 'B')), 'BA': rng.multinomial(N // 10, gen.cells('B', 'A'))}
    true_ba = gen.cells('B', 'A')
    return d, g, 'sd=%.1f|N=%d' % (sd, N), {m: kl(true_ba, fit(m, data, restarts=8, rng=rng)['model'].cells('B', 'A')) for m in MODELS}


if __name__ == '__main__':
    jobs = list(itertools.product(DOMAINS, GENERATORS, SDS, NS, range(REPS)))
    with Pool(WORKERS) as p: out = p.map(job, jobs, chunksize=4)
    res = {}
    for d, g, cond, k in out:
        r = res.setdefault(d, {}).setdefault(g + '|' + cond, {m: [] for m in MODELS})
        for m, v in k.items(): r[m].append(v)
    summary = {d: {g: {m: dict(mean=float(np.mean(v)), median=float(np.median(v)), sd=float(np.std(v))) for m, v in r.items()} for g, r in rd.items()} for d, rd in res.items()}
    save('exp2_cross_order.json', summary)
