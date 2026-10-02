"""Illustrative simulation (Survey 3, Section 12): budget-aware routing among four learning modalities
using confidence signals that are either calibrated or miscalibrated. Synthetic; not robot data."""
import numpy as np
M = ['Vision', 'RL', 'Imitation', 'Fault-recovery']
COST = np.array([1.0, 3.0, 2.0, 4.0])          # relative compute cost per invocation

def episode_contexts(n, rng):
    # each step belongs to one of 4 latent situation types; each modality is best in one type
    return rng.integers(0, 4, n)

def success_prob(ctx):
    P = np.full((len(ctx), 4), 0.35)
    P[np.arange(len(ctx)), ctx] = 0.85          # the matching modality succeeds 85% of the time
    return P

def reported_conf(P, rng, kind):
    noise = rng.normal(0, 0.08, P.shape)
    if kind == 'calibrated':   c = P + noise
    elif kind == 'overconfident':  # imitation & RL overconfident (common for BC / policy entropy proxies)
        c = P + noise; c[:, 1] += 0.35; c[:, 2] += 0.30
    return np.clip(c, 0.01, 0.99)

def run(policy, n=20000, lam=0.05, budget=None, seed=0, kind='calibrated'):
    rng = np.random.default_rng(seed)
    ctx = episode_contexts(n, rng); P = success_prob(ctx); C = reported_conf(P, rng, kind)
    if policy == 'oracle': a = P.argmax(1)
    elif policy == 'fixed': a = np.full(n, np.argmax(P.mean(0) - lam * COST))
    elif policy == 'random': a = rng.integers(0, 4, n)
    elif policy == 'all':   # invoke every modality, take best outcome (upper bound on success, max cost)
        succ = (rng.random((n, 4)) < P).any(1); return succ.mean(), COST.sum()
    elif policy == 'recal':  # per-modality Platt-style (linear) recalibration fitted on a separate calibration set
        rc = np.random.default_rng(seed + 1000); cctx = episode_contexts(4000, rc); cP = success_prob(cctx)
        cC = reported_conf(cP, rc, kind); y = rc.random(cP.shape) < cP
        coef = [np.polyfit(cC[:, m], y[:, m].astype(float), 1) for m in range(4)]
        Cr = np.column_stack([np.polyval(coef[m], C[:, m]) for m in range(4)])
        a = (Cr - lam * COST).argmax(1)
    else: a = (C - lam * COST).argmax(1)            # confidence-gated, cost-penalised routing
    succ = rng.random(n) < P[np.arange(n), a]
    return succ.mean(), COST[a].mean()

if __name__ == '__main__':
    import json
    out = {}
    for name, pol, kind in [('Oracle (true success prob.)', 'oracle', 'calibrated'), ('Invoke all four', 'all', 'calibrated'),
                            ('Fixed single modality', 'fixed', 'calibrated'), ('Random modality', 'random', 'calibrated'),
                            ('Gate on calibrated confidence', 'gate', 'calibrated'), ('Gate on miscalibrated confidence', 'gate', 'overconfident'), ('Gate on recalibrated confidence', 'recal', 'overconfident')]:
        r = [run(pol, seed=s, kind=kind) for s in range(10)]
        out[name] = dict(success=round(float(np.mean([x[0] for x in r])), 3), sd=round(float(np.std([x[0] for x in r])), 3), cost=round(float(np.mean([x[1] for x in r])), 2))
    sweep = {}
    for kind in ('calibrated', 'overconfident'):
        sweep[kind] = [(lam, *[round(float(v), 3) for v in np.mean([run('gate', lam=lam, seed=s, kind=kind) for s in range(5)], 0)]) for lam in (0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3)]
    out['sweep'] = sweep
    json.dump(out, open('routing_results.json', 'w'), indent=1); print(json.dumps(out, indent=1))
