"""Supplementary material for "Meta-Learning Orchestration of Learning Modalities on Resource-Constrained
Robots: A Systematic Review" (IEEE TNNLS).

Part 1: confidence-gated routing among four learning modalities with calibrated, miscalibrated and
recalibrated confidence signals, and a sweep of the cost penalty lambda.
Part 2: meta-learned calibration. Each new task (robot, environment or fault condition) shifts the
reported confidences of each modality by an unknown offset; the gate learns the offsets online from
outcomes, either from scratch or starting from a prior meta-learned on a set of training tasks.

All data are synthetic; nothing here is robot data.  Run: python3 Survey3_TNNLS_Supplementary_routing_sim.py
Writes routing_results.json (numbers quoted in the article)."""
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



# ---------------- Part 2: meta-learned calibration across a task distribution ----------------
MU_BIAS = np.array([0.00, 0.30, 0.25, 0.05])    # systematic over-confidence of each modality across tasks
SD_BIAS = 0.10                                  # task-to-task spread of the offsets
NOISE = 0.08

def sample_task(rng):
    """A task fixes the per-modality confidence offsets and how often each situation type occurs."""
    return dict(bias=MU_BIAS + rng.normal(0, SD_BIAS, 4), mix=rng.dirichlet(np.ones(4)))

def online_gate(task, steps, prior_mean, prior_n, rng, lam=0.05, eps=0.05):
    """Gate on (confidence - estimated offset - lam*cost); the offset of the chosen modality is updated
    from the observed outcome as a running mean shrunk towards prior_mean with prior_n pseudo-counts."""
    s = np.zeros(4); n = np.zeros(4); out = np.zeros(steps)
    for t in range(steps):
        ctx = rng.choice(4, p=task['mix']); p = np.full(4, 0.35); p[ctx] = 0.85
        c = np.clip(p + task['bias'] + rng.normal(0, NOISE, 4), 0.01, 0.99)
        b = (prior_n * prior_mean + s) / (prior_n + n)
        k = rng.integers(4) if rng.random() < eps else int(np.argmax(c - b - lam * COST))
        y = rng.random() < p[k]; out[t] = y
        s[k] += c[k] - y; n[k] += 1
    return out

def meta_fit(n_tasks, steps, rng):
    """Meta-training: estimate the mean offset per modality and the pseudo-count n0 = noise/between-task
    variance (empirical Bayes) from logged outcomes on training tasks."""
    est = []
    for _ in range(n_tasks):
        task = sample_task(rng); d = [[] for _ in range(4)]
        for t in range(steps):
            ctx = rng.choice(4, p=task['mix']); p = np.full(4, 0.35); p[ctx] = 0.85
            c = np.clip(p + task['bias'] + rng.normal(0, NOISE, 4), 0.01, 0.99)
            k = rng.integers(4); d[k].append(c[k] - (rng.random() < p[k]))   # exploratory logging policy
        est.append([np.mean(x) for x in d])
    est = np.array(est); mean = est.mean(0)
    within = 0.25                                            # variance of (c - y) for one outcome, about p(1-p)
    between = np.maximum(est.var(0) - within / (steps / 4), 1e-3)
    return mean, np.clip(within / between, 1, 200)

def part2(seed=0, n_test=300, steps=300):
    rng = np.random.default_rng(seed)
    mean, n0 = meta_fit(50, 400, rng)
    curves = {}
    for name, pm, pn in [('Raw confidence (no recalibration)', np.zeros(4), 1e9),
                         ('Online recalibration from scratch', np.zeros(4), 1.0),
                         ('Meta-learned prior + online update', mean, n0)]:
        r = np.array([online_gate(sample_task(np.random.default_rng(seed * 10000 + i)), steps, pm, pn,
                                  np.random.default_rng(seed * 10000 + i + 5000)) for i in range(n_test)])
        curves[name] = r.mean(0)
    orc = []
    for i in range(n_test):
        trng = np.random.default_rng(seed * 10000 + i); task = sample_task(trng)
        rr = np.random.default_rng(seed * 10000 + i + 5000); o = 0
        for t in range(steps):
            ctx = rr.choice(4, p=task['mix']); p = np.full(4, 0.35); p[ctx] = 0.85
            o += rr.random() < p[int(np.argmax(p - 0.05 * COST))]
        orc.append(o / steps)
    return mean, n0, curves, float(np.mean(orc))

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
    res = []
    for seed in range(3):
        mean, n0, curves, orc = part2(seed)
        res.append((mean, n0, curves, orc))
    names = list(res[0][2])
    out['meta'] = dict(prior_mean=[round(float(v), 3) for v in np.mean([r[0] for r in res], 0)],
                       prior_n0=[round(float(v), 1) for v in np.mean([r[1] for r in res], 0)],
                       oracle=round(float(np.mean([r[3] for r in res])), 3),
                       windows={nm: {w: round(float(np.mean([r[2][nm][a:b].mean() for r in res])), 3)
                                     for w, (a, b) in {'steps 1-25': (0, 25), 'steps 26-100': (25, 100), 'steps 101-300': (100, 300)}.items()}
                                for nm in names},
                       curves={nm: [round(float(v), 4) for v in np.mean([r[2][nm] for r in res], 0)] for nm in names})
    json.dump(out, open('routing_results.json', 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'meta'}, indent=1))
    print(json.dumps({k: v for k, v in out['meta'].items() if k != 'curves'}, indent=1))
