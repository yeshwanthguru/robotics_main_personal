# Survey 1 — literature cross-check (October 2026)

> Historical record (kept as provenance for the 12 studies added by the targeted search in Table S6 and Figure S1). The counts below are superseded: the survey now has 72 primary studies, 107 foundational works and 185 references.

**Status: integrated.** All 12 studies in part A are now primary studies (70 in total) and the five ✔ items in part B are cited as foundational works (96). Counts, Tables 2–4, Figs. 2 and 5, the PRISMA diagram, the supplement and `extraction_table.csv` are updated.

Web search across every branch of the taxonomy, compared against the 155 entries in
`refs.bib`. "In scope" means the study would satisfy inclusion criterion I1 (a quantum or
quantum-inspired method applied to a robotic function). BibTeX for the entries marked ✔ has been merged into `refs.bib`.

## A. Likely in scope — would change counts or claims

| # | Study | Venue | Why it matters | Suggested level | Bib |
|---|---|---|---|---|---|
| 1 | Sun, Hagog, Weber, Hein, Udluft, Tresp, Ma — *First Experience with Real-Time Control Using Simulated VQC-Based Quantum Policies* | arXiv:2508.01690 (QML@QCE 2025) | A VQC policy balances a **physical** cart-pole in real time; latency analysis shows local simulated execution meets the deadline but cloud QPU access does not. Contradicts "no genuinely quantum computational method reached L5" (it is L5 / simulated) and directly supports Section 11.4. | L5 / simulated | ✔ |
| 2 | *Towards Real-time Control of a CartPole System on a Quantum Computer* | arXiv:2605.01716 (2026) | Single-qubit actor–critic agent run on the VTT Q5 superconducting QPU; programming the readout electronics directly gave >10× faster execution — the first attempt to put a QPU inside a control loop. Check whether the cart-pole is physical or simulated. | L3–L4 / QPU | – (authors to confirm) |
| 3 | Lathrop, Boardman, Martínez — *Quantum Search Approaches to Sampling-Based Motion Planning* | IEEE Access 11:89506–89519 (2023) | Recasts sampling-based motion planners as database-oracle search for Grover-type algorithms (q-FPS). Core paper for Section 5; it is in IEEE Xplore, so its absence is a search-coverage question. | L2 / simulated | ✔ |
| 4 | Park, Yun, Kim, Rodrigues, Park, Jung, Kim — *Quantum Multi-Agent Actor-Critic Networks for Cooperative Mobile Access in Multi-UAV Systems* | IEEE Internet of Things J. 10(22):20033–20048 (2023) | QMARL with a quantum centralised critic for UAV fleets. | L4 / simulated | ✔ |
| 5 | Park, Kim, Park, Jung, Kim — *Quantum Multi-Agent Reinforcement Learning for Autonomous Mobility Cooperation* | IEEE Communications Magazine 62(6):106–112 (2024) | QMARL for cooperative autonomous mobility; projection-value-measure trick for action scaling. | L4 / simulated | ✔ |
| 6 | Roh, Baek, Kim, Kim — *Fast Quantum Convolutional Neural Networks for Low-Complexity Object Detection in Autonomous Driving Applications* | IEEE Trans. Mobile Computing 24(2):1031–1042 (2025) | Quantum CNN object detection on KITTI — fills the "QML for robot perception is scarce" gap in Section 6.1. | L2 + real data / simulated | ✔ |
| 7 | Windmann — *Quantum computer-aided job scheduling for storage and retrieval systems* | at – Automatisierungstechnik (2023), doi 10.1515/auto-2023-0072 | QAOA scheduling of automated storage/retrieval machines, run on IBM Q System One. | L3 / QPU | ✔ |
| 8 | Liu et al. — *Optical-Relayed Entanglement Distribution Using Drones as Mobile Nodes* | Phys. Rev. Lett. 126:020503 (2021) | First drone-to-drone and drone-to-ground entanglement distribution (1 km). Belongs next to Tian/Conrad in Section 7.2. | L5 / link hardware | ✔ |
| 9 | Templier et al. — *Tracking the vector acceleration with a hybrid quantum accelerometer triad* | Science Advances 8:eadd3854 (2022) | First 3-axis hybrid quantum accelerometer (50× better stability than classical). Belongs next to Cheiney2018. | L3 / sensor hardware | ✔ |
| 10 | Essalmi, Garrido, Nashashibi — *Multi-Player, Multi-Strategy Quantum Game Model for Interaction-Aware Decision-Making in Automated Driving* | arXiv:2602.03571 (2026); earlier version arXiv:2509.01582 | Quantum game model for driving decisions with lower collision rates in simulation — the only decision-making study close to a robot. | L2 / simulated | ✔ |
| 11 | Bang, Lee, An, Kim — *Optimality-Preserving Decomposition for Scalable QAOA in Natural-Language-Guided Multi-Drone Assignment* | arXiv:2606.14252 (2026) | Constraint-preserving (XY-mixer, W-state) CVaR-QAOA for multi-drone task allocation; directly tests the "constraint-preserving mixers untested on robots" gap stated in Section 12. Statevector simulation only. | L2 / simulated | ✔ |
| 12 | Osaba et al. — Quantum for Drone Routing (Q4DR) | IEEE CEC 2025 | Hybrid QAOA clustering + annealer routing for real-world drone routing. | L3 / QPU (check) | – |

## B. Foundational or related work worth citing

| Study | Venue | Where it fits |
|---|---|---|
| Rieffel et al. — *A case study in programming a quantum annealer for hard operational planning problems* | Quantum Inf. Process. 14:1–36 (2015) | Early annealer study on navigation- and scheduling-type planning (NASA). Section 4.1 / 5.1. ✔ |
| Neukart et al. — *Traffic flow optimization using a quantum annealer* | Frontiers in ICT 4:29 (2017) | First vehicle-routing study on D-Wave (VW). Section 4.2 background. ✔ |
| Yarkoni, Raponi, Bäck, Schmitt — *Quantum annealing for industry applications: introduction and review* | Rep. Prog. Phys. 85:104001 (2022) | Standard annealing review; supports Section 4 assessment. ✔ |
| Geiger et al. — *Detecting inertial effects with airborne matter-wave interferometry* | Nature Communications 2:474 (2011) | First atom-interferometer inertial measurements on an aircraft. Section 7.1. ✔ |
| Zhuang et al. — *Quantum Computing in Intelligent Transportation Systems: A Survey* | arXiv:2406.00862 (2024) | Related survey; add to Section 1.3 / Table 1 discussion. ✔ |
| Osaba, Villar-Rodriguez, Asla — *Solving a real-world package delivery routing problem using quantum annealers* | Scientific Reports (2024) | Vehicle routing, same group as Osaba2025. – |
| SandboxAQ / Acubed AQNav flight trials (2025) | Industry announcement | Independent quantum-magnetometer navigation trials; relevant to the "needs independent replication" point on Muradoglu2025 — cite as grey literature only. – |

## C. What this says about the search

Items 3–7 are journal papers indexed in IEEE Xplore, Scopus and Web of Science, which the
survey says it searched. Their absence suggests the robotics block of the search string missed
terms such as *UAV/drone* combined with *multi-agent*, *autonomous mobility*, *autonomous
driving*, *object detection*, *cart-pole/control*, and *storage and retrieval*. Re-running the
search with those terms, and reporting the new counts in the PRISMA diagram, would address the
coverage question a reviewer is likely to raise.
