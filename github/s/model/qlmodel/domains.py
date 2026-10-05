"""The three robot domains of the experiments. Each domain fixes a pair of yes/no questions that a
robot asks a person and the population parameters of four synthetic 'human' generators:
  QL          two-dimensional quantum-like model (satisfies the QQ equality);
  Bayes       order-free joint distribution matched to the QL model's A-first cells;
  Anchoring   first-position rates of the QL model, order effect from unequal anchoring weights
              (violates the QQ equality);
  Mixture     half the population QL, half anchoring.
QL and Anchoring share the same first- and second-position rates; Bayes reproduces the
A-first joint distribution of QL without an order effect. Individual differences: each simulated
person draws its own parameters around the population values;
population cell probabilities are averages over 2,000 such persons. The parameter values are
illustrative choices, not estimates from human data."""
import numpy as np
from .quantum_like import QLQuestionModel
from .classical import BayesJoint, Anchoring

# Population parameters from tools/calibrate_domains.py (targets: first- and second-position 'yes' rates).
DOMAINS = {
    'object_clarification': dict(
        label='Object clarification', A='Is it the red cup?', B='Is it the cup on the left?',
        ql=(2.3543, 0.9676, 0.5846), ranks=(1, 2), anchoring=(0.3889, 0.4444)),
    'trust_handover': dict(
        label='Trust and hand-over', A='Do you trust the robot to hand you the tool?', B='Was the last hand-over safe?',
        ql=(0.6602, 2.0304, 0.6955), ranks=(1, 2), anchoring=(0.3333, 0.2778)),
    'preference_elicitation': dict(
        label='Preference elicitation', A='Is trajectory 1 acceptable?', B='Is trajectory 2 acceptable?',
        ql=(0.7371, 0.9047, 2.3389), ranks=(1, 2), anchoring=(-0.3115, 0.0)),
}
SD = 0.10   # spread of individual parameters (radians for QL, logit or weight units for the others)


class Population:
    """Average of individual models; exposes cells(first, second) like the individual models."""
    def __init__(self, members):
        self.members = members

    def cells(self, first, second):
        return np.mean([m.cells(first, second) for m in self.members], axis=0)

    def first_position(self, q):
        return float(np.mean([m.cells(q, 'B' if q == 'A' else 'A')[:2].sum() for m in self.members]))

    def rates(self):
        ab, ba = self.cells('A', 'B'), self.cells('B', 'A')
        return np.array([ab[0] + ab[1], ba[0] + ba[1], ba[0] + ba[2], ab[0] + ab[2]])


def ql_mean(domain):
    return QLQuestionModel(*DOMAINS[domain]['ql'], ranks=DOMAINS[domain]['ranks'])


def generator(domain, kind, n=2000, seed=0, sd=SD):
    rng = np.random.default_rng(seed)
    if sd == 0: n = 2          # identical members; two so that the mixture has one of each
    SD_ = sd
    a, b, g = DOMAINS[domain]['ql']; ranks = DOMAINS[domain]['ranks']
    ql = [QLQuestionModel(a + rng.normal(0, SD_), b + rng.normal(0, SD_), g + rng.normal(0, SD_), ranks) for _ in range(n)]
    if kind == 'QL':
        return Population(ql)
    m = ql_mean(domain)
    pA, pB = m.first_position('A'), m.first_position('B')
    logit = lambda p: np.log(p / (1 - p)); from scipy.special import expit as sig
    if kind == 'Bayes':
        ab = Population(ql).cells('A', 'B'); pA_, pB_ = ab[0] + ab[1], ab[0] + ab[2]
        lo, hi = max(0, pA_ + pB_ - 1) - pA_ * pB_, min(pA_, pB_) - pA_ * pB_
        cov = ab[0] - pA_ * pB_; rho = cov / hi if cov > 0 else -cov / lo
        return Population([BayesJoint(sig(logit(pA_) + rng.normal(0, SD_)), sig(logit(pB_) + rng.normal(0, SD_)), rho) for _ in range(n)])
    wA, wB = DOMAINS[domain]['anchoring']
    anc = [Anchoring(sig(logit(pA) + rng.normal(0, SD_)), sig(logit(pB) + rng.normal(0, SD_)),
                     np.clip(wA + rng.normal(0, SD_ / 2), -0.95, 0.95), np.clip(wB + rng.normal(0, SD_ / 2), -0.95, 0.95)) for _ in range(n)]
    if kind == 'Anchoring':
        return Population(anc)
    if kind == 'Mixture':
        return Population(ql[: n // 2] + anc[: n // 2])
    raise ValueError(kind)
