"""Run the question-order and trust circuits on IBM Quantum hardware (Qiskit Runtime, SamplerV2).

Prerequisites
  pip install -r ../requirements.txt
  An IBM Quantum Platform account and API key. Save it once:
    python3 -c "from qiskit_ibm_runtime import QiskitRuntimeService as S; S.save_account(channel='ibm_quantum_platform', token='<API key>', instance='<CRN or instance name>')"

Usage (from github/s/model)
  python3 cloud/ibm_runtime_run.py --dry-run                 # build and transpile only; no job is sent
  python3 cloud/ibm_runtime_run.py --backend ibm_torino --shots 4000
  python3 cloud/ibm_runtime_run.py --least-busy --shots 4000 --domains object_clarification

The script submits one SamplerV2 job containing the question circuits (both orders, every chosen
domain) and the two trust circuits, waits for it, and writes results/cloud/ibm_<backend>_<job id>.json
with the counts, the answer cells, the total variation distance to the analytic model and the QQ
value. The dynamic (mid-circuit measurement) form is used; IBM backends support it. Each circuit
uses 3 (questions) or 2 (trust) qubits. Check the remaining time of the account before running: a
run with 8 circuits of 4000 shots takes a few seconds of QPU time."""
import argparse, json, os, sys, datetime
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, 'experiments'))
from qlmodel.domains import DOMAINS, ql_mean
from qlmodel.quantum_like import qq_value
from qlmodel.trust import OpenSystemTrust, final_trust
from qlmodel import circuits as C
from exp4_trust import TRUE_OS, OUT, C0, C1


def build(domains):
    jobs = []
    for d in domains:
        m = ql_mean(d)
        for o in ('AB', 'BA'):
            jobs.append(dict(kind='question', domain=d, order=o, circuit=C.question_circuit(m, o, 'dynamic'), model=m))
    T = OpenSystemTrust(*TRUE_OS)
    for name, q in (('C0', C0), ('C1', C1)):
        jobs.append(dict(kind='trust', condition=name, circuit=C.trust_circuit(T, OUT, q, 'dynamic'), model=T, query=q))
    return jobs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--backend'); ap.add_argument('--least-busy', action='store_true')
    ap.add_argument('--shots', type=int, default=4000); ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--domains', nargs='*', default=list(DOMAINS))
    a = ap.parse_args()
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    jobs = build(a.domains)
    if a.dry_run:
        from qiskit_ibm_runtime.fake_provider import FakeTorino
        backend = FakeTorino()
    else:
        from qiskit_ibm_runtime import QiskitRuntimeService
        service = QiskitRuntimeService()
        backend = service.least_busy(operational=True, simulator=False) if a.least_busy else service.backend(a.backend)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=3)
    isa = [pm.run(j['circuit']) for j in jobs]
    for j, c in zip(jobs, isa):
        print(j['kind'], j.get('domain', j.get('condition')), j.get('order', ''), 'depth', c.depth(), 'ops', dict(c.count_ops()))
    if a.dry_run:
        print('dry run on', backend.name, '- no job submitted'); return
    from qiskit_ibm_runtime import SamplerV2
    sampler = SamplerV2(mode=backend)
    job = sampler.run(isa, shots=a.shots)
    print('submitted job', job.job_id(), 'on', backend.name); res = job.result()
    out = dict(backend=backend.name, job_id=job.job_id(), shots=a.shots, date=datetime.datetime.utcnow().isoformat(), circuits=[])
    for j, r in zip(jobs, res):
        counts = r.data.ans.get_counts()
        rec = dict(kind=j['kind'], counts=counts)
        if j['kind'] == 'question':
            cells = C.counts_to_cells(counts, j['model'], j['order']); exact = j['model'].cells(j['order'][0], j['order'][1])
            rec.update(domain=j['domain'], order=j['order'], cells=cells.tolist(), exact=exact.tolist(), tvd=0.5 * float(np.abs(cells - exact).sum()))
        else:
            rec.update(condition=j['condition'], final_trust=C.final_trust_from_counts(counts), exact=final_trust(j['model'], OUT, j['query']))
        out['circuits'].append(rec)
    for d in a.domains:
        cab = next(c['cells'] for c in out['circuits'] if c.get('domain') == d and c['order'] == 'AB')
        cba = next(c['cells'] for c in out['circuits'] if c.get('domain') == d and c['order'] == 'BA')
        out.setdefault('qq', {})[d] = float(qq_value(np.array(cab), np.array(cba)))
    os.makedirs(os.path.join(ROOT, 'results', 'cloud'), exist_ok=True)
    path = os.path.join(ROOT, 'results', 'cloud', 'ibm_%s_%s.json' % (backend.name, job.job_id()))
    json.dump(out, open(path, 'w'), indent=1); print('wrote', path)


if __name__ == '__main__':
    main()
