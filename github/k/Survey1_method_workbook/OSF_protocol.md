# OSF registration text — Survey 1 (retrospective)

Paste each section into the matching field of the OSF "Generalized Systematic Review Registration"
form (or into a single description field if you use "Open-Ended Registration").

---

**Title**
Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints — review protocol

**Authors**
Yeshwanth Guru (ORCID 0009-0007-6353-4033); Dev Kunwar Singh Chauhan (ORCID 0000-0002-1466-4567).
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

**Contributors (OSF project > Contributors)**
Yeshwanth Guru (Admin, bibliographic) first; Dev Kunwar Singh Chauhan (Read + Write, bibliographic)
second. Add Dev to the project before starting the registration. Link both ORCIDs to the OSF profiles.

**License**
CC-By Attribution 4.0 International (not "No Derivatives", not "Non-Commercial").
Copyright holders: Yeshwanth Guru, Dev Kunwar Singh Chauhan. Year: 2026.

**Description / Summary**
Protocol for a systematic survey of quantum technologies applied to autonomous robots (optimization
and planning, learning, sensing and communication, decision-making and reasoning). The survey grades
72 primary studies on a six-level evidence scale (L1 argued to L6 deployed with measured advantage)
and appraises reporting quality against seven criteria. Registered retrospectively after the review
was completed (corpus closed October 2026). Authors: Yeshwanth Guru and Dev Kunwar Singh Chauhan,
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

**Registration timing / Stage of review (state this honestly)**
Review completed. Registered retrospectively after the corpus was closed (October 2026), to document
the methods as applied, so that readers can check the review against them.
If asked "Has data collection started?": Yes, completed.
Review stage (tick Completed for every stage): preliminary searches; piloting of the study selection
process; formal screening of search results against eligibility criteria; data extraction; risk of
bias (quality) assessment; data analysis. Single choice: "Completed" / "Review completed".
Free text: All stages completed; search closed October 2026; registered retrospectively before
journal submission.

**Review stages (free-text field; all stages already completed)**
All stages below were completed before this retrospective registration.
1. Preparation: research questions (RQ1-RQ5), eligibility criteria, six-level evidence scale,
   execution tags, and extraction codebook defined.
2. Search: seven databases (IEEE Xplore, ACM DL, Scopus, Web of Science, SpringerLink,
   ScienceDirect, arXiv), backward and forward reference chasing, and targeted searches in
   application areas; closed October 2026.
3. Screening: title/abstract, then full text, against the eligibility criteria, by the first author.
4. Extraction: by the first author, using the codebook; reviewed by the second author, with
   disagreements resolved by discussion.
5. Critical appraisal and evidence grading: seven appraisal criteria (met / partly met / not met);
   each study assigned an evidence level (L1-L6) and a quantum-execution tag.
6. Synthesis: narrative synthesis by robotic function; cross-tabulation of evidence level by
   execution tag; latency analysis; fault-tolerant resource estimate. No meta-analysis.
7. Reporting: manuscript prepared following PRISMA 2020.
No separate pilot screening or pilot extraction stage was recorded, and there were no
preregistration updates, because the protocol is registered after completion.

**Current review stage**
All stages (1-7) completed; the manuscript is ready for journal submission. This is a retrospective
registration, not a preregistration, and it is the first and only registration of this review (no
earlier versions or updates). It records the methods as applied so that readers can check the
published review against them.

**Start date**
2026-06-01 (approximate: the review started in June 2026; the exact day was not recorded).
End of search: October 2026.

**End date**
2026-10-02 (review completed; manuscript ready for submission).

**Type of review**
Dropdown: Systematic review (not meta-analysis, not scoping, not rapid, not umbrella).
Free-text version: Systematic review with narrative synthesis (no meta-analysis), reported following
PRISMA 2020 where applicable. Evidence is graded on a six-level scale (L1 argued to L6 deployed with
measured advantage) and reporting quality is appraised against seven criteria.

**Discipline / Subjects**
Engineering > Robotics; Computer science (if absent: Physical sciences > Quantum physics).

**Background**
Autonomous robots repeatedly solve hard computational problems under tight time budgets: they
estimate their state from noisy sensors, plan motions, share tasks with other robots, and learn from
limited experience. Multi-robot routing and task allocation are NP-hard, localization and
belief-space planning scale with the state space, and reinforcement learning on physical robots is
sample-inefficient. Quantum computing offers tools that target exactly these problems (Grover search,
amplitude estimation, quantum annealing and QAOA for combinatorial optimization, and parameterized
circuits as compact learners), and quantum sensors are beginning to improve inertial and magnetic
navigation. Robots, however, need decisions within milliseconds to seconds under limits on size,
weight, and power, whereas today's noisy intermediate-scale quantum (NISQ) processors are small,
noisy, cryogenic, and usually reached through the cloud.

Existing reviews of quantum robotics (Tandon et al. 2017; Petschnigg et al. 2019; Yan et al. 2024;
Haldorai 2024; Udekwe et al. 2025; Fazilat et al. 2025; Nigatu et al. 2026) are mostly descriptive.
They rarely grade the evidence behind a claim, seldom separate genuinely quantum results from
quantum-inspired classical algorithms, and, because most predate the experimental work of the NISQ
era, say little about quantum reinforcement learning on robot tasks, annealer-based fleet control,
head-to-head comparisons with classical solvers, dequantization, error-mitigation costs, or measured
cloud latency. Broader reviews of quantum computing, quantum machine learning, and quantum
reinforcement learning do not address robots.

This review aims to establish what the published evidence actually shows. It (1) maps quantum
methods onto five robotic functions, (2) grades every primary study on one six-level evidence scale
and records whether its quantum component ran on hardware, a simulator, or classical hardware,
(3) separates genuinely quantum from quantum-inspired results, (4) tests the claims against the
latency and hardware budgets of real robots, and (5) proposes a research agenda and a reporting
checklist for quantum-robotics experiments.

**Primary research question(s)** (wording identical to Section 3.1 of the manuscript)
- RQ1. Which quantum methods have been applied to which robotic functions (optimization and planning;
  learning, including quantum machine learning and reinforcement learning; sensing and communication;
  and decision-making and reasoning)?
- RQ2. What level of evidence supports each application, from theory to end-to-end deployment?
- RQ3. Which reported benefits are genuinely quantum, and which come from quantum-inspired classical
  algorithms or are removed by dequantization?
- RQ4. Which hardware and deployment constraints (qubit counts, noise, latency, quantum-classical
  communication, and size, weight, power, and cooling) limit quantum computing in robotics today?
- RQ5. Which directions offer realistic benefit by 2030, and what is needed beyond?

PICOS framing (adapted to a computing review):
- Population: autonomous robots and robotic systems (mobile robots, manipulators, swarms, UAVs, AGVs,
  autonomous vehicles) and their functions.
- Intervention: quantum or quantum-inspired methods (quantum computation, quantum sensing, quantum
  communication, quantum-probability models).
- Comparison: classical robotics methods and solvers, where the study reports them.
- Outcomes: evidence level (L1-L6), execution venue (none / simulated / QPU / quantum sensor or link
  hardware / classical), reported performance against baselines, and deployment constraints.
- Study design: any primary study (theoretical, simulation, hardware experiment, field trial) and
  reviews of the topic.

**Secondary research question(s)**
None; all five questions are primary and all are answered in the final report.

**Expectations / hypotheses**
No formal hypotheses were specified before the review began. Because this registration is made
after the review was completed, we do not state expectations here, to avoid presenting the findings
as if they had been predicted.
Context that may color interpretation: (1) the authors work in robotics (Department of Mechanical
Engineering) and are users, not developers, of quantum hardware; (2) the authors receive no funding
from, and have no ties to, quantum-hardware or software vendors; (3) the field is young and fast
moving, many studies are preprints, and advantage claims are often made in promotional language, so
each claim was judged against its evidence level and baseline rather than its stated conclusion;
(4) a single reviewer screened the records, which may bias inclusion decisions.

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
