# Online Continual Learning in Decentralized Robot Agents for Autonomous Self-Healing

**Local LLM-based coordination with sensor-fault adaptation on the LeKwik mobile manipulator**

Yeshwanth Guru Krishnakumar — PhD Research Proposal
Amrita University | Prepared August 2026

> **Citation caveat:** I don't have live search or a paper database in this session. Every reference below is from memory and should be verified (title, authors, venue, year) before it goes into a submitted document. Treat the reference list as a checklist to confirm, not as a verified bibliography.

---

# PART I — STATE OF THE ART

## 1. Scope and structure of the review

The thesis sits at the intersection of four literatures that have each matured independently but have never been combined into a single deployed system:

| Pillar | Question it answers | Maturity |
|---|---|---|
| **A. Runtime fault tolerance & self-adaptation in robotics** | How does a robot keep working when a component degrades? | Mature, mostly non-learning or offline-learned |
| **B. LLMs for robot reasoning, diagnosis, and replanning** | Can a language model explain and recover from failure? | Very active, but frozen weights |
| **C. On-device / edge LLM adaptation** | Can a small LLM be updated on embedded hardware? | Emerging, mostly NLP, not robotics |
| **D. Online continual learning** | Can a model learn during deployment without forgetting? | Mature theory, benchmark-bound |
| **E. Multi-agent / hierarchical LLM coordination** | Can multiple agents coordinate through a language model? | Active, task-level not subsystem-level |

The state of the art is reviewed pillar by pillar, then synthesised into an explicit gap matrix (§7).

---

## 2. Pillar A — Runtime fault tolerance and self-adaptation in robotics

### 2.1 Model- and ontology-based adaptation

The dominant engineering approach to runtime robot adaptation is **metacontrol**: a supervisory layer reasons over an explicit model of the system and reconfigures it when a constraint is violated.

- **MROS / Metacontrol for ROS** (Hernández Corbato, Bozhinoski, and colleagues, TU Delft / RobMoSys lineage) uses an OWL ontology (TOMASys) to describe components, function designs, and quality attributes. When a QA threshold is breached, the metacontroller selects an alternative configuration. It is the strongest available baseline for "runtime self-reconfiguration on a real ROS robot."
- **SkiROS2** (Rovida, Krueger et al.) provides a skill-based, semantically annotated task-planning layer that can re-plan when preconditions fail.
- **Runtime verification / monitoring** work (ROSMonitoring, RV-based safety envelopes) detects specification violations at runtime but does not itself repair.

**Common limitation.** These systems are *rule-complete but experience-blind*. Every recovery must be anticipated and encoded by the designer. There is no mechanism by which the system's recovery policy improves after the tenth occurrence of the same fault.

### 2.2 Learning-based adaptation, trained offline

- **Cully, Clune, Tarapore & Mouret (2015), "Robots that can adapt like animals," *Nature*.** The canonical damage-recovery result: a behaviour–performance map is generated offline (MAP-Elites), then a Bayesian-optimisation search over that map finds a compensating gait within minutes of damage. Adaptation is *search over a precomputed archive*, not learning — the archive itself never changes.
- **Kumar, Fu, Pathak & Malik (2021), "RMA: Rapid Motor Adaptation for Legged Robots," RSS.** A base policy plus an adaptation module that infers environment extrinsics from proprioceptive history. Fast, robust, deployed — but the adaptation module's weights are frozen at deployment; adaptation is inference over a latent variable.
- **Miki, Lee, Hwangbo, Wellhausen, Koltun & Hutter (2022), "Learning robust perceptive locomotion for quadrupedal robots in the wild," *Science Robotics*.** The strongest sensor-fault-tolerance baseline: an attention-based belief encoder learns, in simulation, when to trust exteroception versus fall back on proprioception. Handles degraded/misleading perception gracefully. Crucially, the fallback behaviour is **learned offline and frozen** — a novel sensor failure mode outside the training distribution has no path to being learned in the field.
- **Classical FDI/FTC** (fault detection, isolation and reconfiguration; analytical redundancy, Kalman-bank residual methods, sliding-mode observers) remains the control-theoretic backbone: rigorous, provable, and dependent on an accurate a-priori fault model.

### 2.3 What Pillar A establishes

Self-healing behaviour on real robots is achievable today, by one of three routes: (i) hand-authored reconfiguration rules, (ii) offline-precomputed behaviour archives, (iii) offline-trained robust policies. **None of the three updates its own parameters during deployment.** The system's competence at time *t* equals its competence at deployment.

---

## 3. Pillar B — LLMs for robot reasoning, diagnosis, and replanning

### 3.1 Language-model planning and grounding

- **SayCan** (Ahn et al., 2022) — grounds LLM proposals in learned affordance value functions.
- **Inner Monologue** (Huang et al., 2022) — closes the loop with textual feedback (success detectors, scene descriptions, human input), letting the LLM replan after failure.
- **Code as Policies** (Liang et al., 2022) and **ProgPrompt** (Singh et al., 2022) — the LLM emits executable policy code rather than symbolic plans.

### 3.2 Failure explanation and recovery specifically

- **REFLECT** (Liu et al., 2023) — builds a hierarchical multisensory summary of the robot's experience and queries an LLM to explain *why* a task failed, then generates a corrective plan. This is the closest existing work to "LLM as diagnostic layer."
- **DoReMi** (Guo et al., 2023) — the LLM emits constraints alongside the plan; a vision-language model detects violations at execution time and triggers recovery.
- **AutoGPT-style agentic loops** and **ReAct**-style interleaved reasoning/acting provide the general control pattern that robotics has adopted.

### 3.3 Vision-language-action models

**RT-2** (Brohan et al., 2023), **OpenVLA** (Kim et al., 2024), **TinyVLA**, **π0** (Physical Intelligence, 2024) and **RoboCat** (Bousmalis et al., 2023) map observations directly to actions with large pretrained backbones. RoboCat notably self-improves — but through *offline* fine-tuning rounds on collected data, not online during a deployment episode.

### 3.4 What Pillar B establishes — and its shared blind spot

LLMs are demonstrably good at (i) explaining failures from heterogeneous sensor evidence and (ii) proposing structured recoveries. But across essentially the entire literature:

- the model is **frozen** — it is a fixed reasoning oracle;
- it is typically **cloud-hosted** (GPT-4-class), introducing latency, cost, and connectivity dependence incompatible with a 200 ms control budget;
- it reasons at the **task level** ("the object was not grasped"), not the **subsystem-health level** ("the wrist force sensor's bias has drifted 0.4 N over 30 minutes").

---

## 4. Pillar C — On-device and edge LLM adaptation

- **Parameter-efficient fine-tuning:** LoRA (Hu et al., 2021) and QLoRA (Dettmers et al., 2023) reduce the trainable-parameter count by 3–4 orders of magnitude, making gradient updates feasible in single-digit GB of VRAM.
- **Small capable models:** Phi-2 / Phi-3 (Microsoft), TinyLlama, Gemma-2B, Qwen-small — the 1–3 B parameter class that fits and runs on a Jetson Orin at usable token rates.
- **Quantisation and serving:** GPTQ, AWQ, llama.cpp, TensorRT-LLM, MLC — mature for *inference*.
- **On-device training:** work such as POET and the tinyML training literature establishes that backward passes on embedded accelerators are viable under memory-planning constraints; MobileLLM addresses sub-billion architecture design for on-device use.

**What Pillar C establishes.** The engineering prerequisites for updating a small LLM's weights on embedded hardware exist. **But the edge-LLM literature is almost entirely inference-oriented, and almost entirely non-robotic** — the demonstrated use case is on-device chat/assistant personalisation, not closed-loop control of a physical system.

---

## 5. Pillar D — Online continual learning

- **Catastrophic forgetting** (McCloskey & Cohen, 1989; French, 1999) is the core obstacle.
- **Regularisation approaches:** EWC (Kirkpatrick et al., 2017), SI, MAS — penalise movement of parameters important to prior tasks.
- **Replay approaches:** Experience Replay, DER/DER++ (Buzzega et al., 2020), GEM / A-GEM (Lopez-Paz & Ranzato; Chaudhry et al.) — the empirically strongest family, and the one most compatible with a small on-robot buffer.
- **Online / streaming CL:** the "online" setting (single pass, no task boundaries) is the realistic one for robots; CLEAR, CORe50 and Stream-51 are the standard benchmarks.
- **PEFT-based continual learning:** O-LoRA, InfLoRA, LoRA-subspace methods — recent work showing that constraining sequential LoRA updates to orthogonal subspaces mitigates forgetting. This is the most directly transferable line of work for this thesis.
- **Lifelong learning in robotics:** LIBERO (Liu et al., 2023) as a benchmark; various lifelong-manipulation studies.

**What Pillar D establishes.** The algorithms for learning-without-forgetting are mature and well-characterised — **on curated, i.i.d.-shuffled, offline benchmark streams**. They have rarely been stress-tested where the data stream is generated by the agent's own degrading body, in real time, with a safety-critical closed loop attached.

---

## 6. Pillar E — Multi-agent and hierarchical LLM coordination

- **General multi-agent LLM frameworks:** CAMEL, AutoGen (Microsoft), MetaGPT, ChatDev — role-specialised LLM agents negotiating in natural language.
- **Robotics-specific:** **RoCo** (Mandi, Jain & Song, 2023) — dialectic multi-robot collaboration via LLM dialogue; **SMART-LLM** — LLM-driven multi-robot task decomposition and allocation; **Co-NavGPT** — multi-robot exploration coordination.
- **Classical decentralised robot architectures:** subsumption (Brooks), behaviour trees (Colledanchise & Ögren), blackboard architectures, and the ROS 2 lifecycle/diagnostics stack (`diagnostic_aggregator`) — decentralised monitoring exists, but reports to a human or to a fixed rule set.

**What Pillar E establishes.** LLM-mediated coordination between agents is well demonstrated, but the agents are almost always **task-level peers** ("robot A fetches, robot B holds"). No mainstream work instantiates agents as **subsystem health monitors of a single robot** (arm, base, gripper) reporting upward to a local coordinating LLM that both arbitrates and *learns* from their reports.

---

## 7. Synthesis — the gap matrix

| System / line of work | On-device LLM | Weight updates at deployment | Online continual learning | Hierarchical multi-agent coordination | Sensor-fault adaptation | Real hardware |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| MROS / metacontrol | — | — | — | partial (supervisory) | ✓ (rule-based) | ✓ |
| Cully et al. 2015 | — | — | — | — | ✓ (damage) | ✓ |
| RMA (2021) | — | — | — | — | partial | ✓ |
| Miki et al. 2022 | — | — | — | — | ✓ (offline-learned) | ✓ |
| REFLECT / DoReMi | — | — | — | — | partial | ✓ |
| OpenVLA / TinyVLA | ✓ | — | — | — | — | ✓ |
| RoboCat | — | offline rounds | — | — | — | ✓ |
| RoCo / SMART-LLM | — | — | — | ✓ | — | partial |
| O-LoRA / DER++ / EWC | — | ✓ | ✓ | — | — | — (benchmarks) |
| **This thesis** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

**The novelty claim is the row, not any single column.** Each individual capability exists somewhere. The four-way combination — *on-device LLM weight updates + online continual learning + hierarchical multi-agent subsystem coordination + sensor-fault adaptation*, validated on a real mobile manipulator — has not been published together.

---

## 8. Open problems the SOTA does not resolve

1. **The frozen-oracle problem.** Every LLM-for-robotics system treats the language model as a fixed reasoner. A fault mode outside its pretraining is never learned, only re-explained.
2. **The offline-adaptation ceiling.** Robust fault tolerance (Miki et al.) is bought with simulation-time training; the field has no accepted method for a robot to *acquire a new compensation strategy in the field*.
3. **Stability–plasticity under embodied streams.** Continual-learning guarantees are benchmark-derived; behaviour under a self-generated, non-stationary, safety-coupled stream is largely unmeasured.
4. **Latency and connectivity.** Cloud LLM diagnosis is incompatible with real-time recovery; on-device diagnosis with *learning* is unexplored.
5. **Granularity of agency.** Multi-agent LLM work coordinates robots, not the subsystems within a robot — losing the natural locality of fault detection.

---

# PART II — MEETING PRESENTATION

**Format:** 10 slides, ~15 minutes plus discussion. Covers the seven required sections.

---

## Slide 1 — Title

**ONLINE CONTINUAL LEARNING IN DECENTRALIZED ROBOT AGENTS FOR AUTONOMOUS SELF-HEALING**

Local LLM-based coordination with sensor-fault adaptation on the LeKwik mobile manipulator

Yeshwanth Guru Krishnakumar · PhD Research Proposal · Amrita University

*Speaker note:* One-line framing — "The robot doesn't just detect that a sensor has failed; it learns, on board and in real time, how to work around it."

---

## Slide 2 — Academic and professional background

| | |
|---|---|
| **Doctoral study** | PhD candidate, cognitive robotics, Amrita University |
| **Master's thesis** | IIT Genoa — DIBRIS / TheEngineRoom (Mastrogiovanni, Lanza, Solinas). Quantum-like cognitive architecture for human–robot handover, implemented on TIAGo++ |
| **Current roles** | Research Fellow, Italian Institute of Technology (humanoid and wearable robotics); Technical Product Manager, Jio Platforms |
| **Experience** | ~7 years in robotics — ROS 1/ROS 2, mobile manipulation, learning-based control, deployment engineering |
| **Continuity** | Master's work established cognitive decision-making under uncertainty on a mobile manipulator; this PhD replaces the fixed decision layer with one that *learns on-device during deployment* |

*Speaker note:* Emphasise the TIAGo++ handover work as direct evidence of prior competence on exactly this class of platform and task.

---

## Slide 3 — Proposed research area

**Platform.** LeKwik (LeRobot ecosystem) — low-cost holonomic mobile base + 5-DoF arm with Feetech servos + gripper. Compute: Jetson Orin.

**Core system.**
- Decentralised agents — **ARM**, **BASE**, **GRIPPER** — each monitoring its own subsystem's sensor and actuator state locally.
- A **local small LLM** (Phi-2 or TinyLlama) running on the Jetson, receiving structured agent reports, arbitrating between them, and issuing recovery decisions.
- **Online continual learning:** LoRA adapters updated during deployment, stabilised by a replay buffer — no cloud, no offline retraining loop, no human in the recovery path.

**Target behaviour.** When a sensor degrades or fails mid-task, the system detects it locally, forms a compensation strategy, executes it, and *retains* what it learned for the next occurrence.

**Tasks.** Human–robot handover, fetch-and-place, multi-item delivery.

---

## Slide 4 — Preliminary literature review

Four pillars, one gap in each:

| Pillar | Representative work | Limitation |
|---|---|---|
| Runtime self-adaptation | MROS / metacontrol, SkiROS2 | Ontology-driven; rule-complete but experience-blind — no learning |
| Learned fault tolerance | Cully 2015 (*Nature*), RMA 2021, Miki 2022 (*Science Robotics*) | Adaptation policy trained **offline** and frozen at deployment |
| LLMs for robot reasoning | REFLECT, DoReMi, Inner Monologue, SayCan | LLM is **frozen** and typically **cloud-hosted**; task-level, not subsystem-level |
| Edge LLMs + continual learning | OpenVLA, TinyVLA; LoRA/QLoRA; EWC, DER++, O-LoRA | Edge work is **inference-only**; CL results are **benchmark-bound**, not embodied |
| Multi-agent LLM coordination | RoCo, SMART-LLM, AutoGen | Agents are **task-level peers**, not subsystem health monitors |

*Speaker note:* The honest framing to the committee — every ingredient is individually well-studied. That is a strength: it means each design choice has a defensible precedent. The contribution is the integration and its validation.

---

## Slide 5 — Identified research gap

**What is missing.**
1. No published system updates LLM weights *during deployment* on a real robot.
2. No hierarchical multi-agent LLM coordination at the **subsystem-health** level of a single platform.
3. No online-learned **sensor-fault compensation** — existing robustness is offline-trained.
4. All four capabilities together, on real hardware: **never published.**

**Gap statement.**
> Robots today either follow pre-authored recovery rules or execute robustness policies fixed at training time. Neither acquires new compensation strategies from its own operational experience. Consequently a robot's fault-handling competence is bounded at deployment and never improves.

**Why now.** Sub-3B models that fit on a Jetson, LoRA making on-device gradient updates tractable, and mature replay-based CL methods have only recently coincided. The combination was not implementable three years ago.

---

## Slide 6 — Tentative objectives

| | Objective | Success criterion |
|---|---|---|
| **O1** | Implement decentralised subsystem agents (ARM, BASE, GRIPPER) producing structured health reports on LeKwik under ROS 2 | Agents detect injected faults with quantified detection latency and false-positive rate |
| **O2** | Deploy and characterise a local small LLM (Phi-2 / TinyLlama) on Jetson Orin as the coordinating layer | End-to-end decision latency within the real-time control budget (target < 200 ms) |
| **O3** | Enable online LoRA weight updates with a replay buffer during deployment | Measurable improvement in recovery success across repeated exposures to the same fault |
| **O4** | Demonstrate no catastrophic forgetting under the embodied stream | Retained performance on earlier fault types and on nominal task execution after new-fault adaptation |
| **O5** | Show hierarchical LLM coordination outperforms a rule-based arbiter | Head-to-head against a hand-authored / MROS-style baseline on identical fault sequences |
| **O6** | Validate on real hardware with human subjects | 50 trials on physical LeKwik, handover and fetch-and-place tasks |
| **O7** | Demonstrate generalisation beyond the training tasks | Transfer to 2–3 unseen tasks without retraining from scratch |

---

## Slide 7 — Proposed methodology

**Architecture — three layers**

1. **Agent layer (decentralised).** Per-subsystem monitors on ARM, BASE, GRIPPER. Each maintains local residual/anomaly signals and emits a compact structured report (subsystem, signal, deviation, confidence).
2. **Coordination layer (local LLM).** Phi-2 / TinyLlama on Jetson Orin consumes agent reports plus task context, arbitrates conflicting reports, and emits a recovery decision (re-parameterise, substitute a sensing modality, degrade gracefully, abort).
3. **Learning layer (online CL).** Outcomes of executed recoveries feed a replay buffer; LoRA adapters are updated online with replay-based stabilisation. Update cadence and safety gating are explicit design parameters.

**Experimental phases**

| Phase | Environment | Scale | Purpose |
|---|---|---|---|
| **1** | Gazebo + ROS 2, systematic sensor-fault injection | ~30 trials | Ablations, safety envelope, hyperparameter selection |
| **2** | Physical LeKwik, human subjects | ~50 trials | Real-hardware validation of the full loop |
| **3** | 2–3 unseen tasks | — | Generalisation / transfer |

**Baselines**
- **MROS / metacontrol** — ontology-based reconfiguration, no learning.
- **Frozen cloud LLM** — REFLECT / DoReMi-style diagnosis with a fixed model.
- **Offline-trained sensor FTC** — Miki et al. 2022-style robust policy, frozen at deployment.

**Metrics.** Recovery success rate; time-to-recovery; recovery success versus number of prior exposures (the learning curve — the central evidence); retention on prior faults and nominal tasks (forgetting); on-device decision latency; task success under fault versus nominal.

**Ablations.** With/without online updates; with/without replay; LLM coordinator versus rule-based arbiter; decentralised agents versus single centralised monitor.

---

## Slide 8 — Expected outcomes and contributions

1. **First demonstration of on-device LLM weight updates during robot deployment** — a robot whose reasoning layer improves in the field, not between field trials.
2. **A decentralised subsystem-agent architecture** for mobile manipulators, with an LLM coordination layer that outperforms rule-based arbitration.
3. **Online sensor-fault self-healing** — empirically characterised learning curves showing compensation strategies acquired in real time.
4. **Continual-learning evidence in an embodied setting** — quantified stability–plasticity behaviour under a self-generated, non-stationary stream, rather than a curated benchmark.
5. **An open, reproducible validation stack** on a low-cost LeRobot-ecosystem platform — deliberately chosen so results are replicable outside well-funded labs.

**Publication plan (12 months).**

| Paper | Content | Target venue |
|---|---|---|
| 1 | Architecture + simulation validation (Phase 1) | ICRA |
| 2 | Full system + real-hardware human-subject validation (Phase 2) | *Science Robotics* |
| 3 | Generalisation and transfer (Phase 3) | IEEE RA-L |

---

## Slide 9 — Risks and mitigations

| Risk | Mitigation |
|---|---|
| On-device update latency exceeds the control budget | Decouple update cadence from the control loop — asynchronous adaptation with safety gating; fall back to inference-only mode under load |
| Catastrophic forgetting degrades nominal performance | Replay buffer + orthogonal-subspace LoRA constraints (O-LoRA-style); forgetting is a measured outcome, not an assumption |
| Online learning produces an unsafe recovery | Hard safety envelope outside the learned layer; learned decisions constrained to a validated action set |
| Human-subject trials slip on ethics approval | Phase 1 simulation results stand as an independent publishable unit; begin approval process immediately |
| Hardware failure on a low-cost platform | Feetech servos are cheap and replaceable; keep spares and a Gazebo digital twin |

---

## Slide 10 — Closing statement

> **Decentralised subsystem agents, coordinated by a local LLM that updates its own weights online, allow a mobile manipulator to acquire sensor-fault compensation strategies in real time — turning fault tolerance from a fixed property set at deployment into a capability that improves with experience.**

**Scope discipline:** one platform (LeKwik), one problem (sensor-fault self-healing), one architecture, three validation phases. The quantum-cognition track remains a separate parallel line, scheduled for integration in Phases 4–5 — not part of this thesis's critical path.

**Applications:** service and assistive robotics, warehouse mobile manipulation, human–robot collaboration, search and rescue — any setting where a robot must keep working without a technician.

---

# APPENDIX

## A. Technical stack

| Layer | Choice |
|---|---|
| Platform | LeKwik (LeRobot) — holonomic base, 5-DoF arm, Feetech servos |
| Middleware | ROS 2 |
| Simulation | Gazebo (primary, Phase 1); Isaac Sim available for higher-fidelity perception |
| On-device compute | NVIDIA Jetson Orin |
| Language model | Phi-2 (primary) / TinyLlama (fallback for tighter latency) |
| Adaptation | LoRA / QLoRA adapters, replay buffer, PEFT stack |
| Baseline implementations | MROS (metacontrol), REFLECT/DoReMi-style frozen-LLM diagnosis, offline-trained FTC policy |

## B. Reference checklist (verify all before submission)

**Fault tolerance and adaptation**
- Cully, Clune, Tarapore, Mouret (2015). Robots that can adapt like animals. *Nature*.
- Kumar, Fu, Pathak, Malik (2021). RMA: Rapid Motor Adaptation for Legged Robots. *RSS*.
- Miki, Lee, Hwangbo, Wellhausen, Koltun, Hutter (2022). Learning robust perceptive locomotion for quadrupedal robots in the wild. *Science Robotics*.
- Hernández Corbato, Bozhinoski et al. MROS / metacontrol for ROS (TOMASys ontology).
- Rovida, Krueger et al. SkiROS2.
- Colledanchise & Ögren. *Behavior Trees in Robotics and AI*.

**LLMs for robotics**
- Ahn et al. (2022). Do As I Can, Not As I Say (SayCan).
- Huang et al. (2022). Inner Monologue.
- Liang et al. (2022). Code as Policies.
- Singh et al. (2022). ProgPrompt.
- Liu et al. (2023). REFLECT.
- Guo et al. (2023). DoReMi.
- Brohan et al. (2023). RT-2. / Kim et al. (2024). OpenVLA. / TinyVLA. / π0.
- Bousmalis et al. (2023). RoboCat.
- Mandi, Jain, Song (2023). RoCo. / SMART-LLM.

**Efficient adaptation and continual learning**
- Hu et al. (2021). LoRA. / Dettmers et al. (2023). QLoRA.
- Kirkpatrick et al. (2017). EWC (*PNAS*).
- Buzzega et al. (2020). DER++.
- Lopez-Paz & Ranzato (2017). GEM. / Chaudhry et al. A-GEM.
- O-LoRA / InfLoRA (orthogonal-subspace continual LoRA).
- Liu et al. (2023). LIBERO (lifelong robot-learning benchmark).
- McCloskey & Cohen (1989); French (1999) — catastrophic forgetting.

## C. Anticipated committee questions

1. *Why an LLM rather than a smaller learned controller?* — The coordination layer must fuse heterogeneous, symbolically-described subsystem reports and produce structured decisions; that is a language-shaped problem. Justify with an ablation against a non-LLM arbiter (O5).
2. *Isn't online weight updating unsafe?* — Learned decisions are constrained to a pre-validated action set behind a hard safety envelope; the learning layer selects among safe options, it does not author new low-level control.
3. *How do you know it's learning and not just retrieving?* — The learning curve (recovery success versus number of prior exposures) plus held-out novel fault modes distinguishes the two.
4. *Is 50 hardware trials enough?* — Power-analysis justification, plus the 30-trial simulation study for effect-size estimation.
5. *Where did the quantum work go?* — Parallel secondary track, Phases 4–5, off the critical path. Committee-approved separation.
