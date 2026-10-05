"""Run the question-order circuits on Amazon Braket (managed simulators or QPUs).

Prerequisites
  pip install -r ../requirements.txt
  An AWS account with Amazon Braket enabled, credentials configured (aws configure), and an S3
  bucket in the device's region for results (Braket creates amazon-braket-<region>-<account> by default).

Usage (from github/s/model)
  python3 cloud/braket_run.py --dry-run                                   # local simulator only, no cost
  python3 cloud/braket_run.py --device arn:aws:braket:::device/quantum-simulator/amazon/dm1 --shots 2000
  python3 cloud/braket_run.py --device arn:aws:braket:us-east-1::device/qpu/ionq/Forte-1 --shots 1000

The deferred-measurement form is used (one ancilla per question, read at the end), so the circuits
run on devices without mid-circuit measurement. Each question circuit uses 4 qubits. QPU tasks are
billed per task and per shot; check current Braket pricing before running on a QPU. Results go to
results/cloud/braket_<device>_<date>.json with cells, total variation distance and QQ value."""
import argparse, json, os, sys, datetime
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from qlmodel.domains import DOMAINS, ql_mean
from qlmodel.quantum_like import qq_value
from qlmodel import circuits as C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--device'); ap.add_argument('--shots', type=int, default=1000)
    ap.add_argument('--dry-run', action='store_true'); ap.add_argument('--domains', nargs='*', default=list(DOMAINS))
    a = ap.parse_args()
    if a.dry_run:
        from braket.devices import LocalSimulator
        dev, name = LocalSimulator(), 'local'
    else:
        from braket.aws import AwsDevice
        dev = AwsDevice(a.device); name = dev.name
        print('device', dev.name, 'status', dev.status)
    out = dict(device=name, shots=a.shots, date=datetime.datetime.utcnow().isoformat(), circuits=[], qq={})
    for d in a.domains:
        m = ql_mean(d); cells = {}
        for o in ('AB', 'BA'):
            circ = C.braket_question_circuit(m, o)
            task = dev.run(circ, shots=a.shots)
            counts = dict(task.result().measurement_counts)
            cells[o] = C.braket_counts_to_cells(counts, m, o); exact = m.cells(o[0], o[1])
            rec = dict(domain=d, order=o, counts=counts, cells=cells[o].tolist(), exact=exact.tolist(),
                       tvd=0.5 * float(np.abs(cells[o] - exact).sum()), task_id=getattr(task, 'id', 'local'))
            out['circuits'].append(rec); print(d, o, 'TVD', round(rec['tvd'], 4))
        out['qq'][d] = float(qq_value(cells['AB'], cells['BA']))
    os.makedirs(os.path.join(ROOT, 'results', 'cloud'), exist_ok=True)
    path = os.path.join(ROOT, 'results', 'cloud', 'braket_%s_%s.json' % (name.replace(' ', '_'), datetime.date.today().isoformat()))
    json.dump(out, open(path, 'w'), indent=1); print('wrote', path)


if __name__ == '__main__':
    main()
