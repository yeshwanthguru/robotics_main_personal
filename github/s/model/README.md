# Order-aware human models for robot questioning and trust

Code, simulation studies, quantum-circuit versions and manuscript of the model paper that accompanies
Survey 3 (`../`). Authors: Yeshwanth Guru and Dev Kunwar Singh Chauhan, Department of Mechanical
Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

## 1. What the model is, in plain terms

A robot that works with people has to ask them things: *Is it the red cup? Do you trust me to hand
you the knife? Is this trajectory acceptable?* People's answers depend on the order of the questions
(asking about Gore first changed how many people called Clinton honest in a 1997 Gallup poll), and
asking a question can change what the person thinks next. Classical (Bayesian) models of a person
assume that answers just read out fixed beliefs, so they cannot represent either effect.

The **quantum-like model** represents the person's state of mind as a vector and each question as a
projection; answering a question moves the state. This is ordinary linear algebra on an ordinary
computer: nothing quantum happens in the person or in the robot. It predicts order effects and a
specific regularity (the QQ equality) that some classical models break. The **open-system trust
model** applies the same idea to trust over a series of robot hand-overs and predicts that asking
about trust changes later trust; the Markov model predicts that it does not.

The project asks, by simulation and against published data: when can these models be told apart,
what does the robot gain by using them, and what does it lose if the model is wrong?

## 2. Folder contents

| Path | Contents |
|---|---|
| `qlmodel/quantum_like.py` | Three-dimensional real quantum-like question-order model (Lueders rule, projector ranks), QQ statistic, interference law |
| `qlmodel/classical.py` | Bayesian joint model (no order effect), anchoring model (one or two weights), saturated model |
| `qlmodel/trust.py` | Markov and open-system (Lindblad dephasing) trust dynamics with trust queries |
| `qlmodel/fitting.py` | Maximum-likelihood fitting, BIC, sampling, QQ test, KL divergence |
| `qlmodel/domains.py` | Three robot domains (object clarification, trust and hand-over, preference elicitation) and four synthetic human generators |
| `qlmodel/planner.py` | Questioning designs for recovering unprimed answer rates |
| `qlmodel/circuits.py` | Qiskit circuits (dynamic and deferred-measurement forms), Aer and Braket simulators |
| `experiments/exp1`–`exp6` | Model recovery, cross-order prediction, question planning, trust dynamics, published data, circuits |
| `experiments/literature_data.py` | The only human data used: Clinton–Gore poll (Moore 2002) and Prisoner's Dilemma (Shafir and Tversky 1992) aggregates |
| `cloud/ibm_runtime_run.py` | Runs the circuits on IBM Quantum hardware (Qiskit Runtime SamplerV2) |
| `cloud/braket_run.py` | Runs the circuits on Amazon Braket simulators or QPUs |
| `tests/` | Unit tests (`python3 -m pytest -q tests`) |
| `tools/` | Domain calibration, identifiability check, figure script, figure style |
| `results/` | JSON output of every experiment (the numbers quoted in the paper) |
| `paper/` | Manuscript (IEEEtran), bibliography, figures, PDF and Word versions |
| `PUBLICATION_PLAN.md` | Target venues, claims, steps to submission, proposed human study |

## 3. Installation

```
cd github/s/model
pip install -r requirements.txt
python3 -m pytest -q tests          # 11 tests, about 5 s
```

## 4. Reproducing the results

```
QLMODEL_REPS=30 python3 experiments/run_all.py     # all experiments, then figures (about 1 h on 4 cores)
python3 experiments/exp5_literature.py             # single experiment
python3 tools/make_figures.py                      # figures only, from results/*.json
cd paper && pdflatex main && bibtex main && pdflatex main && pdflatex main
```

All randomness is seeded; rerunning gives the same numbers.

## 5. How the circuits work

The belief space is embedded in two qubits; to ask a question, a rotation maps the question's
'yes' direction to |00>, an ancilla qubit is flipped if and only if the system is in |00>, the
ancilla is measured, and the rotation is undone. Only the ancilla is measured, so the state collapses
exactly as the Lueders rule requires. The trust circuit uses one qubit, rotations for robot outcomes
and an ancilla that applies Z with probability gamma/2 to implement dephasing. Each circuit has a
*dynamic* form (mid-circuit measurement and reset, for IBM hardware) and a *deferred* form (one
ancilla per measurement, read at the end, for hardware without mid-circuit measurement).

Results so far are **simulations only**: ideal Aer and Braket simulators, and Aer with the noise
models of the IBM FakeTorino and FakeBrisbane backends (`results/exp6_circuits.json`). No quantum
hardware has been used.

## 6. Running on real quantum hardware (cloud)

**IBM Quantum.** Create an account at quantum.cloud.ibm.com, copy the API key and instance, then
```
python3 -c "from qiskit_ibm_runtime import QiskitRuntimeService as S; S.save_account(channel='ibm_quantum_platform', token='<API key>', instance='<instance>')"
python3 cloud/ibm_runtime_run.py --dry-run                   # transpile only, nothing sent
python3 cloud/ibm_runtime_run.py --least-busy --shots 4000   # one job of 8 circuits
```

**Amazon Braket.** Enable Braket in the AWS console, run `aws configure`, then
```
python3 cloud/braket_run.py --dry-run                        # local simulator, no cost
python3 cloud/braket_run.py --device arn:aws:braket:::device/quantum-simulator/amazon/dm1 --shots 2000
python3 cloud/braket_run.py --device arn:aws:braket:us-east-1::device/qpu/ionq/Forte-1 --shots 1000
```
QPU runs are billed; check the current price list first. Results are written to `results/cloud/`
and can be added to Fig. 7 and Table V of the paper. Report hardware results exactly as measured,
with backend, date and job id.

Quantum hardware is not needed to use the model: the analytic version runs in microseconds on a
Raspberry Pi. The circuits are a test of the representation on quantum hardware, and a basis for
future work in which several human models are evaluated in superposition.

## 7. Connection to Survey 3

Survey 3 reviews how a resource-constrained robot can orchestrate several learning modalities on
calibrated confidence signals. This model provides one more signal: the predictive uncertainty of the
human model (how sure the robot is about what the person will answer or how much they trust it).
In Survey 3 it appears as the dashed fifth input of Fig. 1 and in Section XVII ("Human-model
uncertainty as an orchestration signal"). The trust experiment also bears on the orchestrator's
help-seeking decisions: if asking changes trust, asking is an action with a cost, not a free reading.

## 8. Results and conclusion

See `paper/main.tex` (Sections V–VII) and `results/`. A summary is in `RESULTS.md`.
