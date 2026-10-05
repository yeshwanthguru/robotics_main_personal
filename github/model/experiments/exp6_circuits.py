"""Experiment 6: the models as quantum circuits, on simulators with and without hardware noise.
For each domain the question-order circuit is run in both orders, and the trust circuit in both
query conditions, on: Qiskit Aer (ideal); Aer with the noise model of the IBM fake backends
FakeTorino (Heron r1) and FakeBrisbane (Eagle r3), dynamic and deferred forms; and the Amazon Braket
local simulators (ideal state vector; density matrix with depolarizing noise of 0.5% and 2% after
every gate, deferred form). Scores: total variation distance (TVD) between circuit and analytic
answer distributions, and the QQ value estimated from the circuit output (zero for the exact model).
No quantum hardware is used here; cloud/ has the scripts for IBM Quantum and Amazon Braket.
Output: results/exp6_circuits.json"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qlmodel.domains import DOMAINS, ql_mean
from qlmodel.quantum_like import qq_value
from qlmodel.trust import OpenSystemTrust, final_trust
from qlmodel import circuits as C
from common import save
from exp4_trust import TRUE_OS, OUT, C0, C1

SHOTS = 20000
tvd = lambda p, q: 0.5 * float(np.abs(np.asarray(p) - np.asarray(q)).sum())
res = {'shots': SHOTS, 'questions': {}, 'trust': {}}
for d in DOMAINS:
    m = ql_mean(d); r = {}
    exact = {o: m.cells(o[0], o[1]) for o in ('AB', 'BA')}
    runs = {}
    for label, kw, form in [('Aer ideal', {}, 'dynamic'), ('Aer FakeTorino dynamic', {'noise_backend': 'FakeTorino'}, 'dynamic'),
                            ('Aer FakeTorino deferred', {'noise_backend': 'FakeTorino'}, 'deferred'),
                            ('Aer FakeBrisbane dynamic', {'noise_backend': 'FakeBrisbane'}, 'dynamic')]:
        cells, info = {}, {}
        for o in ('AB', 'BA'):
            cnt, inf = C.run_aer(C.question_circuit(m, o, form), shots=SHOTS, **kw)
            cells[o] = C.counts_to_cells(cnt, m, o); info[o] = inf
        runs[label] = (cells, info)
    for label, dep in [('Braket ideal', 0.0), ('Braket depolarizing 0.5%', 0.005), ('Braket depolarizing 2%', 0.02)]:
        cells = {o: C.braket_counts_to_cells(C.run_braket_local(C.braket_question_circuit(m, o), shots=SHOTS, depolarizing=dep), m, o) for o in ('AB', 'BA')}
        runs[label] = (cells, {})
    for label, (cells, info) in runs.items():
        r[label] = dict(tvd_AB=tvd(cells['AB'], exact['AB']), tvd_BA=tvd(cells['BA'], exact['BA']),
                        qq=float(qq_value(cells['AB'], cells['BA'])), cells_AB=cells['AB'], cells_BA=cells['BA'], transpiled=info)
        print(d, label, round(r[label]['tvd_AB'], 4), round(r[label]['tvd_BA'], 4), 'QQ', round(r[label]['qq'], 4))
    r['exact'] = dict(cells_AB=exact['AB'], cells_BA=exact['BA'])
    res['questions'][d] = r

T = OpenSystemTrust(*TRUE_OS)
for label, kw, form in [('Aer ideal', {}, 'dynamic'), ('Aer FakeTorino dynamic', {'noise_backend': 'FakeTorino'}, 'dynamic'),
                        ('Aer FakeTorino deferred', {'noise_backend': 'FakeTorino'}, 'deferred')]:
    f = {}
    for name, q in (('C0', C0), ('C1', C1)):
        cnt, inf = C.run_aer(C.trust_circuit(T, OUT, q, form), shots=SHOTS, **kw)
        f[name] = C.final_trust_from_counts(cnt)
    res['trust'][label] = dict(final_C0=f['C0'], final_C1=f['C1'], query_effect=f['C1'] - f['C0'])
    print('trust', label, {k: round(v, 3) for k, v in res['trust'][label].items()})
res['trust']['exact'] = dict(final_C0=final_trust(T, OUT, C0), final_C1=final_trust(T, OUT, C1))
res['trust']['exact']['query_effect'] = res['trust']['exact']['final_C1'] - res['trust']['exact']['final_C0']
save('exp6_circuits.json', res)
