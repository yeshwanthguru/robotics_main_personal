# OSF registration text — Survey 1 (retrospective)

Paste each section into the matching field of the OSF "Generalized Systematic Review Registration"
form (or into a single description field if you use "Open-Ended Registration").

---

**Title**
Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints — review protocol

**Authors**
Yeshwanth Guru (ORCID 0009-0007-6353-4033); Dev Kunwar Singh Chauhan (ORCID 0000-0002-1466-4567).
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

**Registration timing (state this honestly)**
This protocol is registered retrospectively, after the review was completed (corpus closed in
October 2026). It records the methods as they were applied, so that readers can check the review
against them.

**Type of review**
Systematic review of the literature in computing and robotics, reported following PRISMA 2020
where it applies.

**Research questions**
- RQ1. Which quantum methods have been applied to which robotic functions (optimization and planning;
  learning, including quantum machine learning and reinforcement learning; sensing and communication;
  and decision-making and reasoning)?
- RQ2. What level of evidence supports each application, from theoretical analysis to end-to-end
  deployment on physical robots?
- RQ3. Which reported benefits are genuinely quantum, and which come from quantum-inspired classical
  algorithms or are removed by dequantization?
- RQ4. Which hardware and deployment constraints (qubit counts, noise, latency, quantum-classical
  communication, size, weight, power, and cooling) limit quantum computing in robotics today?
- RQ5. Which directions offer realistic benefit by 2030, and what is needed beyond?

**Information sources**
IEEE Xplore, ACM Digital Library, Scopus, Web of Science, SpringerLink, ScienceDirect, arXiv
(quant-ph, cs.RO, cs.LG); backward and forward reference chasing from key papers and earlier
surveys; targeted searches in application areas where quantum-robotics work appears outside
robotics venues. Coverage: 1982 to October 2026.

**Search strings**
- Core: ("quantum computing" OR "quantum algorithm*" OR "quantum annealing" OR QAOA OR "variational
  quantum" OR "quantum machine learning" OR "quantum reinforcement learning" OR "quantum-inspired" OR
  "quantum sensing" OR "quantum cognition" OR "quantum probability") AND (robot* OR "autonomous
  vehicle*" OR "mobile robot*" OR swarm OR UAV OR AGV OR manipulator) AND (planning OR navigation OR
  localization OR "path planning" OR "task allocation" OR routing OR control OR learning OR
  "decision making" OR SLAM OR kinematics)
- Foundations: ("quantum computing" OR "quantum algorithm*") AND (review OR survey OR tutorial) AND
  (NISQ OR "error mitigation" OR "barren plateau*" OR "fault-tolerant" OR dequantiz*)
- Targeted: drones and UAVs, multi-agent and autonomous mobility, autonomous driving, control
  benchmarks (cart-pole), automated storage and retrieval — each combined with the quantum block.

**Eligibility criteria**
Include: (I1) proposes, evaluates, or reviews a quantum or quantum-inspired method applied to a
robotic function [primary studies]; (I2) foundational algorithms, hardware, or theory; (I3) classical
robotics baselines [I2/I3 = foundational works, not graded].
Exclude: (E1) "quantum" used only metaphorically; (E2) not in English; (E3) duplicate or earlier
version (most complete version kept); (E4) quantum communication without a robotic application.

**Selection process**
Title/abstract screening, then full-text assessment against the criteria, by the first author.
Record counts per stage were not logged.

**Data extraction**
Robotic task, quantum method and type, hardware or simulator, setup and baselines, key results,
stated and unstated limitations — by the first author; reviewed by the second author, with
disagreements resolved by discussion.

**Evidence grading**
Six ordered levels: L1 argued (theory), L2 simulated, L3 executed on quantum hardware, L4 coupled to
a robot or robot simulator in a closed loop, L5 demonstrated on a physical robot or vehicle,
L6 deployed end to end with a measured advantage over a classical baseline. Each study also carries a
quantum-execution tag: none / simulated / QPU / quantum sensor or link hardware / classical
(quantum-inspired).

**Quality appraisal**
Seven criteria (problem formulation, classical baseline, experimental realism, hardware and noise
reporting, performance metrics, reproducibility, critical discussion), each judged not met / partly
met / met; not summed into a score.

**Synthesis**
Narrative synthesis structured by a robotics-function taxonomy; cross-tabulation of evidence level
by execution tag; latency analysis; worked fault-tolerant resource estimate for one representative
algorithm. No meta-analysis (heterogeneous tasks, metrics, and baselines).

**Data availability**
Extraction table, quality appraisal, codebook, and search strings: [Zenodo DOI, once deposited].

**Funding / conflicts**
No external funding; carried out at Amrita Vishwa Vidyapeetham, Chennai. No competing interests.
