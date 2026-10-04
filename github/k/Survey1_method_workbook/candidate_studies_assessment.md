# Survey 1: candidate studies found after the main search

Status: **pending supervisor decision.** Nothing here has been added to the manuscript, the
extraction table, the supplement, the figures, or the counts. Full texts are in
`Survey1_fulltexts/candidates/include/` and `Survey1_fulltexts/candidates/exclude/` (private).

Assessed October 2026 against the protocol's criteria (I1–I3, E1–E4), evidence levels (L1–L6),
quantum-execution tag, and appraisal items Q1–Q7 (M = met, P = partly met, N = not met).

## 1. Summary

| # | Study | Decision | Level | Execution |
|---|---|---|---|---|
| 1 | Eker et al. 2026, QANTIS | Include (borderline) | L3 | QPU (IBM Heron) |
| 2 | Cunha et al. 2025, QBRL | Include | L2 | Simulated |
| 3 | Liu 2025, parallel QAOA grid path planning | Include (weak) | L2 | Simulated |
| 4 | Santos et al. 2025, QG-PSO inverse kinematics | Include (strong fit) | L2 | Simulated |
| 5 | Ho and Hoorn 2022, Q-Coppélia | Include (borderline) | L1 | None (design only) |
| 6 | Efe et al. 2026, Ising acceleration | Exclude: not quantum (CMOS Ising chips) | – | – |
| 7 | Gandhudi et al. 2026, QAQL for remaining useful life | Exclude: I1, no robot | – | – |
| 8 | Kong et al. 2026, UAV swarm quantum annealing | Exclude: E2, Chinese full text | – | – |
| 9 | van der Meer et al. 2025, quantum-like trust dynamics | Exclude: I1, no robot | – | – |
| 10 | Tang et al. 2024, CIM for AGV scheduling | Not assessed: full text needed | – | – |
| 11 | Liu et al. 2020, drone-based entanglement distribution | Not assessed: full text needed | – | – |
| 12 | NV-centre magnetometers for GPS-denied UAV control (preprint) | Not assessed: full text needed | – | – |

Also checked and **already in the corpus**: Otani2025, Lokossou2025, Innan2025 (the gradings in
`extraction_table.csv` match the papers).

Still to check: the JNEP 2025 AMR task-allocation paper and candidates 10–12 (Section 5).

## 2. Included candidates

### 2.1 Eker et al. 2026, QANTIS
- **Reference:** B. Y. Eker, S. S. Arslan, Ö. Nazlı, M. S. Demirgil, F. Deligöz. "QANTIS: A Hardware-Validated
  Quantum Platform for POMDP Planning and Multi-Target Data Association." arXiv:2603.00785, 2026 (preprint).
- **What it does:** quantum belief update (Grover amplitude amplification, BIQAE) for POMDP planning
  and QUBO data association (FPC-QAOA). 45 experiments on three IBM Heron backends. One Grover
  iterate raised a rare-observation probability from 0.179 to 0.907 while preserving the posterior,
  and they ran a closed-loop Tiger POMDP on hardware. The authors claim no wall-clock advantage.
- **Why borderline:** the robotics link is autonomous navigation and target tracking (simulated UAV
  tracking); the hardware runs use the Tiger toy problem.
- **Appraisal:** Q1 P, Q2 M, Q3 N, Q4 M, Q5 P, Q6 M (github.com/neuraparse/qantis), Q7 M.
- **Where:** Section 6.2, "Real-time control" paragraph, after Sun2025; add a row to the hardware
  table in Section 11.2.
- **Draft text:** "Eker et al. (2026) ran quantum belief updates for POMDP planning on IBM Heron
  processors: one Grover iterate raised a rare observation's probability from 0.18 to 0.91 without
  distorting the posterior, and a Tiger POMDP was closed in the loop on hardware. The authors
  present this as a check of the mechanism at toy scale, not as a speed-up."

### 2.2 Cunha et al. 2025, QBRL
- **Reference:** G. Cunha, A. Ramôa, A. Sequeira, M. de Oliveira, L. Barbosa. "Quantum Bayesian Networks
  Can Speed up Reinforcement Learning in Partially Observable Environments." arXiv:2507.18606v2, 2026 (preprint).
- **What it does:** model-based look-ahead RL with quantum rejection sampling for belief updates;
  sub-quadratic speed-up for sparse Bayesian-network dynamics under fault-tolerant assumptions,
  and no speed-up when fully observable or dense. Benchmarked in simulation (Tiger and a small
  room-navigation robot task).
- **Where:** Section 6.2, end of the "Navigation and control" paragraph.
- **Draft text:** "Cunha et al. (2025) showed that quantum rejection sampling can speed up belief
  updates in model-based RL for partially observable tasks, but only when the environment's
  Bayesian network is sparse; their simulated benchmarks on small navigation tasks show the size of
  the gain depends strongly on the setting."

### 2.3 Liu 2025, parallel QAOA grid path planning
- **Reference:** J. Liu. "Quantum Grid Path Planning Using Parallel QAOA Circuits Based on Minimum
  Energy Principle." arXiv:2510.07413, 2025 (preprint).
- **What it does:** grid path planning mapped to a minimum-energy state; two parallel QAOA circuits,
  12 qubits, simulated in PennyLane. No classical baseline (Q2 N).
- **Where:** Section 5.2, "Motion Planning and Swarm Planning", after Chella2022.
- **Draft text:** "Liu (2025) mapped grid path planning to a minimum-energy problem solved by two
  parallel QAOA circuits; the 12-qubit simulations find valid paths but are not compared with any
  classical planner."

### 2.4 Santos et al. 2025, QG-PSO inverse kinematics
- **Reference:** D. O. Santos, F. M. de Assis, E. A. N. Carvalho, L. Molina. "A Grover-Operator-Based
  Quantum Variant of Particle Swarm Optimization for Robot Manipulators' Inverse Kinematics: Theory
  and Simulation." IEEE Access, 2025. doi:10.1109/ACCESS.2025.3628560
- **What it does:** Grover-operator-based PSO for inverse kinematics; simulated on 7- and 15-joint
  manipulators; 3.4–5.1× fewer forward-kinematics calls. The oracle uses prior knowledge of the solution region.
- **Appraisal:** Q1 M, Q2 P, Q3 P, Q4 N, Q5 P, Q6 M (github.com/GPRUFS/Quantum-Grover-PSO), Q7 M.
- **Where:** Section 4.3, "Kinematics", after the Otani2025 sentence.
- **Draft text:** "Santos et al. (2025) built a Grover-operator variant of particle swarm
  optimization for inverse kinematics; in simulation on 7- and 15-joint arms it needed 3.4 to 5.1
  times fewer forward-kinematics evaluations, although its oracle assumes prior knowledge of where
  the solution lies."

### 2.5 Ho and Hoorn 2022, Q-Coppélia
- **Reference:** J. K. W. Ho, J. F. Hoorn. "Quantum affective processes for multidimensional
  decision-making." Scientific Reports 12, 20468 (2022). doi:10.1038/s41598-022-22855-0
- **What it does:** translates the fuzzy Silicon Coppélia model of a robot's attitude towards its
  user into full quantum circuits. No simulation or hardware run; the authors call it a theoretical
  exercise because of the qubit count. Data on request; no code.
- **Appraisal:** Q2 P (conceptual comparison with the fuzzy system only), Q3 N, Q6 N; limitations partly stated.
- **Where:** Section 9.2, right after the Yan2021 sentence.
- **Draft text:** "Ho and Hoorn (2022) translated the fuzzy Silicon Coppélia model of a robot's
  developing attitude towards its user into a full quantum circuit (Q-Coppélia), using superposition
  for mixed affective states and entanglement for weighting factors. Like Yan2021 it is a design
  only: the authors note that the qubit count makes even simulation impractical."
- **Note:** this is a 2022 journal paper inside the search window that the query strings did not
  find (no "affective" term). Worth mentioning in Threats to Validity.

## 3. Excluded candidates

- **Efe et al. 2026** (arXiv:2608.06803), "Ising Acceleration for Multi-Robot Multi-Target
  Planning": CMOS Ising machines, neither quantum nor quantum-inspired. Optional supporting citation
  for I3.
- **Gandhudi et al. 2026** (arXiv:2606.18503), "Quantum Annealing Enhanced Reinforcement Learning
  for Accurate Remaining Useful Lifetime Prediction": D-Wave annealer inside Q-learning, but for
  turbofan and device prognostics; no robot. Optional supporting citation in Section 6.2.
- **Kong et al. 2026**, "Quantum Annealing Algorithm for Solving Unmanned Aerial Vehicle Swarm
  Trajectory Planning Problem", Computer Engineering 52(3), doi:10.19678/j.issn.1000-3428.0069959:
  in scope, but the full text is Chinese (E2). Quantum annealing beat simulated annealing on mean
  route length (193.1 vs 208.3 over 500 runs). Mention as a language-exclusion example.
- **van der Meer et al. 2025** (arXiv:2504.13918), "Modeling the quantum-like dynamics of human
  reliability ratings in Human-AI interactions by interaction dependent Hamiltonians": human–AI
  trust, no robot. Optional supporting citation in Section 9.2 next to Widdows2023.

## 4. What changes if all five inclusions are accepted

| Item | Now | After |
|---|---|---|
| Primary studies | 72 | 77 |
| Graded (non-review) studies | 65 | 70 |
| L1 / L2 / L3 / L4 / L5 / L6 | 6 / 19 / 23 / 10 / 6 / 1 | 7 / 22 / 24 / 10 / 6 / 1 |
| QPU studies | 22 | 23 |
| refs.bib entries | 185 | 190 |
| Keys cited in main paper | 173 | 178 (180 with two optional supporting citations) |

Places to update: abstract, Table 1, Contributions, Section 3.4 (PRISMA counts), Section 11.2
(text, evidence figure, hardware table), levels table, Conclusion, Data Availability, Tables S1/S5,
`extraction_table.csv` (both copies), the Word master copy, and the Zenodo package. Keep the PDF at
35 pages or fewer.

## 5. Candidates from the authors' literature database (added 4 October 2026)

Found by comparing the authors' reading database with `refs.bib`: on topic for Survey 1 but never
cited, and no full text in the repository, so they cannot be graded yet. Download them, then assess
them with the same criteria as Sections 2–3.

| # | Reference (from the database; details to be confirmed) | Likely fit | What to check |
|---|---|---|---|
| 10 | Tang et al. 2024, "Quantum computing for several AGV scheduling models", *Scientific Reports* 14, 12205 | Fleets and AGVs (Section 4); coherent Ising machine, so quantum-inspired hardware rather than a QPU | Whether the CIM counts as quantum execution under our tags; reported ~92% time saving on small instances only |
| 11 | Liu, H.-Y. et al. 2020, "Drone-based entanglement distribution towards mobile quantum networks", *National Science Review* | Quantum communication between robots; precursor of `Liu2021` (PRL 2021, already L5) | Whether it adds evidence beyond `Liu2021` or is cited only as background |
| 12 | "NV-centre magnetometers for GPS-denied UAV control", Research Square preprint, 2025 (authors unknown) | Quantum navigation sensors, next to `Wang2023` | Authors and whether it has been peer reviewed (flag it as a preprint) |

Also from the database: Lawless 2020 ("Quantum-like interdependence theory advances A-HMTs") belongs
to Survey 2 (cited there as `Lawless2020`); it is not a Survey 1 candidate.

If candidates 10–12 were all included as primary studies, the primary, graded and refs.bib counts in
Section 4 would each rise by 3 more; the level counts depend on their assessment.
The database corrections and the 43 missing rows are in `Survey1_database_update.csv`.
