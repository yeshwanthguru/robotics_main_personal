"""Unit tests: run from github/s/model with  python3 -m pytest -q tests"""
import os, sys
import numpy as np
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.quantum_like import QLQuestionModel, qq_value, interference_total_probability
from qlmodel.classical import BayesJoint, Anchoring
from qlmodel.trust import MarkovTrust, OpenSystemTrust, final_trust
from qlmodel.fitting import fit, sample
from qlmodel.domains import DOMAINS, generator, ql_mean

RNG = np.random.default_rng(0)


@pytest.mark.parametrize('ranks', [(1, 1), (1, 2), (2, 1), (2, 2)])
def test_ql_probabilities_and_qq(ranks):
    for _ in range(20):
        m = QLQuestionModel(*RNG.uniform(0, np.pi, 3), ranks=ranks)
        ab, ba = m.cells('A', 'B'), m.cells('B', 'A')
        assert abs(ab.sum() - 1) < 1e-12 and abs(ba.sum() - 1) < 1e-12
        assert abs(qq_value(ab, ba)) < 1e-12
        assert abs(ab[:2].sum() - m.first_position('A')) < 1e-12


def test_bayes_has_no_order_effect():
    b = BayesJoint(0.4, 0.7, 0.3)
    ab, ba = b.cells('A', 'B'), b.cells('B', 'A')
    assert abs(ab[0] + ab[2] - (ba[0] + ba[1])) < 1e-12        # P(B yes) the same in both positions
    assert abs(qq_value(ab, ba)) < 1e-12


def test_anchoring_qq():
    assert abs(qq_value(Anchoring(0.5, 0.68, 0.4, 0.4).cells('A', 'B'), Anchoring(0.5, 0.68, 0.4, 0.4).cells('B', 'A'))) < 1e-12
    a = Anchoring(0.5, 0.68, 0.2, 0.5)
    assert abs(qq_value(a.cells('A', 'B'), a.cells('B', 'A'))) > 1e-3


def test_markov_query_has_no_effect_and_dephased_open_system_matches():
    out = [1, 1, 0, 1, 0, 1]
    m = MarkovTrust(0.6, 0.3, 0.4)
    assert abs(final_trust(m, out, {5}) - final_trust(m, out, {2, 5})) < 1e-12
    o = OpenSystemTrust(1.6, 0.8, 1.2, 1.0)                    # full dephasing: no coherence left
    assert abs(final_trust(o, out, {5}) - final_trust(o, out, {2, 5})) < 1e-12
    o = OpenSystemTrust(1.6, 0.8, 1.2, 0.3)
    assert abs(final_trust(o, out, {5}) - final_trust(o, out, {2, 5})) > 0.01


def test_interference_law():
    assert abs(interference_total_probability(0.97, 0.84, 0.5, np.pi / 2) - 0.905) < 1e-12


def test_fit_recovers_generating_model():
    m = ql_mean('object_clarification')
    data = {o: (2_000_000 * m.cells(o[0], o[1])).round() for o in ('AB', 'BA')}
    f = fit('QL', data, restarts=12, rng=np.random.default_rng(1))
    for o in ('AB', 'BA'):
        assert np.allclose(f['model'].cells(o[0], o[1]), m.cells(o[0], o[1]), atol=2e-3)


def test_generators_share_first_position_rates():
    for d in DOMAINS:
        q, a = generator(d, 'QL', sd=0), generator(d, 'Anchoring', sd=0)
        assert np.allclose(q.rates()[:2], a.rates()[:2], atol=0.01)


def test_circuits_match_analytic():
    pytest.importorskip('qiskit_aer')
    from qlmodel import circuits as C
    m = ql_mean('trust_handover')
    for form in ('dynamic', 'deferred'):
        counts, _ = C.run_aer(C.question_circuit(m, 'AB', form), shots=20000)
        assert 0.5 * np.abs(C.counts_to_cells(counts, m, 'AB') - m.cells('A', 'B')).sum() < 0.02
    o = OpenSystemTrust(1.6, 0.8, 1.2, 0.3)
    counts, _ = C.run_aer(C.trust_circuit(o, [1, 1, 0, 1, 0, 1], {2, 5}, 'dynamic'), shots=20000)
    assert abs(C.final_trust_from_counts(counts) - final_trust(o, [1, 1, 0, 1, 0, 1], {2, 5})) < 0.02
