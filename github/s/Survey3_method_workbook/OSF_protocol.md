# OSF registration text — Survey 3 (retrospective)

Paste each section into the matching field of the OSF "Generalized Systematic Review Registration"
form, in the same order as for Surveys 1 and 2. Items marked **[CHECK]** need information from the authors.

---

**Title**
Meta-Learning Orchestration of Learning Modalities on Resource-Constrained Robots: A Systematic Review — review protocol

**Authors**
Yeshwanth Guru (ORCID 0009-0007-6353-4033); Dev Kunwar Singh Chauhan (ORCID 0000-0002-1466-4567).
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

**Contributors (OSF project > Contributors)**
Yeshwanth Guru (Admin, bibliographic) first; Dev Kunwar Singh Chauhan (Read + Write, bibliographic)
second. Use a new OSF project, separate from the Survey 1 and Survey 2 projects.

**License**
CC-By Attribution 4.0 International. Copyright holders: Yeshwanth Guru, Dev Kunwar Singh Chauhan. Year: 2026.

**Description / Summary**
Protocol for a systematic review of the methods an embodied agent on resource-constrained hardware
would need in order to orchestrate several learning modalities (vision perception, reinforcement
learning, imitation learning, fault adaptation) with a small, meta-learned gate that routes on
calibrated confidence signals under a compute budget. The review grades 180 works on a six-level
evidence scale (E1 conceptual to E6 deployment), codes the compute footprint of each system as
published and the confidence signal it exposes, and appraises the 161 primary studies at levels E2–E5
against seven criteria. Registered retrospectively after the corpus was closed (4 October 2026).
Companion of two reviews by the same authors (quantum technologies for autonomous robotics;
quantum-like cognition for autonomous agents), registered separately.

**Registration timing / Stage of review**
Review completed. Registered retrospectively to document the methods as applied. If asked "Has data
collection started?": Yes, completed. Review stage: tick Completed for every stage.

**Review stages (free text)**
1. Preparation: research questions (RQ1–RQ5), eligibility criteria (I1–I3, X1–X5), evidence scale
   (E1–E6, R, S), coding scheme (edge class, confidence-signal class) and extraction fields defined.
2. Identification: stage 1, initial reading list (108 works); stage 2, structured searches in ten topic
   streams, September 2026 (72 works added); stage 3, targeted web search, 4 October 2026 (no work
   added; four candidates recorded).
3. Screening and eligibility: title and abstract against I1–I3 and X1–X5; every included record
   checked against its arXiv or publisher page.
4. Extraction: one structured write-up per work (task, method, setup, key result, limitation, edge
   footprint, role in the framework), from the full text for 13 works, the abstract and publisher page
   for 162, and the standard description for 5 well-known works.
5. Appraisal and coding: evidence level, edge class, confidence-signal class and criteria Q1–Q7.
6. Synthesis: narrative synthesis by topic, cross-tabulation of evidence level against edge class and
   signal class, and an illustrative routing simulation.

**Primary research questions**
- RQ1. Which learning modalities can a resource-constrained robot draw on, and which confidence signal
  can each modality emit?
- RQ2. How is the choice among models, skills or modalities made in current systems, and is that choice
  learned, uncertainty-aware, compute-budgeted and deployable on edge hardware?
- RQ3. Which confidence signals are cheap and calibrated enough to be compared and fused on edge hardware?
- RQ4. Can meta-learning and on-device adaptation train such an orchestrator on the robot within its
  memory and compute?
- RQ5. How far does the published evidence go toward a physical, resource-constrained robot, and what
  evaluation would show that orchestration outperforms its strongest single component?

**Eligibility criteria**
Inclusion (all required):
- I1. Proposes, evaluates or reviews a method in one of twelve component areas of learned orchestration
  for embodied agents: LLM planners and orchestrators; VLA and robot foundation models; perception with
  epistemic uncertainty; reinforcement learning and policy variance; imitation learning and behavioral
  fidelity; fault detection, adaptation and recovery; meta-learning; uncertainty fusion and calibration;
  on-device adaptation and continual learning; adaptive computation, mixture of experts and routing;
  low-cost platforms, benchmarks and evaluation; safe learning.
- I2. Reports the method and its evaluation in enough detail to assign an evidence level, or is a
  review, benchmark or software release that defines a component.
- I3. Journal article, conference paper or arXiv preprint in English, 1991 to October 2026.
Exclusion:
- X1. Multi-robot or fleet learning without a single-robot component (kept only as a source of fusion methods).
- X2. Quantum or neuromorphic hardware (covered by the companion reviews).
- X3. Record that could not be located or verified on an arXiv or publisher page.
- X4. Non-scholarly source (blog, product page, talk abstract, model card).
- X5. Duplicate version of an included work (the archival version is kept).

**Information sources**
arXiv; proceedings of CoRL, RSS, ICRA, IROS, NeurIPS, ICML and ICLR; publisher sites (IEEE Xplore,
ACM, Springer, Elsevier, Nature, JMLR, PMLR); general web search for stage 3. Last search 4 October 2026.

**Search strategy**
See `Survey3_data_package/search_strings.md`. The stage-2 strings and hit counts were not logged; the
concept blocks given there reconstruct their scope. Stage 3 is logged query by query in
`targeted_search_record.md`.

**Study selection and data extraction**
Single reviewer (first author) for screening and extraction; the second author checked the evidence
levels and the edge and signal coding of the core works. **[CHECK: confirm, and give the agreement
statistic if a second coding was done]**

**Evidence levels**
E1 conceptual; E2 algorithmic or analytic; E3 simulation or benchmark; E4 real robot, laboratory;
E5 real robot, extensive or multi-platform; E6 deployment with real users; R review; S software,
dataset or benchmark suite. Ambiguous cases are assigned the lower level.
Distribution: E2 15, E3 81, E4 56, E5 9, E6 0, R 14, S 5 (n = 180).

**Risk-of-bias / quality appraisal**
Seven criteria for primary studies (E2–E5): Q1 method specification; Q2 baseline comparison; Q3
physical validation; Q4 compute reporting; Q5 quantitative evaluation; Q6 code or model release;
Q7 confidence signal exposed. Coded M / P / N / ? by the explicit rules in
`Survey3_data_package/codebook.md`, applied to the extraction fields; to be confirmed against the
full texts.

**Synthesis**
Narrative synthesis by topic, organised around four modality–signal pairs and the orchestrator;
counts by evidence level, edge class and signal class; no meta-analysis (outcomes are heterogeneous).
An illustrative simulation (synthetic data) quantifies the effect of miscalibration on
confidence-gated routing.

**Data and materials**
Data package (`Survey3_data_package/`), simulation code (`Survey3_TNNLS_Supplementary_routing_sim.py`),
Zenodo DOI **[CHECK: add after reserving]**.

**Conflicts of interest / funding**
**[CHECK]**

---

## 6. Corrections made to the initial list (stage 1)

Each item of the initial list was checked against its arXiv or publisher record; the bibliography
uses the corrected details.

- [Liang 2023] Initial list gave 2022 (arXiv); published at ICRA 2023.
- [Yao 2023a] Initial list gave 2022 (arXiv); published at ICLR 2023.
- [Singh 2023] Also a journal version: Autonomous Robots 47(8), 999–1012 (2023), doi:10.1007/s10514-023-10135-3.
- [Wang 2024a] Initial list gave 2023 (arXiv); TMLR 2024.
- [Brohan 2023a] Initial list gave 2022 (arXiv); RSS 2023.
- [Jiang 2023] Initial list gave 2022 (arXiv); ICML 2023.
- [Octo 2024] The RSS proceedings list individual authors; cite them rather than "Octo Model Team".
- [Black 2024] Initial list gave arXiv 2024; published at RSS 2025.
- [Bousmalis 2023] Initial list gave 2023; TMLR 2024.
- [Li 2024a] Initial list gave 2023 (arXiv); ICLR 2024.
- [Burda 2019] Initial list gave 2018 (arXiv); ICLR 2019.
- [Hafner 2023] DreamerV3: the initial list cited the 2023 arXiv version (2301.04104, "Mastering diverse domains through world models"); cite the Nature 2025 version.
- [Nagabandi 2019] Initial list gave 2018 (arXiv); ICLR 2019.
- [Hospedales 2022] Initial list gave 2021 (online); journal issue 2022.
- [Baltrusaitis 2019] Initial list gave 2018 (online); journal issue 2019.
- [Schaul 2016] Initial list gave 2015 (arXiv); ICLR 2016.
- [Hu 2022] Initial list gave 2021 (arXiv); ICLR 2022.
- [DeLange 2022] Initial list gave 2021 (online); journal issue 2022.
- [Puigcerver 2024] Initial list gave 2023 (arXiv); ICLR 2024.
- [Wang 2024b] Full title: "Sparse Diffusion Policy: A Sparse, Reusable, and Flexible Policy for Robot Learning".
- [Reuss 2025] Authors and arXiv id verified.
- [Huang 2025] arXiv:2503.08564; page numbers from project BibTeX.
- [SMP 2026] Authors verified (arXiv, Jan 2026).
- [Cadene 2024] Software. A citable paper now exists: Cadene et al. (2026), ICLR 2026, arXiv:2602.22818 (added as a separate entry).
- [OXE 2024] Initial list gave 2023 (arXiv); ICRA 2024.
- MoDE (Reuss 2025): full authors Reuss, Pari, Agrawal, Lioutikov; arXiv:2412.12953; ICLR 2025.
- MoE-Loco (Huang 2025): authors Runhan Huang, Shaoting Zhu, Yilun Du, Hang Zhao; arXiv:2503.08564; DOI 10.1109/IROS60139.2025.11246585.
- SMP (arXiv:2601.21251): authors Ce Hao, Xuanran Zhai, Yaohua Liu, Harold Soh.
- Sparse Diffusion Policy: CoRL 2024, PMLR 270, 649–665; first author Yixiao Wang.
- DreamerV3: published as "Mastering diverse control tasks through world models", Nature 640, 647–653 (2025).
- π0: published at RSS 2025 (DOI 10.15607/RSS.2025.XXI.010).
- Octo: cite the RSS 2024 author list (Ghosh, Walke, Pertsch, Black, Mees, Dasari, …) rather than "Octo Model Team".
- Shinn 2023 (Reflexion): arXiv lists Edward Berman as an author.
- Ross 2011 (DAgger): Gordon, G.J. and Bagnell, J.A.
- Rakelly 2019 (PEARL): author order Rakelly, Zhou, Quillen, Finn, Levine.
- McMahan 2017 (FedAvg): first author H. Brendan McMahan.
- Cai 2020 (TinyTL): arXiv title says "Reduce Activations, Not Trainable Parameters"; the NeurIPS title uses "Reduce Memory, Not Parameters". Use the NeurIPS title.
- LeRobot: a citable paper now exists (Cadene et al., ICLR 2026, arXiv:2602.22818). Cite it alongside the software.
- Kairouz 2021: volume and pages not confirmed; Pang 2021: arXiv journal-ref gives 2020 online, 2021 issue.
