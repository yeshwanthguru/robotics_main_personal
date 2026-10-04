"""Online Resource 2 for "Quantum-Like Cognition and Decision-Making for Autonomous Agents, from Robotics to
AI/ML Systems: A Systematic Review" (Artificial Intelligence Review). Authors: Yeshwanth Guru and Dev Kunwar Singh Chauhan.
Reproduces the worked examples (Table C2) and the illustrative RL experiment (Section 16.3, Table C1, Fig. 9).
Pure NumPy; runs on any laptop.  Usage:  python3 Survey2_AIR_Online_Resource_2_code.py [--rl]"""
import numpy as np

def proj(theta):
    """Rank-1 projector onto the unit vector at angle theta in a real 2-D Hilbert space."""
    v = np.array([np.cos(theta), np.sin(theta)])
    return np.outer(v, v)

def seq_prob(psi, P1, P2):
    """Lüders rule: probability of 'yes' to question 1 then 'yes' to question 2."""
    return float(np.linalg.norm(P2 @ P1 @ psi) ** 2)

# ---------- Example 1: question-order effect and the QQ equality
def order_effect(theta_psi=np.deg2rad(20), theta_A=np.deg2rad(0), theta_B=np.deg2rad(55)):
    psi = np.array([np.cos(theta_psi), np.sin(theta_psi)])
    A, B = proj(theta_A), proj(theta_B)
    I = np.eye(2); An, Bn = I - A, I - B
    p = {}
    p['A'] = float(psi @ A @ psi); p['B'] = float(psi @ B @ psi)
    p['AyBy'] = seq_prob(psi, A, B); p['ByAy'] = seq_prob(psi, B, A)
    p['AnBn'] = seq_prob(psi, An, Bn); p['BnAn'] = seq_prob(psi, Bn, An)
    p['AyBn'] = seq_prob(psi, A, Bn); p['ByAn'] = seq_prob(psi, B, An)
    # QQ equality: [p(AyBn)+p(AnBy)] - [p(ByAn)+p(BnAy)] = 0
    AnBy = seq_prob(psi, An, B); BnAy = seq_prob(psi, Bn, A)
    p['QQ'] = (p['AyBn'] + AnBy) - (p['ByAn'] + BnAy)
    p['commutator_norm'] = float(np.linalg.norm(A @ B - B @ A))
    return p

# ---------- Example 2: conjunction fallacy (Linda) as sequential projection
def conjunction(theta_psi=np.deg2rad(0), theta_F=np.deg2rad(40), theta_BT=np.deg2rad(80)):
    psi = np.array([np.cos(theta_psi), np.sin(theta_psi)])
    F, BT = proj(theta_F), proj(theta_BT)
    p_BT = float(psi @ BT @ psi)
    p_F_then_BT = seq_prob(psi, F, BT)          # judge 'feminist' first, then 'bank teller'
    return dict(p_F=float(psi @ F @ psi), p_BT=p_BT, p_F_and_BT=p_F_then_BT, fallacy=p_F_then_BT > p_BT)

# ---------- Example 3: disjunction effect / sure-thing violation (Shafir & Tversky 1992 PD data)
def interference(pD_knownD=0.97, pD_knownC=0.84, pD_unknown=0.63, prior=0.5):
    classical = prior * pD_knownD + (1 - prior) * pD_knownC
    interf = pD_unknown - classical
    cos_theta = interf / (2 * np.sqrt(prior * pD_knownD * (1 - prior) * pD_knownC))
    return dict(classical=classical, observed=pD_unknown, interference=interf,
                cos_theta=cos_theta, theta_deg=float(np.degrees(np.arccos(cos_theta))))

# ---------- Example 4: classical vs quantum-like fusion of two cues (Section 16.1)
def kalman_fusion(z1=2.10, r1=0.04, z2=1.90, r2=0.09):
    """Static two-sensor fusion = one Kalman update with prior from sensor 1."""
    k = r1 / (r1 + r2); x = z1 + k * (z2 - z1); p = (1 - k) * r1
    x_rev = z2 + (r2 / (r1 + r2)) * (z1 - z2)
    return dict(x=x, var=p, x_reversed=x_rev)

def qlbn_two_cues(pH_given_c1=0.80, pH_given_c2=0.30, w1=0.5, theta_deg=0.0):
    """Quantum-like law of total probability with an interference phase theta."""
    classical = w1 * pH_given_c1 + (1 - w1) * pH_given_c2
    interf = 2 * np.sqrt(w1 * pH_given_c1 * (1 - w1) * pH_given_c2) * np.cos(np.deg2rad(theta_deg))
    return dict(classical=classical, quantum_like=classical + interf)

# ---------- Example 5: order-dependent labelling (Section 16.2)
def label_order(theta_img=np.deg2rad(35), theta_cat=np.deg2rad(0), theta_wild=np.deg2rad(60)):
    psi = np.array([np.cos(theta_img), np.sin(theta_img)])
    C, W = proj(theta_cat), proj(theta_wild)
    return dict(p_cat=float(psi @ C @ psi), p_wild=float(psi @ W @ psi),
                cat_then_wild=seq_prob(psi, C, W), wild_then_cat=seq_prob(psi, W, C))

# ---------- Example 6: small RL experiment (Section 16.3)
class Grid:
    """6x6 grid, start (0,0), goal (5,5) reward 1 +- noise, step cost -0.01, 4 walls."""
    def __init__(s, n=6, noise=0.0, rng=None):
        s.n, s.noise, s.rng = n, noise, rng
        s.walls = {(1, 1), (2, 3), (3, 1), (4, 4)}
    def reset(s): s.pos = (0, 0); return s.idx(s.pos)
    def idx(s, p): return p[0] * s.n + p[1]
    def step(s, a):
        dx, dy = [(-1, 0), (1, 0), (0, -1), (0, 1)][a]
        nx, ny = s.pos[0] + dx, s.pos[1] + dy
        if 0 <= nx < s.n and 0 <= ny < s.n and (nx, ny) not in s.walls: s.pos = (nx, ny)
        if s.pos == (s.n - 1, s.n - 1):
            return s.idx(s.pos), 1.0 + s.noise * s.rng.standard_normal(), True
        return s.idx(s.pos), -0.01 + s.noise * s.rng.standard_normal(), False

def run_agent(kind, seed, episodes=300, noise=0.0, alpha=0.1, gamma=0.95, max_steps=200, k=30.0):
    rng = np.random.default_rng(seed); env = Grid(noise=noise, rng=rng)
    nS, nA = env.n * env.n, 4
    Q = np.zeros((nS, nA)); V = np.zeros(nS)
    amp = np.full((nS, nA), 0.5)                 # QRL: equal amplitudes 1/sqrt(4)
    steps_log = []
    for ep in range(episodes):
        s = env.reset(); done = False; t = 0
        while not done and t < max_steps:
            if kind == 'eps':                     # epsilon-greedy Q-learning, eps decays 0.3 -> 0.01
                eps = max(0.01, 0.3 * (1 - ep / (0.6 * episodes)))
                a = rng.integers(nA) if rng.random() < eps else int(rng.choice(np.flatnonzero(Q[s] == Q[s].max())))
            elif kind == 'softmax':               # Boltzmann Q-learning, tau decays 0.2 -> 0.01
                tau = max(0.01, 0.2 * (1 - ep / (0.6 * episodes)))
                z = Q[s] / tau; z -= z.max(); pr = np.exp(z) / np.exp(z).sum(); a = int(rng.choice(nA, p=pr))
            else:                                  # QRL (Dong et al. 2008): 'measure' the action superposition
                pr = amp[s] ** 2; pr /= pr.sum(); a = int(rng.choice(nA, p=pr))
            s2, r, done = env.step(a); t += 1
            if kind == 'qrl':
                V[s] += alpha * (r + gamma * V[s2] * (not done) - V[s])
                L = int(min(max(0.0, k * (r + V[s2])), 3))   # number of Grover iterations (Dong et al. 2008), capped at 3
                # amplitude amplification of the chosen action a (Grover rotation about the uniform state)
                for _ in range(L):
                    v = amp[s].copy(); v[a] = -v[a]                    # oracle: flip chosen action
                    u = np.full(nA, 1 / np.sqrt(nA)); v = 2 * u * (u @ v) - v   # diffusion
                    amp[s] = v / np.linalg.norm(v)
                    if amp[s][a] ** 2 > 0.97: break
            else:
                target = r + (0 if done else gamma * Q[s2].max())
                Q[s, a] += alpha * (target - Q[s, a])
            s = s2
        steps_log.append(t)
    return np.array(steps_log)

def rl_experiment(seeds=30, episodes=300, noise_levels=(0.0, 0.5)):
    out = {}
    for noise in noise_levels:
        for kind in ('eps', 'softmax', 'qrl'):
            runs = np.array([run_agent(kind, s, episodes, noise) for s in range(seeds)])
            out[(kind, noise)] = runs
    return out

if __name__ == '__main__':
    import json
    res = dict(order=order_effect(), conj=conjunction(), interf=interference(),
               kalman=kalman_fusion(), qlbn=[qlbn_two_cues(theta_deg=t) for t in (60, 90, 120)],
               label=label_order())
    print(json.dumps(res, indent=1, default=float))
    import sys
    if '--rl' in sys.argv:                         # Table C1: about 5-10 minutes
        for (kind, noise), runs in rl_experiment().items():
            final = runs[:, -50:].mean(1)
            conv = []
            for r in runs:
                ma = np.convolve(r, np.ones(10) / 10, 'valid'); hit = np.flatnonzero(ma <= 15)
                if len(hit): conv.append(hit[0] + 10)
            print(f"{kind:8s} noise={noise}: final {final.mean():.1f} +- {final.std():.1f}; "
                  f"convergence {np.mean(conv):.0f} +- {np.std(conv):.0f} ({len(conv)}/30 seeds); "
                  f"total steps {runs.sum(1).mean():.0f}")
