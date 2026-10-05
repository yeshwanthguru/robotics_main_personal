"""Shared settings for the experiments. All data are simulated; no human data are used except the
published aggregate numbers in literature_data.py."""
import json, os
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, 'results')
os.makedirs(RES, exist_ok=True)
GENERATORS = ['QL', 'Bayes', 'Anchoring', 'Mixture']
CANDIDATES = ['QL', 'Bayes', 'Anchoring2']
WORKERS = int(os.environ.get('QLMODEL_WORKERS', os.cpu_count() or 1))
REPS = int(os.environ.get('QLMODEL_REPS', 50))


def save(name, obj):
    def conv(o):
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.floating,)): return float(o)
        if isinstance(o, np.ndarray): return o.tolist()
        raise TypeError(type(o))
    json.dump(obj, open(os.path.join(RES, name), 'w'), indent=1, default=conv)
    print('wrote results/' + name)


def seed(*args):
    """Deterministic seed from the arguments (Python's hash() of strings changes between runs)."""
    import zlib
    return zlib.crc32(repr(args).encode())
