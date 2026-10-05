"""Classical baselines for two yes/no questions asked in either order.

BayesJoint       one joint distribution p(a, b), the same in both orders (no order effect);
Anchoring        first answer given at its first-position rate; the second answer is pulled toward
                 the first by a weight that depends on the second question (w_A, w_B; assimilation
                 if positive, contrast if negative). With w_A = w_B it satisfies the QQ equality;
                 with w_A != w_B it does not;
Saturated        a free joint distribution for each order (6 free parameters; upper reference).
Symmetric response noise added to BayesJoint (a binary-response analogue of the probability-theory-
plus-noise account) produces another order-free joint distribution, so it stays inside BayesJoint.
All return cell probabilities [yy, yn, ny, nn] for an ordered pair (first, second)."""
import numpy as np


def _sig(x): return 1 / (1 + np.exp(-x))


class BayesJoint:
    def __init__(self, pA, pB, rho):
        """pA, pB marginals; rho in (-1, 1) scales the covariance between its feasible bounds."""
        self.pA, self.pB, self.rho = pA, pB, rho

    def joint(self):
        pA, pB = self.pA, self.pB
        lo, hi = max(0.0, pA + pB - 1) - pA * pB, min(pA, pB) - pA * pB
        cov = self.rho * (hi if self.rho > 0 else -lo)
        yy = pA * pB + cov
        return {'yy': yy, 'yn': pA - yy, 'ny': pB - yy, 'nn': 1 - pA - pB + yy}

    def cells(self, first, second):
        j = self.joint()
        if first == 'A': return np.array([j['yy'], j['yn'], j['ny'], j['nn']])
        return np.array([j['yy'], j['ny'], j['yn'], j['nn']])


class Anchoring:
    def __init__(self, pA, pB, wA, wB):
        self.p = {'A': pA, 'B': pB}; self.w = {'A': wA, 'B': wB}

    def cells(self, first, second):
        p1, p2, w = self.p[first], self.p[second], self.w[second]
        if w >= 0:
            y2_given_y, y2_given_n = p2 + w * (1 - p2), p2 - w * p2
        else:
            y2_given_y, y2_given_n = p2 + w * p2, p2 - w * (1 - p2)
        return np.array([p1 * y2_given_y, p1 * (1 - y2_given_y), (1 - p1) * y2_given_n, (1 - p1) * (1 - y2_given_n)])


class Saturated:
    def __init__(self, cells_ab, cells_ba):
        self.c = {'AB': np.asarray(cells_ab), 'BA': np.asarray(cells_ba)}

    def cells(self, first, second):
        return self.c[first + second]
