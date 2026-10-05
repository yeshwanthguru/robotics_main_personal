"""Runs every experiment in order and then draws the figures.
Run from github/s/model:  python3 experiments/run_all.py
Environment variables: QLMODEL_REPS (repetitions per condition, default 50; the paper uses 30),
QLMODEL_WORKERS (parallel processes, default all cores)."""
import os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
for script in ['exp1_model_recovery.py', 'exp2_cross_order.py', 'exp3_planning.py', 'exp4_trust.py',
               'exp5_literature.py', 'exp6_circuits.py']:
    t = time.time(); print('==', script, flush=True)
    subprocess.run([sys.executable, script], cwd=HERE, check=True)
    print('   %.0f s' % (time.time() - t), flush=True)
subprocess.run([sys.executable, os.path.join(os.path.dirname(HERE), 'tools', 'make_figures.py')], check=True)
subprocess.run([sys.executable, os.path.join(os.path.dirname(HERE), 'tools', 'identifiability.py')], check=True)
