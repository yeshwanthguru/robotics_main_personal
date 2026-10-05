"""Trust dynamics over a sequence of robot outcomes, with optional trust queries.

MarkovTrust     two hidden states (trust, distrust); each outcome (1 success, 0 failure) applies a
                row-stochastic transition matrix; a query reads the state. Averaged over the
                answer, a query leaves the state distribution unchanged, so asking about trust
                cannot change later trust (law of total probability).
OpenSystemTrust a qubit density matrix; each outcome applies a rotation (toward trust after a
                success, away after a failure) followed by dephasing of strength gamma (a Lindblad
                channel). A query is a projective measurement in the trust basis, which removes
                coherence; with gamma < 1 a query therefore changes later trust (an interference,
                or question, effect). gamma = 1 removes all coherence and gives Markov-like behavior.
Both return the probability of a 'trust' answer at the final query, and the joint probability of
answers when intermediate queries are made."""
import numpy as np


class MarkovTrust:
    def __init__(self, p0, s_up, f_down):
        """p0 initial P(trust); after a success, distrust -> trust with prob s_up; after a
        failure, trust -> distrust with prob f_down."""
        self.p0, self.s_up, self.f_down = p0, s_up, f_down

    def step(self, p, outcome):
        return p + (1 - p) * self.s_up if outcome else p * (1 - self.f_down)

    def answer_probs(self, outcomes, query_after):
        """Joint probabilities of trust answers at the queries (indices into outcomes, answer
        recorded after that outcome). Returns {answers tuple: probability}."""
        out = {(): (1.0, self.p0)}
        for t, o in enumerate(outcomes):
            out = {k: (pr, self.step(p, o)) for k, (pr, p) in out.items()}
            if t in query_after:
                new = {}
                for k, (pr, p) in out.items():
                    new[k + (1,)] = (pr * p, 1.0)
                    new[k + (0,)] = (pr * (1 - p), 0.0)
                out = new
        return {k: pr for k, (pr, _) in out.items()}


class OpenSystemTrust:
    def __init__(self, phi0, a_s, a_f, gamma):
        """phi0 initial Bloch angle (P(trust) = cos^2(phi0/2)); a_s, a_f rotation angles after a
        success (toward trust) or failure (toward distrust); gamma in [0, 1] dephasing per step."""
        self.phi0, self.a_s, self.a_f, self.gamma = phi0, a_s, a_f, gamma

    @staticmethod
    def _ry(a):
        c, s = np.cos(a / 2), np.sin(a / 2)
        return np.array([[c, -s], [s, c]])

    def rho0(self):
        v = np.array([np.cos(self.phi0 / 2), np.sin(self.phi0 / 2)])   # |0> = trust
        return np.outer(v, v)

    def step(self, rho, outcome):
        U = self._ry(-self.a_s if outcome else self.a_f)
        rho = U @ rho @ U.T
        off = (1 - self.gamma)
        return np.array([[rho[0, 0], off * rho[0, 1]], [off * rho[1, 0], rho[1, 1]]])

    def answer_probs(self, outcomes, query_after):
        out = {(): (1.0, self.rho0())}
        for t, o in enumerate(outcomes):
            out = {k: (pr, self.step(r, o)) for k, (pr, r) in out.items()}
            if t in query_after:
                new = {}
                for k, (pr, r) in out.items():
                    pt = float(np.clip(r[0, 0], 0, 1))
                    new[k + (1,)] = (pr * pt, np.diag([1.0, 0.0]))
                    new[k + (0,)] = (pr * (1 - pt), np.diag([0.0, 1.0]))
                out = new
        return {k: pr for k, (pr, _) in out.items()}


def final_trust(model, outcomes, query_after):
    """P(trust answer at the last query), marginalised over earlier answers."""
    probs = model.answer_probs(outcomes, query_after)
    return sum(p for k, p in probs.items() if k[-1] == 1)
