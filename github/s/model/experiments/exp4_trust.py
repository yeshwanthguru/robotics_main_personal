"""Experiment 4: does asking about trust change trust, and can a robot tell which dynamics hold?
A person watches six robot hand-overs with outcomes (success, success, failure, success, failure,
success). Condition C0: the robot asks 'Do you trust me to hand over the next tool?' only after the
sixth hand-over. Condition C1: it also asks after the third. Generators: an open-system (quantum-like)
model with partial dephasing, and the Markov model that best matches it. Both models are fitted to
C0 and C1 answers (N people per condition) and compared by BIC. The robot-relevant quantity is the
query effect: the change in final trust caused by the intermediate question. Fitting each model on
C1 only and predicting C0 shows the error a robot makes if it assumes that asking has no effect.
Output: results/exp4_trust.json"""
import sys, os, itertools
import numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.trust import MarkovTrust, OpenSystemTrust, final_trust
from common import WORKERS, REPS, save, seed

OUT = [1, 1, 0, 1, 0, 1]
C0, C1 = {5}, {2, 5}
TRUE_OS = (1.6, 0.8, 1.2, 0.3)      # phi0, a_s, a_f, gamma (illustrative values)
from scipy.special import expit as sig
BUILD = {'Markov': (3, lambda x: MarkovTrust(sig(x[0]), sig(x[1]), sig(x[2]))),
         'OpenSystem': (4, lambda x: OpenSystemTrust(np.pi * sig(x[0]), np.pi * sig(x[1]), np.pi * sig(x[2]), sig(x[3])))}


def probs(m, cond):
    p = m.answer_probs(OUT, cond); keys = sorted(p)
    return keys, np.array([p[k] for k in keys])


def ll(m, data):
    tot = 0.0
    for cond, counts in data.items():
        keys, p = probs(m, C0 if cond == 'C0' else C1)
        tot += float(np.dot(counts, np.log(np.clip(p, 1e-12, 1))))
    return tot


def fit(name, data, rng, restarts=8):
    k, b = BUILD[name]; best = None
    for _ in range(restarts):
        r = minimize(lambda x: -ll(b(x), data), rng.normal(0, 1.5, k), method='Nelder-Mead', options=dict(maxiter=3000))
        if best is None or r.fun < best.fun: best = r
    n = sum(int(c.sum()) for c in data.values())
    return b(best.x), -best.fun, k * np.log(n) - 2 * (-best.fun)


def sample(m, n, rng):
    return {c: rng.multinomial(n, probs(m, C0 if c == 'C0' else C1)[1]) for c in ('C0', 'C1')}


def markov_match():
    """Markov model closest (in expected log-likelihood) to the open-system generator."""
    os_m = OpenSystemTrust(*TRUE_OS)
    exp = {c: 1e5 * probs(os_m, C0 if c == 'C0' else C1)[1] for c in ('C0', 'C1')}
    m, _, _ = fit('Markov', exp, np.random.default_rng(0), restarts=20)
    return m


def job(args):
    gname, n, rep = args
    gen = OpenSystemTrust(*TRUE_OS) if gname == 'OpenSystem' else markov_match()
    rng = np.random.default_rng(seed(gname, n, rep))
    data = sample(gen, n, rng)
    bic = {m: fit(m, data, rng)[2] for m in BUILD}
    # transfer: fit on C1 only, predict final trust in C0
    pred = {m: final_trust(fit(m, {'C1': data['C1']}, rng)[0], OUT, C0) for m in BUILD}
    return gname, n, min(bic, key=bic.get), pred


if __name__ == '__main__':
    os_m, mk = OpenSystemTrust(*TRUE_OS), markov_match()
    truth = {g: dict(final_C0=final_trust(m, OUT, C0), final_C1=final_trust(m, OUT, C1)) for g, m in (('OpenSystem', os_m), ('Markov', mk))}
    for g in truth: truth[g]['query_effect'] = truth[g]['final_C1'] - truth[g]['final_C0']
    jobs = list(itertools.product(['OpenSystem', 'Markov'], [100, 400, 1600], range(REPS)))
    with Pool(WORKERS) as p: out = p.map(job, jobs, chunksize=2)
    res = {'outcomes': OUT, 'open_system_params': TRUE_OS, 'markov_match': dict(p0=mk.p0, s_up=mk.s_up, f_down=mk.f_down), 'truth': truth, 'recovery': {}, 'transfer_error': {}}
    for g, n, best, pred in out:
        r = res['recovery'].setdefault(g, {}).setdefault(str(n), {'Markov': 0, 'OpenSystem': 0}); r[best] += 1
        t = res['transfer_error'].setdefault(g, {}).setdefault(str(n), {m: [] for m in BUILD})
        for m, v in pred.items(): t[m].append(v - truth[g]['final_C0'])
    for g in res['transfer_error']:
        for n in res['transfer_error'][g]:
            res['transfer_error'][g][n] = {m: dict(bias=float(np.mean(v)), rmse=float(np.sqrt(np.mean(np.square(v))))) for m, v in res['transfer_error'][g][n].items()}
    save('exp4_trust.json', res)
