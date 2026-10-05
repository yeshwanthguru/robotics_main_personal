"""Quantum-circuit versions of the question-order model and the open-system trust model.

The quantum-like models run on ordinary computers; the circuits show that the same probabilities
come out of quantum hardware, and how much hardware noise distorts them. Two forms are built:

  dynamic   mid-circuit measurement and reset (IBM Quantum hardware and Aer support these);
  deferred  every measurement is copied to a fresh ancilla with CNOT or Toffoli gates and read at the
            end (deferred-measurement principle); this runs on hardware without mid-circuit
            measurement, such as the ion-trap devices on Amazon Braket.

Question-order circuit. The three-dimensional belief space is embedded in two system qubits
(e1 = |00>, e2 = |01>, e3 = |10>; |11> is never populated). To ask question q, an orthogonal
unitary V_q maps u_q to |00>; an ancilla is flipped if and only if the system is in |00> and is
measured (a binary Lueders measurement: the system is not measured, so the 'no' subspace is not
collapsed further); then V_q^T rotates back. A rank-2 'yes' subspace reads the ancilla inverted.

Trust circuit. One system qubit (|0> = trust). After each robot outcome an RY rotation is applied,
then dephasing of strength gamma is implemented by applying Z with probability gamma/2 through an
ancilla (RY on the ancilla, CZ, reset). A trust query measures the system qubit."""
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import UnitaryGate


# ------------------------------------------------------------------ helpers
def rotation_to_e1(u):
    """4x4 real orthogonal matrix acting on span(|00>,|01>,|10>) with V u = |00>, identity on |11>."""
    u = np.asarray(u, float); u = u / np.linalg.norm(u)
    # Householder reflection H with H u = e1 (or identity if u == e1); then embed in 4x4.
    e1 = np.array([1.0, 0.0, 0.0])
    v = u - e1
    H = np.eye(3) if np.linalg.norm(v) < 1e-12 else np.eye(3) - 2 * np.outer(v, v) / (v @ v)
    V = np.eye(4); idx = [0, 1, 2]   # basis order of Qiskit little-endian: index = q1*2 + q0
    for i, a in enumerate(idx):
        for j, b in enumerate(idx):
            V[a, b] = H[i, j]
    return V   # H is symmetric and orthogonal, so V^T = V


def _embed_index():
    # e1 -> |00> (index 0), e2 -> |01> (q0 = 1, index 1), e3 -> |10> (q1 = 1, index 2)
    return [0, 1, 2]


# ------------------------------------------------------------------ question-order circuits
def question_circuit(model, order, form='dynamic'):
    """Circuit asking the questions in `order` (e.g. 'AB') of a QLQuestionModel.
    Classical bit i holds the ancilla reading for the i-th question (1 = system was in u_q)."""
    sys_ = QuantumRegister(2, 'sys')
    n_anc = 1 if form == 'dynamic' else len(order)
    anc = QuantumRegister(n_anc, 'anc')
    c = ClassicalRegister(len(order), 'ans')
    qc = QuantumCircuit(sys_, anc, c)
    # psi = e1 = |00>: nothing to prepare
    for i, q in enumerate(order):
        V = UnitaryGate(rotation_to_e1(model.u(q)), label='V_%s' % q)
        a = anc[0] if form == 'dynamic' else anc[i]
        qc.append(V, [sys_[0], sys_[1]])
        qc.x(sys_[0]); qc.x(sys_[1]); qc.ccx(sys_[0], sys_[1], a); qc.x(sys_[0]); qc.x(sys_[1])
        if form == 'dynamic':
            qc.measure(a, c[i]); qc.reset(a)
        qc.append(V, [sys_[0], sys_[1]])          # V is its own inverse (Householder)
    if form == 'deferred':
        for i in range(len(order)): qc.measure(anc[i], c[i])
    return qc


def counts_to_cells(counts, model, order):
    """Convert bitstring counts to the answer cells [yy, yn, ny, nn] of the order."""
    tot = sum(counts.values()); cells = np.zeros(4)
    for bits, n in counts.items():
        b = bits.replace(' ', '')[::-1]          # Qiskit prints the highest classical bit first
        ans = []
        for i, q in enumerate(order):
            hit = int(b[i])
            ans.append(hit if model.ranks[q] == 1 else 1 - hit)
        cells[(1 - ans[0]) * 2 + (1 - ans[1])] += n
    return cells / tot


# ------------------------------------------------------------------ trust circuit
def trust_circuit(model, outcomes, query_after, form='dynamic'):
    """Circuit for an OpenSystemTrust model: rotations for outcomes, dephasing, trust queries.
    Classical bit k holds the k-th query answer (0 = trust)."""
    s = QuantumRegister(1, 'sys')
    nq = len(query_after)
    if form == 'dynamic':
        anc = QuantumRegister(1, 'deph'); qa = None
    else:
        anc = QuantumRegister(len(outcomes), 'deph'); qa = QuantumRegister(nq, 'query')
    c = ClassicalRegister(nq, 'ans')
    qc = QuantumCircuit(s, anc, c) if qa is None else QuantumCircuit(s, anc, qa, c)
    qc.ry(model.phi0, s[0])
    theta = 2 * np.arcsin(np.sqrt(model.gamma / 2))       # P(ancilla = 1) = gamma / 2
    k = 0
    for t, o in enumerate(outcomes):
        qc.ry(-model.a_s if o else model.a_f, s[0])
        a = anc[0] if form == 'dynamic' else anc[t]
        if model.gamma > 0:
            qc.ry(theta, a); qc.cz(a, s[0])
            if form == 'dynamic': qc.reset(a)
        if t in query_after:
            if form == 'dynamic':
                qc.measure(s[0], c[k])
            else:
                qc.cx(s[0], qa[k])
            k += 1
    if form == 'deferred':
        for j in range(nq): qc.measure(qa[j], c[j])
    return qc


def final_trust_from_counts(counts):
    tot = sum(counts.values()); trust = 0
    for bits, n in counts.items():
        if bits.replace(' ', '')[0] == '0': trust += n      # highest classical bit = last query
    return trust / tot


# ------------------------------------------------------------------ simulators
def run_aer(qc, shots=20000, noise_backend=None, seed=7):
    """Run on Qiskit Aer, ideal or with the noise model of a fake IBM backend (e.g. 'FakeTorino')."""
    from qiskit import transpile
    from qiskit_aer import AerSimulator
    if noise_backend is None:
        sim = AerSimulator(seed_simulator=seed)
        tq = transpile(qc, sim, optimization_level=1, seed_transpiler=seed)
    else:
        from qiskit_ibm_runtime import fake_provider
        backend = getattr(fake_provider, noise_backend)()
        sim = AerSimulator.from_backend(backend, seed_simulator=seed)
        tq = transpile(qc, backend, optimization_level=3, seed_transpiler=seed)
    res = sim.run(tq, shots=shots).result()
    return res.get_counts(), dict(depth=tq.depth(), two_qubit_gates=int(sum(v for k, v in tq.count_ops().items() if k in ('cx', 'ecr', 'cz'))))


def braket_question_circuit(model, order):
    """Deferred-measurement question circuit in Amazon Braket form (qubits 0, 1 system; 2.. ancillas)."""
    from braket.circuits import Circuit
    circ = Circuit()
    for i, q in enumerate(order):
        V = rotation_to_e1(model.u(q))
        # Braket's unitary uses big-endian target order; Qiskit index = q1*2 + q0, so target [1, 0]
        circ.unitary(matrix=V, targets=[1, 0])
        a = 2 + i
        circ.x(0).x(1).ccnot(0, 1, a).x(0).x(1)
        circ.unitary(matrix=V, targets=[1, 0])
    return circ


def braket_counts_to_cells(counts, model, order):
    tot = sum(counts.values()); cells = np.zeros(4)
    for bits, n in counts.items():
        ans = []
        for i, q in enumerate(order):
            hit = int(bits[2 + i])                  # Braket bitstrings are in qubit order 0, 1, 2, ...
            ans.append(hit if model.ranks[q] == 1 else 1 - hit)
        cells[(1 - ans[0]) * 2 + (1 - ans[1])] += n
    return cells / tot


def run_braket_local(circ, shots=20000, depolarizing=0.0):
    """Run on the Braket local simulator (state vector, or density matrix with depolarizing noise
    after every gate)."""
    from braket.devices import LocalSimulator
    from braket.circuits import Noise
    if depolarizing > 0:
        circ = circ.copy(); circ.apply_gate_noise(Noise.Depolarizing(probability=depolarizing))
        dev = LocalSimulator('braket_dm')
    else:
        dev = LocalSimulator()
    return dict(dev.run(circ, shots=shots).result().measurement_counts)
