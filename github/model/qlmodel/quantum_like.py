"""Projective (quantum-like) model of answers to a sequence of yes/no questions.

The respondent's belief is a unit vector psi in a real three-dimensional space. The 'yes' answer to
question q is a projector P_q onto either the ray of a unit vector u_q (rank 1) or the plane
orthogonal to it (rank 2). Answering applies the Lueders rule:
    p(yes) = ||P_q psi||^2,   psi <- P_q psi / ||P_q psi||   (and the complement for 'no').
Up to a rotation, the model has three parameters, the angles between psi, u_A and u_B:
    psi = e1,  u_A = (cos a, sin a, 0),  u_B = (cos b, sin b cos g, sin b sin g).
plus the rank (1 or 2) of each question's 'yes' subspace, a discrete structural choice. A
two-dimensional model has only two effective parameters and cannot change the second-position rate
of B when half the respondents answer A with 'yes', which the Clinton-Gore poll requires. For any parameters the four answer pairs in order AB and BA satisfy
the QQ equality  p_AB(y,n) + p_AB(n,y) = p_BA(y,n) + p_BA(n,y)  (Wang and Busemeyer, 2013)."""
import numpy as np


class QLQuestionModel:
    """Three-dimensional real quantum-like model with angles (a, b, g) and ranks (rank_A, rank_B)."""
    def __init__(self, a, b, g=0.0, ranks=(1, 1)):
        self.a, self.b, self.g = float(a), float(b), float(g)
        self.ranks = {'A': int(ranks[0]), 'B': int(ranks[1])}

    @property
    def psi(self):
        return np.array([1.0, 0.0, 0.0])

    def u(self, q):
        if q == 'A': return np.array([np.cos(self.a), np.sin(self.a), 0.0])
        return np.array([np.cos(self.b), np.sin(self.b) * np.cos(self.g), np.sin(self.b) * np.sin(self.g)])

    def projector(self, q):
        u = self.u(q); P = np.outer(u, u)
        return P if self.ranks[q] == 1 else np.eye(3) - P

    def answer_probs(self, order, psi=None):
        """Probabilities of all answer sequences {(a1, a2, ...): p}, a = 1 yes, 0 no."""
        out = {(): (1.0, self.psi if psi is None else psi)}
        for q in order:
            P = self.projector(q); Q = np.eye(3) - P
            new = {}
            for seq, (p, v) in out.items():
                for ans, M in ((1, P), (0, Q)):
                    w = M @ v; pw = float(w @ w)
                    new[seq + (ans,)] = (p * pw, w / np.sqrt(pw) if pw > 1e-15 else w)
            out = new
        return {k: p for k, (p, _) in out.items()}

    def first_position(self, q):
        v = self.projector(q) @ self.psi
        return float(v @ v)

    def cells(self, first, second):
        """Cell probabilities [yy, yn, ny, nn] for the order (first, second)."""
        p = self.answer_probs((first, second))
        return np.array([p[(1, 1)], p[(1, 0)], p[(0, 1)], p[(0, 0)]])


def qq_value(cells_ab, cells_ba):
    """QQ statistic [p_AB(yn)+p_AB(ny)] - [p_BA(yn)+p_BA(ny)]; zero under the projective model.
    cells_ba are indexed by the answer to B first, then A."""
    return (cells_ab[1] + cells_ab[2]) - (cells_ba[1] + cells_ba[2])


def interference_total_probability(p1, p2, c, phase):
    """Quantum-like law of total probability with an interference term (disjunction effect):
    p = c p1 + (1-c) p2 + 2 cos(phase) sqrt(c p1 (1-c) p2)."""
    return c * p1 + (1 - c) * p2 + 2 * np.cos(phase) * np.sqrt(c * p1 * (1 - c) * p2)
