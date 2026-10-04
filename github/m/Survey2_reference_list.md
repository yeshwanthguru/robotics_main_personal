# Survey 2 — reference list (Artificial Intelligence Review)

**Quantum-Inspired Cognition and Decision-Making for Autonomous Agents, from Robotics to AI/ML Systems: A Systematic Review**  
Yeshwanth Guru and Dev Kunwar Singh Chauhan · generated 4 October 2026 from `Survey2_AIR_LaTeX_Overleaf/refs.bib`, `Survey2_fulltexts/index.csv` and the data package

| Group | Cited | Full text missing |
|---|---|---|
| Application studies | 67 | 50 |
| Theory and evidence studies | 71 | 51 |
| Reviews | 17 | 9 |
| Background works | 43 | 27 |
| Excluded under E5 (cited once; reviewed in Survey 1) | 11 | 0 |
| Method references | 3 | 0 |
| **Total** | **212** | **137** |
| New papers found on 4 Oct 2026, not yet cited | 21 | 21 |

40 works are cited in both Survey 1 and Survey 2 (marked "also S1"); download them once. Full texts are in `github/m/Survey2_fulltexts/` (private: never upload with the submission). `Guru2026` is our own Survey 1 manuscript and is not counted as missing.

## 1. Literature check of 4 October 2026: papers not yet in Survey 2

I ran 22 topic searches (plus a look-up of the details of each hit) covering quantum cognition for robots and autonomous agents, quantum-like Bayesian networks, LLM order effects and contextuality, human–AI trust, quantum-inspired RL, projective simulation, quantum-inspired deep learning and NLP, swarms and teams, emotion models, open-system and quantum-walk decision models, and recent reviews. Records already cited were checked by title against refs.bib. Publisher and arXiv pages could not be opened in this environment, so details come from search-result metadata: verify each one before citing.

Priority A = should be added (clear fit, fills a gap); B = likely add after reading; C = record as an exclusion. Adding any of them changes the counts (67 application, 71 theory studies), the PRISMA flow and the tables, so decide after reading the full texts.

| # | Priority | Proposed group | Reference | Why it matters |
|---|---|---|---|---|
| N1 | A | Application (I1) – circuit design | Romeo, F. and Settino, J. (2026). *Extreme Quantum Cognition Machines for Deliberative Decision Making*. arXiv:2603.05430 | Quantum-cognition learning architecture for decisions with noisy and contradictory data |
| N2 | A | Application (I1) – multi-agent | Beuria, J., Chaurasiya, M. and Behera, L. (2025). *Collective motion using quantum-like entanglement of neighbours in perceptual space*. Proc. R. Soc. A 481, 20250489 (arXiv:2409.18985) | Quantum-like perception model for swarm collective motion; recovers the Vicsek model (Section 12) |
| N3 | A | Application (I1) – multi-agent | *Non-Markovian Collective Motion from Self-Regulated Perceptual Dynamics* (2025). arXiv:2510.23688 — authors to verify (probably the same IIT Mandi group) | Open-quantum-system perception and self registers for swarm agents |
| N4 | A | Application (I1) – multi-agent | *Self-Healing Coordination in Cognitive Swarm Agents with Bloch-Type Perceptual Memory* (2026). arXiv:2607.11960 — authors to verify | Follow-up on quantum-like perceptual memory for swarm coordination |
| N5 | A | Application (I1) – deep learning | Chen, Y., Yan, K., Pan, Y. and Dong, D. (2025). *QiNN-QJ: A Quantum-inspired Neural Network with Quantum Jump for Multimodal Sentiment Analysis*. arXiv:2510.27091 | Quantum-inspired multimodal fusion with learned Hamiltonian and Lindblad operators (Sections 8–9) |
| N6 | A | Application (I1) – deep learning | Liu, Y. et al. (2023). *A Quantum Probability Driven Framework for Joint Multi-Modal Sarcasm, Sentiment and Emotion Analysis*. arXiv:2306.03650 — author list to verify | Quantum-probability multimodal decision fusion (same line as Li2021a/b, Gkoumas2021) |
| N7 | A | Application (I1) – human–machine | Snow, L., Jain, S. and Krishnamurthy, V. (2022). *Lyapunov based Stochastic Stability of a Quantum Decision System for Human-Machine Interaction*. arXiv:2205.12378 (related version arXiv:2204.00059; check the published venue) | Controls a Lindbladian (quantum) human decision model in a human–machine loop |
| N8 | A | Application (I1) – LLMs | Agostino, C. J., Le Thien, Q., Apsel, M., Pak, D., Lesyk, E. and Majumdar, A. (2025). *A quantum semantic framework for natural language processing*. arXiv:2506.10077 | Semantic Bell (CHSH) test on LLM agents; values above the classical bound reported (Section 9.3) |
| N9 | A | Application (I1) – LLMs | Agostino, C. J., Le Thien, Q., D'Souza, N. and van der Elst, L. (2026). *The production of meaning in the processing of natural language*. arXiv:2603.20381 | Contextuality in LLM interpretation of ambiguous expressions |
| N10 | A | Theory and evidence (I2) | Li, J.-A., Dong, D., Wei, Z. et al. (2020). *Quantum reinforcement learning during human decision-making*. Nature Human Behaviour 4, 294–307. doi:10.1038/s41562-019-0804-2 | Quantum RL fitted to human Iowa Gambling Task and fMRI data — direct human evidence for Section 10 and Case Study 3 |
| N11 | A | Theory and evidence (I2) | Chen, M., Ferro, G. M., Sornette, D. and Lorenzo, S. (2022). *On the use of discrete-time quantum walks in decision theory*. PLOS ONE 17(8), e0273551. doi:10.1371/journal.pone.0273551 | Quantum-walk models of choice and confidence (Sections 5 and 21) |
| N12 | B | Application (I1) – LLMs | Laine, T. A. (2025). *The Quantum LLM: Modeling Semantic Spaces with Quantum Principles*. arXiv:2504.13202 | Quantum-probability reading of LLM semantic spaces |
| N13 | B | Application (I1) – circuit on QPU | Laine, T. A. (2025). *Quantum LLMs Using Quantum Computing to Analyze and Process Semantic Information*. arXiv:2512.02619 | LLM embedding similarity computed on a real quantum computer; check against E5 |
| N14 | B | Application (I1) – decision systems | Mertová, A., Figl, K. and Pothos, E. M. (2026). *Quantum Cognition Meets Quantum Computing: Modeling Human Reasoning for Advanced Decision Systems*. ECIS 2026 Proceedings (AIS eLibrary) | Quantum-cognition models of human reasoning for information/decision systems |
| N15 | B | Application (I1) – circuit design | Pothukuchi, R. P. et al. (incl. Busemeyer, J. R. and Cohen, J. D.) (2023). *The QUATRO Application Suite: Quantum Computing for Models of Human Cognition*. arXiv:2309.00597 | Benchmark suite of cognition models as quantum circuits (Section 20 software; companion to Widdows2023) |
| N16 | B | Application (I1) – circuit design | Wang, H., Smith, J. W. and Sun, Y. (2019). *Simulating Cognition with Quantum Computers*. arXiv:1905.12599 | Early proposal to run cognitive models on quantum computers |
| N17 | B | Application (I1) – teams | Lawless, W. F. (2026). *Toward tunable advantages of quantum-like teams: the physics of interdependent teams to 'squeeze' uncertainty*. Frontiers in Physics. doi:10.3389/fphy.2025.1715888 | Continues Lawless2020/2023/2025 on quantum-like human–machine teams |
| N18 | B | Theory and evidence (I2) | Edwards, D. J. (2025). *Further N-Frame networking dynamics of conscious observer-self agents via a functional contextual interface ... in humans and AI*. Frontiers in Computational Neuroscience. doi:10.3389/fncom.2025.1551960 | Theoretical model of decision fallacies for humans and AI; low evidence level |
| N19 | C | Probably E5 (quantum computation for inference) | *Hybrid quantum-classical multi-agent decision-making framework based on hierarchical Bayesian networks in the NISQ era* (2025). Chinese Physics B 34(12), 120304. doi:10.1088/1674-1056/adefd7 — authors to verify | Quantum circuits speed up Bayesian-network inference; record as an E5 exclusion (Table S7) |
| N20 | C | Probably E5 (quantum computation for inference) | Recursive quantum-classical hybrid Bayesian-network inference with quantum decision networks (2025), European Physical Journal Special Topics — this is a description, not the exact title; find title, authors and DOI | As above; record as an E5 exclusion |
| N21 | C | Check E5 (variational circuit) | Singh, J., Bhangu, K. S., Alkhanifer, A., Alzubi, A. A. and Ali, F. (2025). *Quantum neural networks for multimodal sentiment, emotion, and sarcasm analysis*. Alexandria Engineering Journal 124, 170–187 | VQE-trained quantum neural network; probably quantum ML as accelerator (E5) |

**Cited entries to update**

- `Maksymov2025` (cited as an arXiv preprint) — Now a Springer book: Maksymov, I. S. (2026). *Cognition in Superposition: Quantum Models in AI, Economics, Defence, Gaming and Collective Behaviour*. Springer, Cham. doi:10.1007/978-3-032-25965-3. Relevant chapters: 4 Quantum Perception; 6 Quantum-Cognitive Artificial Neural Networks; 9 Neuromorphic Implementation of Quantum-Cognitive Models; 11 Quantum Cognition and Quantum Mind. Update the bib entry (title now says "Economics" instead of "Finance").
- `Busemeyer2012` — The text mentions the second edition; add Busemeyer, J. R. and Bruza, P. D. (2024). *Quantum Models of Cognition and Decision*, 2nd edn. Cambridge University Press — or cite the 2nd edition only.

**Found and judged out of scope**

- arXiv:2512.20654 Q-RUN, quantum-inspired data re-uploading networks (generic ML, no cognition or decision model)
- arXiv:2601.18953, 2603.25138, 2602.12464, 2412.18208, 2507.01691 (reinforcement learning *for* or *on* quantum devices: quantum computation, Survey 1 territory)
- arXiv:2602.06286 Yamin et al. 2026, belief coherence of LLMs (classical probability only)
- Mannone et al. 2025, quantum computing for swarm robotics (already in Survey 1)
- Explainable Quantum AI for vehicle energy management (quantum ML + SHAP/LIME; no cognition model)

Already cited, confirmed current: Khrennikov2026 (Discover AI), Humr2025, Chella2026 (teleo-reactive robot), Kang2026 (QQ audit of LLMs), Lawless2025, Huang2025b (overview of the research programme), Asano2026 (GKSL dynamics), vanderMeer2025 (trust and quantum random walks), Song2022 (autonomous driving), Ho2022 (affective processes), Daglarli2025, Maksimovic2025, Ried2019, Lanza2020/2021.

## 2. To download

### 2a. New papers from the literature check (21)

- [ ] N1 (A) Romeo, F. and Settino, J. (2026). *Extreme Quantum Cognition Machines for Deliberative Decision Making*. arXiv:2603.05430
- [ ] N2 (A) Beuria, J., Chaurasiya, M. and Behera, L. (2025). *Collective motion using quantum-like entanglement of neighbours in perceptual space*. Proc. R. Soc. A 481, 20250489 (arXiv:2409.18985)
- [ ] N3 (A) *Non-Markovian Collective Motion from Self-Regulated Perceptual Dynamics* (2025). arXiv:2510.23688 — authors to verify (probably the same IIT Mandi group)
- [ ] N4 (A) *Self-Healing Coordination in Cognitive Swarm Agents with Bloch-Type Perceptual Memory* (2026). arXiv:2607.11960 — authors to verify
- [ ] N5 (A) Chen, Y., Yan, K., Pan, Y. and Dong, D. (2025). *QiNN-QJ: A Quantum-inspired Neural Network with Quantum Jump for Multimodal Sentiment Analysis*. arXiv:2510.27091
- [ ] N6 (A) Liu, Y. et al. (2023). *A Quantum Probability Driven Framework for Joint Multi-Modal Sarcasm, Sentiment and Emotion Analysis*. arXiv:2306.03650 — author list to verify
- [ ] N7 (A) Snow, L., Jain, S. and Krishnamurthy, V. (2022). *Lyapunov based Stochastic Stability of a Quantum Decision System for Human-Machine Interaction*. arXiv:2205.12378 (related version arXiv:2204.00059; check the published venue)
- [ ] N8 (A) Agostino, C. J., Le Thien, Q., Apsel, M., Pak, D., Lesyk, E. and Majumdar, A. (2025). *A quantum semantic framework for natural language processing*. arXiv:2506.10077
- [ ] N9 (A) Agostino, C. J., Le Thien, Q., D'Souza, N. and van der Elst, L. (2026). *The production of meaning in the processing of natural language*. arXiv:2603.20381
- [ ] N10 (A) Li, J.-A., Dong, D., Wei, Z. et al. (2020). *Quantum reinforcement learning during human decision-making*. Nature Human Behaviour 4, 294–307. doi:10.1038/s41562-019-0804-2
- [ ] N11 (A) Chen, M., Ferro, G. M., Sornette, D. and Lorenzo, S. (2022). *On the use of discrete-time quantum walks in decision theory*. PLOS ONE 17(8), e0273551. doi:10.1371/journal.pone.0273551
- [ ] N12 (B) Laine, T. A. (2025). *The Quantum LLM: Modeling Semantic Spaces with Quantum Principles*. arXiv:2504.13202
- [ ] N13 (B) Laine, T. A. (2025). *Quantum LLMs Using Quantum Computing to Analyze and Process Semantic Information*. arXiv:2512.02619
- [ ] N14 (B) Mertová, A., Figl, K. and Pothos, E. M. (2026). *Quantum Cognition Meets Quantum Computing: Modeling Human Reasoning for Advanced Decision Systems*. ECIS 2026 Proceedings (AIS eLibrary)
- [ ] N15 (B) Pothukuchi, R. P. et al. (incl. Busemeyer, J. R. and Cohen, J. D.) (2023). *The QUATRO Application Suite: Quantum Computing for Models of Human Cognition*. arXiv:2309.00597
- [ ] N16 (B) Wang, H., Smith, J. W. and Sun, Y. (2019). *Simulating Cognition with Quantum Computers*. arXiv:1905.12599
- [ ] N17 (B) Lawless, W. F. (2026). *Toward tunable advantages of quantum-like teams: the physics of interdependent teams to 'squeeze' uncertainty*. Frontiers in Physics. doi:10.3389/fphy.2025.1715888
- [ ] N18 (B) Edwards, D. J. (2025). *Further N-Frame networking dynamics of conscious observer-self agents via a functional contextual interface ... in humans and AI*. Frontiers in Computational Neuroscience. doi:10.3389/fncom.2025.1551960
- [ ] N19 (C) *Hybrid quantum-classical multi-agent decision-making framework based on hierarchical Bayesian networks in the NISQ era* (2025). Chinese Physics B 34(12), 120304. doi:10.1088/1674-1056/adefd7 — authors to verify
- [ ] N20 (C) Recursive quantum-classical hybrid Bayesian-network inference with quantum decision networks (2025), European Physical Journal Special Topics — this is a description, not the exact title; find title, authors and DOI
- [ ] N21 (C) Singh, J., Bhangu, K. S., Alkhanifer, A., Alzubi, A. A. and Ali, F. (2025). *Quantum neural networks for multimodal sentiment, emotion, and sarcasm analysis*. Alexandria Engineering Journal 124, 170–187
- [ ] Maksymov (2026) book *Cognition in Superposition*, Springer, doi:10.1007/978-3-032-25965-3 (chapters 4, 6, 9, 11)

### 2b. Cited works without a full text in the repository (137)

Save each PDF as `<key>.pdf`. Application studies come first: their full texts are needed to complete the quality appraisal (Q6 reproducibility, currently "?" for 47 studies).

**Application studies (50)**

- [ ] `Moreira2014` [E2] — Moreira and Wichert (2014). *Interference effects in quantum belief networks*. Applied Soft Computing 25, 64–85. doi:10.1016/j.asoc.2014.09.008
- [ ] `Moreira2016` [E3] — Moreira and Wichert (2016). *Quantum-Like Bayesian Networks for Modeling Decision Making*. Frontiers in Psychology 7, 11. doi:10.3389/fpsyg.2016.00011
- [ ] `Moreira2017a` [E3] — Moreira (2017). *Quantum Probabilistic Graphical Models for Cognition and Decision*. Instituto Superior Técnico, Universidade de Lisboa. —
- [ ] `Moreira2020b` [E3] — Moreira et al. (2020). *Quantum-like influence diagrams for decision-making*. Neural Networks 132, 190–210. doi:10.1016/j.neunet.2020.07.009
- [ ] `Wichert2020` [E3] — Wichert, Moreira and Bruza (2020). *Balanced Quantum-Like Bayesian Networks*. Entropy 22(2), 170. doi:10.3390/e22020170
- [ ] `She2021` [E4] — She, Han and Liu (2021). *Application of quantum-like Bayesian network and belief entropy for interference effect in multi-attribute decision making problem*. Computers & Industrial Engineering 157, 107307. doi:10.1016/j.cie.2021.107307
- [ ] `Meghdadi2022` [E3] — Meghdadi, Akbarzadeh-T. and Javidan (2022). *A quantum-like cognitive approach to modeling human biased selection behavior*. Scientific Reports 12, 22545. doi:10.1038/s41598-022-13757-2
- [ ] `Gao2025` [E3] — Gao et al. (2025). *Quantum-like evidence networks decision-making model*. Engineering Applications of Artificial Intelligence 157, 111368. doi:10.1016/j.engappai.2025.111368
- [ ] `Widdows2003` [E4] — Widdows and Peters (2003). *Word Vectors and Quantum Logic: Experiments with negation and disjunction*. Proceedings of the 8th Mathematics of Language Conference (MOL 8). —
- [ ] `Sordoni2013` [E4] — Sordoni, Nie and Bengio (2013). *Modeling term dependencies with quantum language models for IR*. Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '13). doi:10.1145/2484028.2484098
- [ ] `Stoudenmire2016` [E4] — Stoudenmire and Schwab (2016). *Supervised Learning with Tensor Networks*. Advances in Neural Information Processing Systems 29 (NIPS 2016). arXiv:1605.05775
- [ ] `Zhang2018` [E4] — Zhang et al. (2018). *A Quantum Many-body Wave Function Inspired Language Modeling Approach*. Proceedings of the 27th ACM International Conference on Information and Knowledge Management (CIKM 2018). doi:10.1145/3269206.3271723
- [ ] `Li2019` [E4] — Li, Wang and Melucci (2019). *CNM: An Interpretable Complex-valued Network for Matching*. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). doi:10.18653/v1/N19-1420
- [ ] `Li2021a` [E4] — Li et al. (2021). *Quantum-inspired multimodal fusion for video sentiment analysis*. Information Fusion 65, 58–71. doi:10.1016/j.inffus.2020.08.006
- [ ] `Li2021b` [E4] — Li et al. (2021). *Quantum-inspired Neural Network for Conversational Emotion Recognition*. Proceedings of the AAAI Conference on Artificial Intelligence. doi:10.1609/aaai.v35i15.17567
- [ ] `Gkoumas2021` [E4] — Gkoumas et al. (2021). *Quantum Cognitively Motivated Decision Fusion for Video Sentiment Analysis*. Proceedings of the AAAI Conference on Artificial Intelligence. doi:10.1609/aaai.v35i1.16165
- [ ] `Uprety2024` [E4] — Uprety et al. (2024). *Investigating Context Effects in Similarity Judgements in Large Language Models*. arXiv preprint. arXiv:2408.10711
- [ ] `Zhang2025` [E4] — Zhang et al. (2025). *Quantum-Inspired Semantic Matching Based on Neural Networks with the Duality of Density Matrices*. Engineering Applications of Artificial Intelligence 140, 109667. doi:10.1016/j.engappai.2024.109667
- [ ] `Maksimovic2025` [E4] — Maksimovic and Maksymov (2025). *Quantum-Cognitive Neural Networks: Assessing Confidence and Uncertainty with Human Decision-Making Simulations*. Big Data and Cognitive Computing 9(1), 12. doi:10.3390/bdcc9010012
- [ ] `Aerts2026` [E4] — Aerts et al. (2026). *Identifying Quantum Structure in AI Language: Evidence for Evolutionary Convergence of Human and Artificial Cognition*. Entropy 28(6), 622. doi:10.3390/e28060622
- [ ] `Imannezhad2026` [E4] — Imannezhad, Pothos and Wills (2026). *Divergent Patterns of Probabilistic Reasoning in Humans and GPT-5*. Frontiers in Psychology 17, 1782184. doi:10.3389/fpsyg.2026.1782184
- [ ] `Kang2026` [E4] — Kang (2026). *Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat*. arXiv preprint. arXiv:2607.17219
- [ ] `Dong2008` [E4] — Dong et al. (2008). *Quantum Reinforcement Learning*. IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics 38(5), 1207–1220. doi:10.1109/TSMCB.2008.925743 — *also needed for Survey 1 (`Dong2008`)*
- [ ] `Melnikov2018` [E4] — Melnikov, Makmal and Briegel (2018). *Benchmarking Projective Simulation in Navigation Problems*. IEEE Access 6, 64639–64648. doi:10.1109/ACCESS.2018.2876494
- [ ] `Wei2022` [E4] — Wei et al. (2022). *Deep Reinforcement Learning with Quantum-Inspired Experience Replay*. IEEE Transactions on Cybernetics 52(9), 9326–9338. doi:10.1109/TCYB.2021.3053414
- [ ] `Lukac2007` [E2] — Lukac and Perkowski (2007). *Quantum Mechanical Model of Emotional Robot Behaviors*. Proceedings of the 37th International Symposium on Multiple-Valued Logic (ISMVL 2007). —
- [ ] `Hangl2016` [E5] — Hangl et al. (2016). *Robotic Playing for Hierarchical Complex Skill Learning*. Proceedings of the 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). arXiv:1603.00794
- [ ] `Yan2019` [E2] — Yan et al. (2019). *Quantum Structure for Modelling Emotion Space of Robots*. Applied Sciences 9(16), 3351. doi:10.3390/app9163351
- [ ] `Moreira2020a` [E1] — Moreira et al. (2020). *Towards a Quantum-Like Cognitive Architecture for Decision-Making*. Behavioral and Brain Sciences 43, e17. doi:10.1017/S0140525X19001687
- [ ] `Hangl2020` [E5] — Hangl et al. (2020). *Skill Learning by Autonomous Robotic Playing Using Active Learning and Exploratory Behavior Composition*. Frontiers in Robotics and AI 7, 42. doi:10.3389/frobt.2020.00042
- [ ] `Yan2021c` [E2] — Yan et al. (2021). *Emotion Generation and Transition of Companion Robots Based on Plutchik's Model and Quantum Circuit Schemes*. Security and Communication Networks 2021, 6802521. doi:10.1155/2021/6802521
- [ ] `Song2022` [E4] — Song et al. (2022). *Research on Quantum Cognition in Autonomous Driving*. Scientific Reports 12, 300. doi:10.1038/s41598-021-04239-y
- [ ] `Mannone2024` [E2] — Mannone et al. (2024). *Modeling Robotic Thinking and Creativity: A Classic–Quantum Dialogue*. Mathematics 12(5), 642. doi:10.3390/math12050642
- [ ] `Chella2026` [E4] — Chella et al. (2026). *An Architecture for a Quantum Teleo-Reactive Robot*. Entropy 28(7), 731. doi:10.3390/e28070731
- [ ] `Yukalov2018` [E2] — Yukalov, Yukalova and Sornette (2018). *Information Processing by Networks of Quantum Decision Makers*. Physica A: Statistical Mechanics and its Applications 492, 747–766. doi:10.1016/j.physa.2017.11.004
- [ ] `Ried2019` [E4] — Ried, Müller and Briegel (2019). *Modelling Collective Motion Based on the Principle of Agency: General Framework and the Case of Marching Locusts*. PLoS ONE 14(2), e0212044. doi:10.1371/journal.pone.0212044
- [ ] `LopezIncera2020` [E4] — López-Incera et al. (2020). *Development of Swarm Behavior in Artificial Learning Agents that Adapt to Different Foraging Environments*. PLoS ONE 15(12), e0243628. doi:10.1371/journal.pone.0243628
- [ ] `Lawless2020` [E1] — Lawless (2020). *Quantum-Like Interdependence Theory Advances Autonomous Human–Machine Teams (A-HMTs)*. Entropy 22(11), 1227. doi:10.3390/e22111227
- [ ] `Yukalov2022` [E2] — Yukalov, Yukalova and Sornette (2022). *Role of collective information in networks of quantum operating agents*. Physica A: Statistical Mechanics and its Applications 598, 127365. doi:10.1016/j.physa.2022.127365
- [ ] `Yukalov2023` [E2] — Yukalov (2023). *Quantum operation of affective artificial intelligence*. Laser Physics 33(6), 065204. doi:10.1088/1555-6611/accf7a
- [ ] `Essalmi2025` [E4] — Essalmi, Garrido and Nashashibi (2025). *Quantum game models for interaction-aware decision-making in automated driving*. arXiv preprint. arXiv:2509.01582
- [ ] `Kong2026` [E4] — Kong et al. (2026). *Emergence of Longitudinal Queues in Group Navigation: An Interpretable Approach via Projective Simulation*. Biomimetics 11(3), 201. doi:10.3390/biomimetics11030201
- [ ] `Ashtiani2019` [E4] — Ashtiani and Abdollahi Azgomi (2019). *A novel trust evolution algorithm based on a quantum-like model of computational trust*. Cognition, Technology & Work 21(2), 201–224. doi:10.1007/s10111-018-0496-9
- [ ] `Pushparaj2021` [E3] — Pushparaj et al. (2021). *A quantum-inspired model for human-automation trust in air traffic controllers derived from functional Magnetic Resonance Imaging and correlated with behavioural indicators*. Journal of Air Transport Management 97, 102143. doi:10.1016/j.jairtraman.2021.102143
- [ ] `Humr2023` [E2] — Humr, Canan and Demir (2023). *Temporal Evolution of Trust in Artificial Intelligence-Supported Decision-Making*. Proceedings of the Human Factors and Ergonomics Society Annual Meeting 67(1), 1936–1941. doi:10.1177/21695067231193672
- [ ] `Roeder2023` [E3] — Roeder et al. (2023). *A Quantum Model of Trust Calibration in Human–AI Interactions*. Entropy 25(9), 1362. doi:10.3390/e25091362
- [ ] `Humr2026` [E1] — Humr and Canan (2026). *System Level Intervention for AI-Supported Decision-Making: A Quantum Cognition Perspective*. Quantum AI and NLP (QNLPAI 2025). doi:10.1007/978-3-032-13883-5_14
- [ ] `Kak2018` [E2] — Kak (2018). *Order Effects for Queries in Intelligent Systems*. arXiv preprint. arXiv:1804.02759
- [ ] `Hoorn2019` [E2] — Hoorn and Ho (2019). *Robot Affect: the Amygdala as Bloch Sphere*. arXiv preprint. arXiv:1911.12128
- [ ] `Nebli2026` [E2] — Nebli, Saadatdoorabi and Yam (2026). *Deep Sequence Modeling with Quantum Dynamics: Language as a Wave Function*. arXiv preprint. arXiv:2602.22255

**Theory and evidence studies (51)**

- [ ] `Aerts2000` [E2] — Aerts, D'Hondt and Gabora (2000). *Why the Disjunction in Quantum Logic Is Not Classical*. Foundations of Physics 30(9), 1473–1480. doi:10.1023/A:1026457918361
- [ ] `Busemeyer2006` [E2] — Busemeyer, Wang and Townsend (2006). *Quantum Dynamics of Human Decision-Making*. Journal of Mathematical Psychology 50(3), 220–241. doi:10.1016/j.jmp.2006.01.003
- [ ] `Pothos2009` [E3] — Pothos and Busemeyer (2009). *A Quantum Probability Explanation for Violations of `Rational' Decision Theory*. Proceedings of the Royal Society B: Biological Sciences 276(1665), 2171–2178. doi:10.1098/rspb.2009.0121
- [ ] `Busemeyer2009` [E3] — Busemeyer, Wang and Lambert-Mogiliansky (2009). *Empirical Comparison of Markov and Quantum Models of Decision Making*. Journal of Mathematical Psychology 53(5), 423–433. doi:10.1016/j.jmp.2009.03.002
- [ ] `Khrennikov2010` [E2] — Khrennikov (2010). *Ubiquitous Quantum Structure: From Psychology to Finance*. Springer. doi:10.1007/978-3-642-05101-2
- [ ] `Trueblood2011` [E3] — Trueblood and Busemeyer (2011). *A Quantum Probability Account of Order Effects in Inference*. Cognitive Science 35(8), 1518–1552. doi:10.1111/j.1551-6709.2011.01197.x
- [ ] `Yukalov2011` [E3] — Yukalov and Sornette (2011). *Decision Theory with Prospect Interference and Entanglement*. Theory and Decision 70(3), 283–328. doi:10.1007/s11238-010-9202-y
- [ ] `Pothos2013a` [E3] — Pothos and Busemeyer (2013). *Can Quantum Probability Provide a New Direction for Cognitive Modeling?*. Behavioral and Brain Sciences 36(3), 255–274. doi:10.1017/S0140525X12001525 — *also needed for Survey 1 (`Pothos2013`)*
- [ ] `Wang2013a` [E1] — Wang et al. (2013). *The Potential of Using Quantum Theory to Build Models of Cognition*. Topics in Cognitive Science 5(4), 672–688. doi:10.1111/tops.12043
- [ ] `Wang2013b` [E3] — Wang and Busemeyer (2013). *A quantum question order model supported by empirical tests of an a priori and precise prediction*. Topics in Cognitive Science 5(4), 689–710. doi:10.1111/tops.12040
- [ ] `Aerts2013` [E3] — Aerts, Gabora and Sozzo (2013). *Concepts and their dynamics: A quantum-theoretic modeling of human thought*. Topics in Cognitive Science 5(4), 737–772. doi:10.1111/tops.12042
- [ ] `Wang2014` [E3] — Wang et al. (2014). *Context effects produced by question orders reveal quantum nature of human judgments*. Proceedings of the National Academy of Sciences 111(26), 9431–9436. doi:10.1073/pnas.1407756111
- [ ] `Khrennikov2014` [E2] — Khrennikov et al. (2014). *Quantum models for psychological measurements: An unsolved problem*. PLoS ONE 9(10), e110909. doi:10.1371/journal.pone.0110909
- [ ] `Busemeyer2015` [E1] — Busemeyer and Wang (2015). *What is quantum cognition, and how is it applied to psychology?*. Current Directions in Psychological Science 24(3), 163–169. doi:10.1177/0963721414568663
- [ ] `Kvam2015` [E3] — Kvam et al. (2015). *Interference effects of choice on confidence: Quantum characteristics of evidence accumulation*. Proceedings of the National Academy of Sciences 112(34), 10645–10650. doi:10.1073/pnas.1500688112
- [ ] `Yearsley2016a` [E2] — Yearsley and Busemeyer (2016). *Quantum cognition and decision theories: A tutorial*. Journal of Mathematical Psychology 74, 99–116. doi:10.1016/j.jmp.2015.11.005
- [ ] `Wang2016` [E3] — Wang and Busemeyer (2016). *Interference effects of categorization on decision making*. Cognition 150, 133–149. doi:10.1016/j.cognition.2016.01.019
- [ ] `Yearsley2016b` [E3] — Yearsley and Pothos (2016). *Zeno's paradox in decision-making*. Proceedings of the Royal Society B: Biological Sciences 283(1828), 20160291. doi:10.1098/rspb.2016.0291
- [ ] `Dzhafarov2016a` [E2] — Dzhafarov and Kujala (2016). *Context–content systems of random variables: The Contextuality-by-Default theory*. Journal of Mathematical Psychology 74, 11–33. doi:10.1016/j.jmp.2016.04.010
- [ ] `Yearsley2017` [E2] — Yearsley (2017). *Advanced tools and concepts for quantum cognition: A tutorial*. Journal of Mathematical Psychology 78, 24–39. doi:10.1016/j.jmp.2016.07.005
- [ ] `Pothos2017` [E2] — Pothos et al. (2017). *The rational status of quantum cognition*. Journal of Experimental Psychology: General 146(7), 968–987. doi:10.1037/xge0000312
- [ ] `Trueblood2017a` [E3] — Trueblood, Yearsley and Pothos (2017). *A quantum probability framework for human probabilistic inference*. Journal of Experimental Psychology: General 146(9), 1307–1341. doi:10.1037/xge0000326
- [ ] `Broekaert2017` [E2] — Broekaert et al. (2017). *Quantum-like dynamics applied to cognition: A consideration of available options*. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 375(2106), 20160387. doi:10.1098/rsta.2016.0387
- [ ] `Aerts2017` [E4] — Aerts et al. (2017). *Testing quantum models of conjunction fallacy on the World Wide Web*. International Journal of Theoretical Physics 56(12), 3744–3756. doi:10.1007/s10773-017-3288-8
- [ ] `Busemeyer2018` [E3] — Busemeyer and Wang (2018). *Hilbert space multidimensional theory*. Psychological Review 125(4), 572–591. doi:10.1037/rev0000106
- [ ] `Cervantes2018` [E3] — Cervantes and Dzhafarov (2018). *Snow Queen is evil and beautiful: Experimental evidence for probabilistic contextuality in human choices*. Decision 5(3), 193–204. doi:10.1037/dec0000095
- [ ] `Basieva2019` [E3] — Basieva et al. (2019). *True contextuality beats direct influences in human decision making*. Journal of Experimental Psychology: General 148(11), 1925–1937. doi:10.1037/xge0000585
- [ ] `Busemeyer2020` [E2] — Busemeyer et al. (2020). *Application of quantum–Markov open system models to human cognition and decision*. Entropy 22(9), 990. doi:10.3390/e22090990
- [ ] `Ozawa2020` [E2] — Ozawa and Khrennikov (2020). *Application of theory of quantum instruments to psychology: Combination of question order effect with response replicability effect*. Entropy 22(1), 37. doi:10.3390/e22010037
- [ ] `Yukalov2020` [E2] — Yukalov (2020). *Evolutionary processes in quantum decision theory*. Entropy 22(6), 681. doi:10.3390/e22060681
- [ ] `Kvam2021` [E3] — Kvam, Busemeyer and Pleskac (2021). *Temporal oscillations in preference strength provide evidence for an open system model of constructed preference*. Scientific Reports 11, 8169. doi:10.1038/s41598-021-87659-0
- [ ] `Epping2023` [E3] — Epping et al. (2023). *Open system model of choice and response time*. Journal of Choice Modelling 49, 100453. doi:10.1016/j.jocm.2023.100453
- [ ] `Khrennikov2023a` [E2] — Khrennikov (2023). *Open systems, quantum probability, and logic for quantum-like modeling in biology, cognition, and decision-making*. Entropy 25(6), 886. doi:10.3390/e25060886
- [ ] `Waddup2023` [E3] — Waddup et al. (2023). *Temporal Bell inequalities in cognition*. Psychonomic Bulletin & Review 30(5), 1946–1953. doi:10.3758/s13423-023-02275-5
- [ ] `Huang2025a` [E3] — Huang et al. (2025). *Bridging the gap between subjective probability and probability judgments: the Quantum Sequential Sampler*. Psychological Review 132(4), 916–955. doi:10.1037/rev0000489
- [ ] `Bruza2009` [E2] — Bruza et al. (2009). *Is there something quantum-like about the human mental lexicon?*. Journal of Mathematical Psychology 53(5), 363–377. doi:10.1016/j.jmp.2009.04.004
- [ ] `Blutner2013` [E2] — Blutner, Pothos and Bruza (2013). *A quantum probability perspective on borderline vagueness*. Topics in Cognitive Science 5(4), 711–736. doi:10.1111/tops.12041
- [ ] `Pothos2013b` [E2] — Pothos, Busemeyer and Trueblood (2013). *A quantum geometric model of similarity*. Psychological Review 120(3), 679–696. doi:10.1037/a0033142
- [ ] `Trueblood2017b` [E3] — Trueblood and Hemmer (2017). *The generalized quantum episodic memory model*. Cognitive Science 41(8), 2089–2125. doi:10.1111/cogs.12460
- [ ] `Costello2014` [E3] — Costello and Watts (2014). *Surprisingly rational: probability theory plus noise explains biases in judgment*. Psychological Review 121(3), 463–480. doi:10.1037/a0037010
- [ ] `BoyerKassem2016` [E3] — Boyer-Kassem, Duchêne and Guerci (2016). *Quantum-like models cannot account for the conjunction fallacy*. Theory and Decision 81(4), 479–510. doi:10.1007/s11238-016-9549-9
- [ ] `Dzhafarov2016b` [E3] — Dzhafarov, Zhang and Kujala (2016). *Is there contextuality in behavioural and social systems?*. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374(2058), 20150099. doi:10.1098/rsta.2015.0099
- [ ] `Busemeyer2017b` [E3] — Busemeyer and Wang (2017). *Is there a problem with quantum models of psychological measurements?*. PLoS ONE 12(11), e0187733. doi:10.1371/journal.pone.0187733
- [ ] `Kellen2018` [E2] — Kellen, Singmann and Batchelder (2018). *Classic-probability accounts of mirrored (quantum-like) order effects in human judgments*. Decision 5(4), 323–338. doi:10.1037/dec0000080
- [ ] `Costello2018` [E3] — Costello and Watts (2018). *Invariants in probabilistic reasoning*. Cognitive Psychology 100, 1–16. doi:10.1016/j.cogpsych.2017.11.003
- [ ] `MartinezMartinez2016` [E2] — Martínez-Martínez and Sánchez-Burillo (2016). *Quantum Stochastic Walks on Networks for Decision-Making*. Scientific Reports 6, 23812. doi:10.1038/srep23812
- [ ] `Waddup2021` [E3] — Waddup et al. (2021). *Sensitivity to Context in Human Interactions*. Mathematics 9(21), 2784. doi:10.3390/math9212784
- [ ] `Busemeyer2017a` [E2] — Busemeyer, Fakhari and Kvam (2017). *Neural implementation of operations used in quantum cognition*. Progress in Biophysics and Molecular Biology 130(Part A), 53–60. doi:10.1016/j.pbiomolbio.2017.04.007
- [ ] `Khrennikov2018` [E2] — Khrennikov et al. (2018). *Quantum probability in decision making from quantum information representation of neuronal states*. Scientific Reports 8, 16225. doi:10.1038/s41598-018-34531-3
- [ ] `Khrennikov2025a` [E2] — Khrennikov et al. (2025). *Coupling quantum-like cognition with the neuronal networks within generalized probability theory*. Journal of Mathematical Psychology 125, 102923. doi:10.1016/j.jmp.2025.102923
- [ ] `Khrennikov2025b` [E2] — Khrennikov, Iriki and Basieva (2025). *Constructing a bridge between functioning of oscillatory neuronal networks and quantum-like cognition along with quantum-inspired computation and AI*. BioSystems 257, 105573. doi:10.1016/j.biosystems.2025.105573

**Reviews (9)**

- [ ] `Pothos2022` — Pothos and Busemeyer (2022). *Quantum cognition*. Annual Review of Psychology 73(1), 749–778. doi:10.1146/annurev-psych-033020-123501 — *also needed for Survey 1 (`Pothos2022`)*
- [ ] `Widdows2024` — Widdows et al. (2024). *Quantum Natural Language Processing*. KI – Künstliche Intelligenz 38(4), 293–310. doi:10.1007/s13218-024-00861-w
- [ ] `Liu2023` — Liu et al. (2023). *A Survey of Quantum-cognitively Inspired Sentiment Analysis Models*. ACM Computing Surveys 56(1), 1–37. doi:10.1145/3604550
- [ ] `Yan2021b` — Yan, Iliyasu and Hirota (2021). *Emotion Space Modelling for Social Robots*. Engineering Applications of Artificial Intelligence 100, 104178. doi:10.1016/j.engappai.2021.104178
- [ ] `Ashtiani2015` — Ashtiani and Azgomi (2015). *A survey of quantum-like approaches to decision making and cognition*. Mathematical Social Sciences 75, 49–80. doi:10.1016/j.mathsocsci.2015.02.004
- [ ] `Khrennikov2022` — Khrennikov (2022). *Quantum probability for modeling cognition, decision making, and artificial intelligence*. Infinite Dimensional Analysis, Quantum Probability and Applications. doi:10.1007/978-3-031-06170-7_4
- [ ] `Yan2024` — Yan et al. (2024). *Quantum robotics: a review of emerging trends*. Quantum Machine Intelligence 6(2), 86. doi:10.1007/s42484-024-00225-5 — *also needed for Survey 1 (`Yan2024`)*
- [ ] `Huang2025b` — Huang et al. (2025). *An overview of the quantum cognition research program*. Psychonomic Bulletin & Review 32, 2507–2556. doi:10.3758/s13423-025-02675-9
- [ ] `Khrennikov2026` — Khrennikov (2026). *Quantum-like cognition and AI toward the convergence of natural and artificial intelligence*. Discover Artificial Intelligence 6, 167. doi:10.1007/s44163-026-00909-w

**Background works (27)**

- [ ] `vonNeumann1932` — von Neumann (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. —
- [ ] `Savage1954` — Savage (1954). *The Foundations of Statistics*. John Wiley & Sons. —
- [ ] `Ellsberg1961` — Ellsberg (1961). *Risk, Ambiguity, and the Savage Axioms*. The Quarterly Journal of Economics 75(4), 643–669. doi:10.2307/1884324
- [ ] `Tversky1974` — Tversky and Kahneman (1974). *Judgment under Uncertainty: Heuristics and Biases*. Science 185(4157), 1124–1131. doi:10.1126/science.185.4157.1124
- [ ] `Tversky1983` — Tversky and Kahneman (1983). *Extensional versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment*. Psychological Review 90(4), 293–315. doi:10.1037/0033-295X.90.4.293
- [ ] `Shafir1992` — Shafir and Tversky (1992). *Thinking through Uncertainty: Nonconsequential Reasoning and Choice*. Cognitive Psychology 24(4), 449–474. doi:10.1016/0010-0285(92)90015-T
- [ ] `Biamonte2017` — Biamonte et al. (2017). *Quantum machine learning*. Nature 549(7671), 195–202. doi:10.1038/nature23474 — *also needed for Survey 1 (`Biamonte2017`)*
- [ ] `Binz2023` — Binz and Schulz (2023). *Using Cognitive Psychology to Understand GPT-3*. Proceedings of the National Academy of Sciences 120(6), e2218523120. doi:10.1073/pnas.2218523120
- [ ] `Tjuatja2024` — Tjuatja et al. (2024). *Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design*. Transactions of the Association for Computational Linguistics 12, 1011–1026. doi:10.1162/tacl_a_00685
- [ ] `Boyajian2020` — Boyajian et al. (2020). *On the Convergence of Projective-Simulation-Based Reinforcement Learning in Markov Decision Processes*. Quantum Machine Intelligence 2(2), 13. doi:10.1007/s42484-020-00023-9
- [ ] `Flamini2020` — Flamini et al. (2020). *Photonic Architecture for Reinforcement Learning*. New Journal of Physics 22(4), 045002. doi:10.1088/1367-2630/ab783c
- [ ] `Saggio2021` — Saggio et al. (2021). *Experimental Quantum Speed-Up in Reinforcement Learning Agents*. Nature 591(7849), 229–233. doi:10.1038/s41586-021-03242-7
- [ ] `Flamini2024` — Flamini et al. (2024). *Towards Interpretable Quantum Machine Learning via Single-Photon Quantum Walks*. Quantum Science and Technology 9(4), 045011. doi:10.1088/2058-9565/ad5907
- [ ] `Eisert1999` — Eisert, Wilkens and Lewenstein (1999). *Quantum Games and Quantum Strategies*. Physical Review Letters 83(15), 3077–3080. doi:10.1103/PhysRevLett.83.3077
- [ ] `Lawless2025` — Lawless and Moskowitz (2025). *An Entropy Approach to Interdependent Human–Machine Teams*. Entropy 27(2), 176. doi:10.3390/e27020176
- [ ] `Luckcuck2019` — Luckcuck et al. (2019). *Formal Specification and Verification of Autonomous Robotic Systems: A Survey*. ACM Computing Surveys 52(5), 100:1–100:41. doi:10.1145/3342355
- [ ] `Dreossi2019` — Dreossi et al. (2019). *VerifAI: A Toolkit for the Formal Design and Analysis of Artificial Intelligence-Based Systems*. Computer Aided Verification (CAV 2019). doi:10.1007/978-3-030-25540-4_25
- [ ] `Bergholm2018` — Bergholm et al. (2018). *PennyLane: Automatic differentiation of hybrid quantum-classical computations*. arXiv preprint. arXiv:1811.04968
- [ ] `Broughton2020` — Broughton et al. (2020). *TensorFlow Quantum: A Software Framework for Quantum Machine Learning*. arXiv preprint. arXiv:2003.02989
- [ ] `Tegmark2000` — Tegmark (2000). *Importance of quantum decoherence in brain processes*. Physical Review E 61(4), 4194–4206. doi:10.1103/PhysRevE.61.4194
- [ ] `Friston2010` — Friston (2010). *The free-energy principle: a unified brain theory?*. Nature Reviews Neuroscience 11(2), 127–138. doi:10.1038/nrn2787
- [ ] `Clark2013` — Clark (2013). *Whatever next? Predictive brains, situated agents, and the future of cognitive science*. Behavioral and Brain Sciences 36(3), 181–204. doi:10.1017/S0140525X12000477
- [ ] `Hameroff2014` — Hameroff and Penrose (2014). *Consciousness in the universe: A review of the `Orch OR' theory*. Physics of Life Reviews 11(1), 39–78. doi:10.1016/j.plrev.2013.08.002
- [ ] `Kalman1960` — Kalman (1960). *A new approach to linear filtering and prediction problems*. Journal of Basic Engineering 82(1), 35–45. doi:10.1115/1.3662552
- [ ] `Haykin2001` — Haykin (2001). *Kalman Filtering and Neural Networks*. Wiley. doi:10.1002/0471221546
- [ ] `Blanke2016` — Blanke et al. (2016). *Diagnosis and Fault-Tolerant Control*. Springer. doi:10.1007/978-3-662-47943-8
- [ ] `Gao2021` — Gao et al. (2021). *Design of a discrete-time fault-tolerant quantum filter and fault detector*. IEEE Transactions on Cybernetics 51(2), 889–899. doi:10.1109/TCYB.2019.2899877

## 3. All cited works (212)

Group: A application study, T theory and evidence study, Rv review, B background, E5 excluded under E5 (reviewed in Survey 1), M method reference. Level: evidence level E1–E6 (graded studies only). "also S1" = also cited in Survey 1.

| # | Key | Authors | Year | Title | Venue | DOI / arXiv | Group · Level · Full text |
|---|---|---|---|---|---|---|---|
| 1 | `Aaronson2015` | Aaronson | 2015 | Read the fine print | Nature Physics 11(4), 291–293 | doi:10.1038/nphys3272 | B · yes · also S1 |
| 2 | `Acuto2022` | Acuto et al. | 2022 | Variational Quantum Soft Actor-Critic for Robotic Arm Control | arXiv preprint | arXiv:2212.11681 | E5 · yes · also S1 |
| 3 | `Aerts2000` | Aerts, D'Hondt and Gabora | 2000 | Why the Disjunction in Quantum Logic Is Not Classical | Foundations of Physics 30(9), 1473–1480 | doi:10.1023/A:1026457918361 | T · E2 · no |
| 4 | `Aerts2009` | Aerts | 2009 | Quantum Structure in Cognition | Journal of Mathematical Psychology 53(5), 314–348 | doi:10.1016/j.jmp.2009.04.005 | T · E3 · yes |
| 5 | `Aerts2011a` | Aerts and Sozzo | 2011 | Quantum Structure in Cognition: Why and How Concepts Are Entangled | Quantum Interaction: 5th International Symposium, QI 2011, Aberdeen, UK, June 26–29, 2011, Revised Selected Papers | doi:10.1007/978-3-642-24971-6_12 | T · E3 · yes |
| 6 | `Aerts2011b` | Aerts et al. | 2011 | Quantum Structure in Cognition: Fundamentals and Applications | Proceedings of the Fifth International Conference on Quantum, Nano and Micro Technologies (ICQNM 2011) | arXiv:1104.3344 | T · E2 · yes |
| 7 | `Aerts2011c` | Aerts et al. | 2011 | A Quantum-Conceptual Explanation of Violations of Expected Utility in Economics | Quantum Interaction: 5th International Symposium, QI 2011, Aberdeen, UK, June 26–29, 2011, Revised Selected Papers | doi:10.1007/978-3-642-24971-6_19 | T · E3 · yes |
| 8 | `Aerts2011d` | Aerts, Czachor and Sozzo | 2011 | Quantum Interaction Approach in Cognition, Artificial Intelligence and Robotics | Proceedings of the Fifth International Conference on Quantum, Nano and Micro Technologies (ICQNM 2011) | arXiv:1104.3345 | A · E1 · yes |
| 9 | `Aerts2013` | Aerts, Gabora and Sozzo | 2013 | Concepts and their dynamics: A quantum-theoretic modeling of human thought | Topics in Cognitive Science 5(4), 737–772 | doi:10.1111/tops.12042 | T · E3 · no |
| 10 | `Aerts2017` | Aerts et al. | 2017 | Testing quantum models of conjunction fallacy on the World Wide Web | International Journal of Theoretical Physics 56(12), 3744–3756 | doi:10.1007/s10773-017-3288-8 | T · E4 · no |
| 11 | `Aerts2017b` | Aerts and Sassoli de Bianchi | 2017 | Beyond-quantum modeling of question order effects and response replicability in psychological measurements | Journal of Mathematical Psychology 79, 104–120 | arXiv:1508.03686 | T · E3 · yes |
| 12 | `Aerts2026` | Aerts et al. | 2026 | Identifying Quantum Structure in AI Language: Evidence for Evolutionary Convergence of Human and Artificial Cognition | Entropy 28(6), 622 | doi:10.3390/e28060622 | A · E4 · no |
| 13 | `Asano2026` | Asano and Khrennikov | 2026 | Quantum-like models of cognition and decision making: open-systems and Gorini–Kossakowski–Sudarshan–Lindblad dynamics | arXiv preprint | arXiv:2604.18643 | T · E2 · yes |
| 14 | `Ashtiani2015` | Ashtiani and Azgomi | 2015 | A survey of quantum-like approaches to decision making and cognition | Mathematical Social Sciences 75, 49–80 | doi:10.1016/j.mathsocsci.2015.02.004 | Rv · no |
| 15 | `Ashtiani2019` | Ashtiani and Abdollahi Azgomi | 2019 | A novel trust evolution algorithm based on a quantum-like model of computational trust | Cognition, Technology & Work 21(2), 201–224 | doi:10.1007/s10111-018-0496-9 | A · E4 · no |
| 16 | `Basieva2019` | Basieva et al. | 2019 | True contextuality beats direct influences in human decision making | Journal of Experimental Psychology: General 148(11), 1925–1937 | doi:10.1037/xge0000585 | T · E3 · no |
| 17 | `Benioff1998` | Benioff | 1998 | Quantum Robots and Environments | Physical Review A 58(2), 893–904 | doi:10.1103/PhysRevA.58.893 | B · yes · also S1 |
| 18 | `Bergholm2018` | Bergholm et al. | 2018 | PennyLane: Automatic differentiation of hybrid quantum-classical computations | arXiv preprint | arXiv:1811.04968 | B · no |
| 19 | `Berner2021` | Berner, Fortuin and Landman | 2021 | Quantum Bayesian Neural Networks | arXiv preprint | doi:10.48550/arXiv.2107.09599 | B · yes |
| 20 | `Biamonte2017` | Biamonte et al. | 2017 | Quantum machine learning | Nature 549(7671), 195–202 | doi:10.1038/nature23474 | B · no · also S1 |
| 21 | `Binz2023` | Binz and Schulz | 2023 | Using Cognitive Psychology to Understand GPT-3 | Proceedings of the National Academy of Sciences 120(6), e2218523120 | doi:10.1073/pnas.2218523120 | B · no |
| 22 | `Blanke2016` | Blanke et al. | 2016 | Diagnosis and Fault-Tolerant Control | Springer | doi:10.1007/978-3-662-47943-8 | B · no |
| 23 | `Blutner2013` | Blutner, Pothos and Bruza | 2013 | A quantum probability perspective on borderline vagueness | Topics in Cognitive Science 5(4), 711–736 | doi:10.1111/tops.12041 | T · E2 · no |
| 24 | `Boyajian2020` | Boyajian et al. | 2020 | On the Convergence of Projective-Simulation-Based Reinforcement Learning in Markov Decision Processes | Quantum Machine Intelligence 2(2), 13 | doi:10.1007/s42484-020-00023-9 | B · no |
| 25 | `BoyerKassem2016` | Boyer-Kassem, Duchêne and Guerci | 2016 | Quantum-like models cannot account for the conjunction fallacy | Theory and Decision 81(4), 479–510 | doi:10.1007/s11238-016-9549-9 | T · E3 · no |
| 26 | `Briegel2012` | Briegel and De las Cuevas | 2012 | Projective Simulation for Artificial Intelligence | Scientific Reports 2, 400 | doi:10.1038/srep00400 | A · E4 · yes · also S1 |
| 27 | `Broekaert2017` | Broekaert et al. | 2017 | Quantum-like dynamics applied to cognition: A consideration of available options | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 375(2106), 20160387 | doi:10.1098/rsta.2016.0387 | T · E2 · no |
| 28 | `Broughton2020` | Broughton et al. | 2020 | TensorFlow Quantum: A Software Framework for Quantum Machine Learning | arXiv preprint | arXiv:2003.02989 | B · no |
| 29 | `Bruza2009` | Bruza et al. | 2009 | Is there something quantum-like about the human mental lexicon? | Journal of Mathematical Psychology 53(5), 363–377 | doi:10.1016/j.jmp.2009.04.004 | T · E2 · no |
| 30 | `Bruza2015` | Bruza, Wang and Busemeyer | 2015 | Quantum cognition: A new theoretical approach to psychology | Trends in Cognitive Sciences 19(7), 383–393 | doi:10.1016/j.tics.2015.05.001 | T · E3 · yes |
| 31 | `Busemeyer2006` | Busemeyer, Wang and Townsend | 2006 | Quantum Dynamics of Human Decision-Making | Journal of Mathematical Psychology 50(3), 220–241 | doi:10.1016/j.jmp.2006.01.003 | T · E2 · no |
| 32 | `Busemeyer2009` | Busemeyer, Wang and Lambert-Mogiliansky | 2009 | Empirical Comparison of Markov and Quantum Models of Decision Making | Journal of Mathematical Psychology 53(5), 423–433 | doi:10.1016/j.jmp.2009.03.002 | T · E3 · no |
| 33 | `Busemeyer2011` | Busemeyer et al. | 2011 | A Quantum Theoretical Explanation for Probability Judgment Errors | Psychological Review 118(2), 193–218 | doi:10.1037/a0022542 | T · E3 · yes |
| 34 | `Busemeyer2012` | Busemeyer and Bruza | 2012 | Quantum Models of Cognition and Decision | Cambridge University Press | doi:10.1017/CBO9780511997716 | T · E3 · yes · also S1 |
| 35 | `Busemeyer2015` | Busemeyer and Wang | 2015 | What is quantum cognition, and how is it applied to psychology? | Current Directions in Psychological Science 24(3), 163–169 | doi:10.1177/0963721414568663 | T · E1 · no |
| 36 | `Busemeyer2017a` | Busemeyer, Fakhari and Kvam | 2017 | Neural implementation of operations used in quantum cognition | Progress in Biophysics and Molecular Biology 130(Part A), 53–60 | doi:10.1016/j.pbiomolbio.2017.04.007 | T · E2 · no |
| 37 | `Busemeyer2017b` | Busemeyer and Wang | 2017 | Is there a problem with quantum models of psychological measurements? | PLoS ONE 12(11), e0187733 | doi:10.1371/journal.pone.0187733 | T · E3 · no |
| 38 | `Busemeyer2018` | Busemeyer and Wang | 2018 | Hilbert space multidimensional theory | Psychological Review 125(4), 572–591 | doi:10.1037/rev0000106 | T · E3 · no |
| 39 | `Busemeyer2019` | Busemeyer, Kvam and Pleskac | 2019 | Markov versus quantum dynamic models of belief change during evidence monitoring | Scientific Reports 9, 18025 | doi:10.1038/s41598-019-54383-9 | T · E3 · yes |
| 40 | `Busemeyer2020` | Busemeyer et al. | 2020 | Application of quantum–Markov open system models to human cognition and decision | Entropy 22(9), 990 | doi:10.3390/e22090990 | T · E2 · no |
| 41 | `Busemeyer2025` | Busemeyer et al. | 2025 | Incorporating episodic memory into quantum models of judgment and decision | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 383(2309), 20240387 | doi:10.1098/rsta.2024.0387 | T · E2 · yes |
| 42 | `Cerezo2021` | Cerezo et al. | 2021 | Cost function dependent barren plateaus in shallow parametrized quantum circuits | Nature Communications 12, 1791 | doi:10.1038/s41467-021-21728-w | B · yes · also S1 |
| 43 | `Cervantes2018` | Cervantes and Dzhafarov | 2018 | Snow Queen is evil and beautiful: Experimental evidence for probabilistic contextuality in human choices | Decision 5(3), 193–204 | doi:10.1037/dec0000095 | T · E3 · no |
| 44 | `Chella2022` | Chella et al. | 2022 | A Quantum Planner for Robot Motion | Mathematics 10(14), 2475 | doi:10.3390/math10142475 | E5 · yes · also S1 |
| 45 | `Chella2026` | Chella et al. | 2026 | An Architecture for a Quantum Teleo-Reactive Robot | Entropy 28(7), 731 | doi:10.3390/e28070731 | A · E4 · no |
| 46 | `Chen2020` | Chen et al. | 2020 | Variational Quantum Circuits for Deep Reinforcement Learning | IEEE Access 8, 141007–141024 | doi:10.1109/ACCESS.2020.3010470 | E5 · yes · also S1 |
| 47 | `Chen2024` | Chen | 2024 | An introduction to quantum reinforcement learning (QRL) | arXiv preprint | arXiv:2409.05846 | Rv · yes |
| 48 | `Clark2013` | Clark | 2013 | Whatever next? Predictive brains, situated agents, and the future of cognitive science | Behavioral and Brain Sciences 36(3), 181–204 | doi:10.1017/S0140525X12000477 | B · no |
| 49 | `Costello2014` | Costello and Watts | 2014 | Surprisingly rational: probability theory plus noise explains biases in judgment | Psychological Review 121(3), 463–480 | doi:10.1037/a0037010 | T · E3 · no |
| 50 | `Costello2018` | Costello and Watts | 2018 | Invariants in probabilistic reasoning | Cognitive Psychology 100, 1–16 | doi:10.1016/j.cogpsych.2017.11.003 | T · E3 · no |
| 51 | `Daglarli2025` | Daglarli | 2025 | A Generative Neuro-Cognitive Architecture Using Quantum Algorithms for the Autonomous Behavior of a Smart Agent in a Simulation Environment | Computers, Materials & Continua 84(3) | doi:10.32604/cmc.2025.065572 | A · E4 · yes · also S1 |
| 52 | `DeCarolis2025` | De Carolis et al. | 2025 | Quantum-Enhanced Social Robotics: The QUADRI Project | Adjunct Proceedings of the 33rd ACM Conference on User Modeling, Adaptation and Personalization (UMAP Adjunct '25) | doi:10.1145/3708319.3735545 | A · E1 · yes · also S1 |
| 53 | `Dong2006` | Dong et al. | 2006 | Quantum Robot: Structure, Algorithms and Applications | Robotica 24(4), 513–521 | doi:10.1017/S0263574705002596 | B · yes · also S1 |
| 54 | `Dong2008` | Dong et al. | 2008 | Quantum Reinforcement Learning | IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics 38(5), 1207–1220 | doi:10.1109/TSMCB.2008.925743 | A · E4 · no · also S1 |
| 55 | `Dong2012` | Dong et al. | 2012 | Robust Quantum-Inspired Reinforcement Learning for Robot Navigation | IEEE/ASME Transactions on Mechatronics 17(1), 86–97 | doi:10.1109/TMECH.2010.2090896 | A · E5 · yes · also S1 |
| 56 | `Dreossi2019` | Dreossi et al. | 2019 | VerifAI: A Toolkit for the Formal Design and Analysis of Artificial Intelligence-Based Systems | Computer Aided Verification (CAV 2019) | doi:10.1007/978-3-030-25540-4_25 | B · no |
| 57 | `Dunjko2018` | Dunjko and Briegel | 2018 | Machine learning & artificial intelligence in the quantum domain: a review of recent progress | Reports on Progress in Physics 81(7), 074001 | doi:10.1088/1361-6633/aab406 | Rv · yes · also S1 |
| 58 | `Dzhafarov2016a` | Dzhafarov and Kujala | 2016 | Context–content systems of random variables: The Contextuality-by-Default theory | Journal of Mathematical Psychology 74, 11–33 | doi:10.1016/j.jmp.2016.04.010 | T · E2 · no |
| 59 | `Dzhafarov2016b` | Dzhafarov, Zhang and Kujala | 2016 | Is there contextuality in behavioural and social systems? | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374(2058), 20150099 | doi:10.1098/rsta.2015.0099 | T · E3 · no |
| 60 | `Eisert1999` | Eisert, Wilkens and Lewenstein | 1999 | Quantum Games and Quantum Strategies | Physical Review Letters 83(15), 3077–3080 | doi:10.1103/PhysRevLett.83.3077 | B · no |
| 61 | `Ellsberg1961` | Ellsberg | 1961 | Risk, Ambiguity, and the Savage Axioms | The Quarterly Journal of Economics 75(4), 643–669 | doi:10.2307/1884324 | B · no |
| 62 | `Epping2023` | Epping et al. | 2023 | Open system model of choice and response time | Journal of Choice Modelling 49, 100453 | doi:10.1016/j.jocm.2023.100453 | T · E3 · no |
| 63 | `Essalmi2025` | Essalmi, Garrido and Nashashibi | 2025 | Quantum game models for interaction-aware decision-making in automated driving | arXiv preprint | arXiv:2509.01582 | A · E4 · no |
| 64 | `Essalmi2026` | Essalmi, Garrido and Nashashibi | 2026 | Multi-Player, Multi-Strategy Quantum Game Model for Interaction-Aware Decision-Making in Automated Driving | arXiv preprint | arXiv:2602.03571 | A · E4 · yes · also S1 |
| 65 | `Fisher2015` | Fisher | 2015 | Quantum cognition: The possibility of processing with nuclear spins in the brain | Annals of Physics 362, 593–602 | doi:10.1016/j.aop.2015.08.020 | B · yes |
| 66 | `Flamini2020` | Flamini et al. | 2020 | Photonic Architecture for Reinforcement Learning | New Journal of Physics 22(4), 045002 | doi:10.1088/1367-2630/ab783c | B · no |
| 67 | `Flamini2024` | Flamini et al. | 2024 | Towards Interpretable Quantum Machine Learning via Single-Photon Quantum Walks | Quantum Science and Technology 9(4), 045011 | doi:10.1088/2058-9565/ad5907 | B · no |
| 68 | `Friston2010` | Friston | 2010 | The free-energy principle: a unified brain theory? | Nature Reviews Neuroscience 11(2), 127–138 | doi:10.1038/nrn2787 | B · no |
| 69 | `Fuyama2025` | Fuyama, Khrennikov and Ozawa | 2025 | Quantum-like cognition and decision-making in the light of quantum measurement theory | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 383(2309), 20240372 | doi:10.1098/rsta.2024.0372 | T · E2 · yes |
| 70 | `Gao2021` | Gao et al. | 2021 | Design of a discrete-time fault-tolerant quantum filter and fault detector | IEEE Transactions on Cybernetics 51(2), 889–899 | doi:10.1109/TCYB.2019.2899877 | B · no |
| 71 | `Gao2025` | Gao et al. | 2025 | Quantum-like evidence networks decision-making model | Engineering Applications of Artificial Intelligence 157, 111368 | doi:10.1016/j.engappai.2025.111368 | A · E3 · no |
| 72 | `Gkoumas2021` | Gkoumas et al. | 2021 | Quantum Cognitively Motivated Decision Fusion for Video Sentiment Analysis | Proceedings of the AAAI Conference on Artificial Intelligence | doi:10.1609/aaai.v35i1.16165 | A · E4 · no |
| 73 | `Guru2026` | Guru and Chauhan | 2026 | Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints | Companion manuscript, prepared for ACM Computing Surveys | — | M · own manuscript |
| 74 | `Hameroff2014` | Hameroff and Penrose | 2014 | Consciousness in the universe: A review of the `Orch OR' theory | Physics of Life Reviews 11(1), 39–78 | doi:10.1016/j.plrev.2013.08.002 | B · no |
| 75 | `Hangl2016` | Hangl et al. | 2016 | Robotic Playing for Hierarchical Complex Skill Learning | Proceedings of the 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | arXiv:1603.00794 | A · E5 · no |
| 76 | `Hangl2020` | Hangl et al. | 2020 | Skill Learning by Autonomous Robotic Playing Using Active Learning and Exploratory Behavior Composition | Frontiers in Robotics and AI 7, 42 | doi:10.3389/frobt.2020.00042 | A · E5 · no |
| 77 | `Haykin2001` | Haykin | 2001 | Kalman Filtering and Neural Networks | Wiley | doi:10.1002/0471221546 | B · no |
| 78 | `Henderson2018` | Henderson et al. | 2018 | Deep reinforcement learning that matters | Proceedings of the AAAI Conference on Artificial Intelligence | doi:10.1609/aaai.v32i1.11694 | B · yes |
| 79 | `Ho2022` | Ho and Hoorn | 2022 | Quantum Affective Processes for Multidimensional Decision-Making | Scientific Reports 12, 20468 | doi:10.1038/s41598-022-22855-0 | A · E2 · yes |
| 80 | `Hohenfeld2024` | Hohenfeld et al. | 2024 | Quantum Deep Reinforcement Learning for Robot Navigation Tasks | IEEE Access 12, 87217–87236 | doi:10.1109/ACCESS.2024.3417808 | E5 · yes · also S1 |
| 81 | `Hoorn2019` | Hoorn and Ho | 2019 | Robot Affect: the Amygdala as Bloch Sphere | arXiv preprint | arXiv:1911.12128 | A · E2 · no |
| 82 | `Huang2025a` | Huang et al. | 2025 | Bridging the gap between subjective probability and probability judgments: the Quantum Sequential Sampler | Psychological Review 132(4), 916–955 | doi:10.1037/rev0000489 | T · E3 · no |
| 83 | `Huang2025b` | Huang et al. | 2025 | An overview of the quantum cognition research program | Psychonomic Bulletin & Review 32, 2507–2556 | doi:10.3758/s13423-025-02675-9 | Rv · no |
| 84 | `Huang2025c` | Huang, Pleskac and Busemeyer | 2025 | Quantum Recognition Heuristics: A Tutorial Example of Quantum Heuristics | 2025 IEEE International Conference on Quantum Computing and Engineering (QCE) | doi:10.1109/QCE65121.2025.10486 | T · E2 · yes |
| 85 | `Humr2023` | Humr, Canan and Demir | 2023 | Temporal Evolution of Trust in Artificial Intelligence-Supported Decision-Making | Proceedings of the Human Factors and Ergonomics Society Annual Meeting 67(1), 1936–1941 | doi:10.1177/21695067231193672 | A · E2 · no |
| 86 | `Humr2025` | Humr, Canan and Demir | 2025 | A Quantum Probability Approach to Improving Human–AI Decision Making | Entropy 27(2), 152 | doi:10.3390/e27020152 | A · E2 · yes · also S1 |
| 87 | `Humr2026` | Humr and Canan | 2026 | System Level Intervention for AI-Supported Decision-Making: A Quantum Cognition Perspective | Quantum AI and NLP (QNLPAI 2025) | doi:10.1007/978-3-032-13883-5_14 | A · E1 · no |
| 88 | `Imannezhad2026` | Imannezhad, Pothos and Wills | 2026 | Divergent Patterns of Probabilistic Reasoning in Humans and GPT-5 | Frontiers in Psychology 17, 1782184 | doi:10.3389/fpsyg.2026.1782184 | A · E4 · no |
| 89 | `Jerbi2021` | Jerbi et al. | 2021 | Parametrized Quantum Policies for Reinforcement Learning | Advances in Neural Information Processing Systems | arXiv:2103.05577 | E5 · yes · also S1 |
| 90 | `Kak2018` | Kak | 2018 | Order Effects for Queries in Intelligent Systems | arXiv preprint | arXiv:1804.02759 | A · E2 · no |
| 91 | `Kalman1960` | Kalman | 1960 | A new approach to linear filtering and prediction problems | Journal of Basic Engineering 82(1), 35–45 | doi:10.1115/1.3662552 | B · no |
| 92 | `Kang2026` | Kang | 2026 | Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat | arXiv preprint | arXiv:2607.17219 | A · E4 · no |
| 93 | `Kellen2018` | Kellen, Singmann and Batchelder | 2018 | Classic-probability accounts of mirrored (quantum-like) order effects in human judgments | Decision 5(4), 323–338 | doi:10.1037/dec0000080 | T · E2 · no |
| 94 | `Khoshnoud2020` | Khoshnoud et al. | 2020 | Quantum Cooperative Robotics and Autonomy | arXiv preprint | arXiv:2008.12230 | E5 · yes · also S1 |
| 95 | `Khrennikov1999` | Khrennikov | 1999 | Classical and Quantum Mechanics on Information Spaces with Applications to Cognitive, Psychological, Social, and Anomalous Phenomena | Foundations of Physics 29(7), 1065–1098 | doi:10.1023/A:1018885632116 | T · E2 · yes |
| 96 | `Khrennikov2010` | Khrennikov | 2010 | Ubiquitous Quantum Structure: From Psychology to Finance | Springer | doi:10.1007/978-3-642-05101-2 | T · E2 · no |
| 97 | `Khrennikov2014` | Khrennikov et al. | 2014 | Quantum models for psychological measurements: An unsolved problem | PLoS ONE 9(10), e110909 | doi:10.1371/journal.pone.0110909 | T · E2 · no |
| 98 | `Khrennikov2018` | Khrennikov et al. | 2018 | Quantum probability in decision making from quantum information representation of neuronal states | Scientific Reports 8, 16225 | doi:10.1038/s41598-018-34531-3 | T · E2 · no |
| 99 | `Khrennikov2022` | Khrennikov | 2022 | Quantum probability for modeling cognition, decision making, and artificial intelligence | Infinite Dimensional Analysis, Quantum Probability and Applications | doi:10.1007/978-3-031-06170-7_4 | Rv · no |
| 100 | `Khrennikov2023a` | Khrennikov | 2023 | Open systems, quantum probability, and logic for quantum-like modeling in biology, cognition, and decision-making | Entropy 25(6), 886 | doi:10.3390/e25060886 | T · E2 · no |
| 101 | `Khrennikov2023b` | Khrennikov | 2024 | Contextual measurement model and quantum theory | Royal Society Open Science 11(3), 231953 | doi:10.1098/rsos.231953 | T · E2 · yes |
| 102 | `Khrennikov2025a` | Khrennikov et al. | 2025 | Coupling quantum-like cognition with the neuronal networks within generalized probability theory | Journal of Mathematical Psychology 125, 102923 | doi:10.1016/j.jmp.2025.102923 | T · E2 · no |
| 103 | `Khrennikov2025b` | Khrennikov, Iriki and Basieva | 2025 | Constructing a bridge between functioning of oscillatory neuronal networks and quantum-like cognition along with quantum-inspired computation and AI | BioSystems 257, 105573 | doi:10.1016/j.biosystems.2025.105573 | T · E2 · no |
| 104 | `Khrennikov2025c` | Khrennikov and Yamada | 2025 | Quantum-like representation of neuronal networks' activity: modeling ``mental entanglement'' | Frontiers in Human Neuroscience 19, 1685339 | doi:10.3389/fnhum.2025.1685339 | T · E2 · yes |
| 105 | `Khrennikov2026` | Khrennikov | 2026 | Quantum-like cognition and AI toward the convergence of natural and artificial intelligence | Discover Artificial Intelligence 6, 167 | doi:10.1007/s44163-026-00909-w | Rv · no |
| 106 | `Kitchenham2007` | Kitchenham and Charters | 2007 | Guidelines for performing Systematic Literature Reviews in Software Engineering | Keele University and Durham University | — | M · yes · also S1 |
| 107 | `Kong2026` | Kong et al. | 2026 | Emergence of Longitudinal Queues in Group Navigation: An Interpretable Approach via Projective Simulation | Biomimetics 11(3), 201 | doi:10.3390/biomimetics11030201 | A · E4 · no |
| 108 | `Kotseruba2020` | Kotseruba and Tsotsos | 2020 | 40 Years of Cognitive Architectures: Core Cognitive Abilities and Practical Applications | Artificial Intelligence Review 53(1), 17–94 | doi:10.1007/s10462-018-9646-y | B · yes |
| 109 | `Krizhevsky2012` | Krizhevsky, Sutskever and Hinton | 2012 | ImageNet classification with deep convolutional neural networks | Advances in Neural Information Processing Systems 25 (NIPS 2012) | https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html | B · yes |
| 110 | `Kvam2015` | Kvam et al. | 2015 | Interference effects of choice on confidence: Quantum characteristics of evidence accumulation | Proceedings of the National Academy of Sciences 112(34), 10645–10650 | doi:10.1073/pnas.1500688112 | T · E3 · no |
| 111 | `Kvam2021` | Kvam, Busemeyer and Pleskac | 2021 | Temporal oscillations in preference strength provide evidence for an open system model of constructed preference | Scientific Reports 11, 8169 | doi:10.1038/s41598-021-87659-0 | T · E3 · no |
| 112 | `Laird2017` | Laird, Lebiere and Rosenbloom | 2017 | A Standard Model of the Mind: Toward a Common Computational Framework across Artificial Intelligence, Cognitive Science, Neuroscience, and Robotics | AI Magazine 38(4), 13–26 | doi:10.1609/aimag.v38i4.2744 | B · yes |
| 113 | `Lanza2020` | Lanza, Solinas and Mastrogiovanni | 2020 | A Preliminary Study for a Quantum-like Robot Perception Model | arXiv preprint | arXiv:2006.02771 | A · E2 · yes |
| 114 | `Lanza2021` | Lanza, Solinas and Mastrogiovanni | 2021 | Multi-sensory Integration in a Quantum-Like Robot Perception Model | Experimental Robotics: The 17th International Symposium (ISER 2020) | doi:10.1007/978-3-030-71151-1_44 | A · E2 · yes |
| 115 | `Lauri2023` | Lauri, Hsu and Pajarinen | 2023 | Partially observable Markov decision processes in robotics: a survey | IEEE Transactions on Robotics 39(1), 21–40 | doi:10.1109/TRO.2022.3200138 | B · yes |
| 116 | `Lawless2020` | Lawless | 2020 | Quantum-Like Interdependence Theory Advances Autonomous Human–Machine Teams (A-HMTs) | Entropy 22(11), 1227 | doi:10.3390/e22111227 | A · E1 · no |
| 117 | `Lawless2023` | Lawless, Moskowitz and Doctor | 2023 | A Quantum-like Model of Interdependence for Embodied Human–Machine Teams: Reviewing the Path to Autonomy Facing Complexity and Uncertainty | Entropy 25(9), 1323 | doi:10.3390/e25091323 | A · E1 · yes · also S1 |
| 118 | `Lawless2025` | Lawless and Moskowitz | 2025 | An Entropy Approach to Interdependent Human–Machine Teams | Entropy 27(2), 176 | doi:10.3390/e27020176 | B · no |
| 119 | `Li2019` | Li, Wang and Melucci | 2019 | CNM: An Interpretable Complex-valued Network for Matching | Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) | doi:10.18653/v1/N19-1420 | A · E4 · no |
| 120 | `Li2021a` | Li et al. | 2021 | Quantum-inspired multimodal fusion for video sentiment analysis | Information Fusion 65, 58–71 | doi:10.1016/j.inffus.2020.08.006 | A · E4 · no |
| 121 | `Li2021b` | Li et al. | 2021 | Quantum-inspired Neural Network for Conversational Emotion Recognition | Proceedings of the AAAI Conference on Artificial Intelligence | doi:10.1609/aaai.v35i15.17567 | A · E4 · no |
| 122 | `Liu2023` | Liu et al. | 2023 | A Survey of Quantum-cognitively Inspired Sentiment Analysis Models | ACM Computing Surveys 56(1), 1–37 | doi:10.1145/3604550 | Rv · no |
| 123 | `Lo2025` | Lo, Sadrzadeh and Mansfield | 2025 | Quantum-Like Contextuality in Large Language Models | Proceedings of the Royal Society A | arXiv:2412.16806 | A · E4 · yes |
| 124 | `LopezIncera2020` | López-Incera et al. | 2020 | Development of Swarm Behavior in Artificial Learning Agents that Adapt to Different Foraging Environments | PLoS ONE 15(12), e0243628 | doi:10.1371/journal.pone.0243628 | A · E4 · no |
| 125 | `Lorenz2023` | Lorenz et al. | 2023 | QNLP in Practice: Running Compositional Models of Meaning on a Quantum Computer | Journal of Artificial Intelligence Research 76, 1305–1342 | doi:10.1613/jair.1.14329 | A · E5 · yes |
| 126 | `Luckcuck2019` | Luckcuck et al. | 2019 | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | ACM Computing Surveys 52(5), 100:1–100:41 | doi:10.1145/3342355 | B · no |
| 127 | `Lukac2007` | Lukac and Perkowski | 2007 | Quantum Mechanical Model of Emotional Robot Behaviors | Proceedings of the 37th International Symposium on Multiple-Valued Logic (ISMVL 2007) | — | A · E2 · no |
| 128 | `Maksimovic2025` | Maksimovic and Maksymov | 2025 | Quantum-Cognitive Neural Networks: Assessing Confidence and Uncertainty with Human Decision-Making Simulations | Big Data and Cognitive Computing 9(1), 12 | doi:10.3390/bdcc9010012 | A · E4 · no |
| 129 | `Maksymov2025` | Maksymov | 2025 | Cognition in superposition: quantum models in AI, finance, defence, gaming and collective behaviour | arXiv preprint | arXiv:2508.20098 | Rv · yes |
| 130 | `Mannone2022` | Mannone, Seidita and Chella | 2022 | Categories, Quantum Computing, and Swarm Robotics: A Case Study | Mathematics 10(3), 372 | doi:10.3390/math10030372 | E5 · yes · also S1 |
| 131 | `Mannone2024` | Mannone et al. | 2024 | Modeling Robotic Thinking and Creativity: A Classic–Quantum Dialogue | Mathematics 12(5), 642 | doi:10.3390/math12050642 | A · E2 · no |
| 132 | `MartinezMartinez2016` | Martínez-Martínez and Sánchez-Burillo | 2016 | Quantum Stochastic Walks on Networks for Decision-Making | Scientific Reports 6, 23812 | doi:10.1038/srep23812 | T · E2 · no |
| 133 | `Meghdadi2022` | Meghdadi, Akbarzadeh-T. and Javidan | 2022 | A quantum-like cognitive approach to modeling human biased selection behavior | Scientific Reports 12, 22545 | doi:10.1038/s41598-022-13757-2 | A · E3 · no |
| 134 | `Melnikov2018` | Melnikov, Makmal and Briegel | 2018 | Benchmarking Projective Simulation in Navigation Problems | IEEE Access 6, 64639–64648 | doi:10.1109/ACCESS.2018.2876494 | A · E4 · no |
| 135 | `Meyer2022` | Meyer et al. | 2022 | A survey on quantum reinforcement learning | arXiv preprint | arXiv:2211.03464 | Rv · yes · also S1 |
| 136 | `Moreira2014` | Moreira and Wichert | 2014 | Interference effects in quantum belief networks | Applied Soft Computing 25, 64–85 | doi:10.1016/j.asoc.2014.09.008 | A · E2 · no |
| 137 | `Moreira2016` | Moreira and Wichert | 2016 | Quantum-Like Bayesian Networks for Modeling Decision Making | Frontiers in Psychology 7, 11 | doi:10.3389/fpsyg.2016.00011 | A · E3 · no |
| 138 | `Moreira2017a` | Moreira | 2017 | Quantum Probabilistic Graphical Models for Cognition and Decision | Instituto Superior Técnico, Universidade de Lisboa | — | A · E3 · no |
| 139 | `Moreira2017b` | Moreira and Wichert | 2017 | Are quantum models for order effects quantum? | International Journal of Theoretical Physics 56, 4029–4046 | doi:10.1007/s10773-017-3424-5 | T · E3 · yes |
| 140 | `Moreira2020a` | Moreira et al. | 2020 | Towards a Quantum-Like Cognitive Architecture for Decision-Making | Behavioral and Brain Sciences 43, e17 | doi:10.1017/S0140525X19001687 | A · E1 · no |
| 141 | `Moreira2020b` | Moreira et al. | 2020 | Quantum-like influence diagrams for decision-making | Neural Networks 132, 190–210 | doi:10.1016/j.neunet.2020.07.009 | A · E3 · no |
| 142 | `Nausheen2025` | Nausheen et al. | 2025 | Quantum Natural Language Processing: A Comprehensive Review of Models, Methods, and Applications | arXiv preprint | arXiv:2504.09909 | Rv · yes |
| 143 | `Nebli2026` | Nebli, Saadatdoorabi and Yam | 2026 | Deep Sequence Modeling with Quantum Dynamics: Language as a Wave Function | arXiv preprint | arXiv:2602.22255 | A · E2 · no |
| 144 | `Ozawa2020` | Ozawa and Khrennikov | 2020 | Application of theory of quantum instruments to psychology: Combination of question order effect with response replicability effect | Entropy 22(1), 37 | doi:10.3390/e22010037 | T · E2 · no |
| 145 | `Ozawa2021` | Ozawa and Khrennikov | 2021 | Modeling combination of question order effect, response replicability effect, and QQ-equality with quantum instruments | Journal of Mathematical Psychology 100, 102491 | doi:10.1016/j.jmp.2020.102491 | T · E3 · yes |
| 146 | `Page2021` | Page et al. | 2021 | The PRISMA 2020 statement: an updated guideline for reporting systematic reviews | BMJ 372, n71 | doi:10.1136/bmj.n71 | M · yes · also S1 |
| 147 | `Paparo2014` | Paparo et al. | 2014 | Quantum Speedup for Active Learning Agents | Physical Review X 4(3), 031002 | doi:10.1103/PhysRevX.4.031002 | E5 · yes · also S1 |
| 148 | `Petschnigg2019` | Petschnigg et al. | 2019 | Quantum computation in robotic science and applications | 2019 International Conference on Robotics and Automation (ICRA) | doi:10.1109/ICRA.2019.8793768 | Rv · yes · also S1 |
| 149 | `Pothos2009` | Pothos and Busemeyer | 2009 | A Quantum Probability Explanation for Violations of `Rational' Decision Theory | Proceedings of the Royal Society B: Biological Sciences 276(1665), 2171–2178 | doi:10.1098/rspb.2009.0121 | T · E3 · no |
| 150 | `Pothos2013a` | Pothos and Busemeyer | 2013 | Can Quantum Probability Provide a New Direction for Cognitive Modeling? | Behavioral and Brain Sciences 36(3), 255–274 | doi:10.1017/S0140525X12001525 | T · E3 · no · also S1 |
| 151 | `Pothos2013b` | Pothos, Busemeyer and Trueblood | 2013 | A quantum geometric model of similarity | Psychological Review 120(3), 679–696 | doi:10.1037/a0033142 | T · E2 · no |
| 152 | `Pothos2017` | Pothos et al. | 2017 | The rational status of quantum cognition | Journal of Experimental Psychology: General 146(7), 968–987 | doi:10.1037/xge0000312 | T · E2 · no |
| 153 | `Pothos2022` | Pothos and Busemeyer | 2022 | Quantum cognition | Annual Review of Psychology 73(1), 749–778 | doi:10.1146/annurev-psych-033020-123501 | Rv · no · also S1 |
| 154 | `Preskill2018` | Preskill | 2018 | Quantum Computing in the NISQ era and beyond | Quantum 2, 79 | doi:10.22331/q-2018-08-06-79 | B · yes · also S1 |
| 155 | `Pushparaj2021` | Pushparaj et al. | 2021 | A quantum-inspired model for human-automation trust in air traffic controllers derived from functional Magnetic Resonance Imaging and correlated with behavioural indicators | Journal of Air Transport Management 97, 102143 | doi:10.1016/j.jairtraman.2021.102143 | A · E3 · no |
| 156 | `Ried2019` | Ried, Müller and Briegel | 2019 | Modelling Collective Motion Based on the Principle of Agency: General Framework and the Case of Marching Locusts | PLoS ONE 14(2), e0212044 | doi:10.1371/journal.pone.0212044 | A · E4 · no |
| 157 | `Roeder2023` | Roeder et al. | 2023 | A Quantum Model of Trust Calibration in Human–AI Interactions | Entropy 25(9), 1362 | doi:10.3390/e25091362 | A · E3 · no |
| 158 | `Saggio2021` | Saggio et al. | 2021 | Experimental Quantum Speed-Up in Reinforcement Learning Agents | Nature 591(7849), 229–233 | doi:10.1038/s41586-021-03242-7 | B · no |
| 159 | `Savage1954` | Savage | 1954 | The Foundations of Statistics | John Wiley & Sons | — | B · no |
| 160 | `Schuld2019` | Schuld and Killoran | 2019 | Quantum Machine Learning in Feature Hilbert Spaces | Physical Review Letters 122(4), 040504 | doi:10.1103/PhysRevLett.122.040504 | B · yes · also S1 |
| 161 | `Shafir1992` | Shafir and Tversky | 1992 | Thinking through Uncertainty: Nonconsequential Reasoning and Choice | Cognitive Psychology 24(4), 449–474 | doi:10.1016/0010-0285(92)90015-T | B · no |
| 162 | `She2021` | She, Han and Liu | 2021 | Application of quantum-like Bayesian network and belief entropy for interference effect in multi-attribute decision making problem | Computers & Industrial Engineering 157, 107307 | doi:10.1016/j.cie.2021.107307 | A · E4 · no |
| 163 | `Sinha2023` | Sinha, Macaluso and Klusch | 2025 | Nav-Q: Quantum Deep Reinforcement Learning for Collision-Free Navigation of Self-Driving Cars | Quantum Machine Intelligence 7(1), 19 | doi:10.1007/s42484-024-00226-4 | E5 · yes · also S1 |
| 164 | `Skolik2022` | Skolik, Jerbi and Dunjko | 2022 | Quantum Agents in the Gym: A Variational Quantum Algorithm for Deep Q-Learning | Quantum 6, 720 | doi:10.22331/q-2022-05-24-720 | E5 · yes · also S1 |
| 165 | `Song2022` | Song et al. | 2022 | Research on Quantum Cognition in Autonomous Driving | Scientific Reports 12, 300 | doi:10.1038/s41598-021-04239-y | A · E4 · no |
| 166 | `Sordoni2013` | Sordoni, Nie and Bengio | 2013 | Modeling term dependencies with quantum language models for IR | Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '13) | doi:10.1145/2484028.2484098 | A · E4 · no |
| 167 | `Stoudenmire2016` | Stoudenmire and Schwab | 2016 | Supervised Learning with Tensor Networks | Advances in Neural Information Processing Systems 29 (NIPS 2016) | arXiv:1605.05775 | A · E4 · no |
| 168 | `Sutton2018` | Sutton and Barto | 2018 | Reinforcement Learning: An Introduction | MIT Press | ISBN 978-0-262-03924-6 | B · yes · also S1 |
| 169 | `Svozil2025` | Svozil | 2025 | Quantum Contextuality for Contextual Word Embeddings | arXiv preprint | arXiv:2504.13824 | A · E2 · yes |
| 170 | `Tang2019` | Tang | 2019 | A quantum-inspired classical algorithm for recommendation systems | Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing (STOC 2019) | doi:10.1145/3313276.3316310 | B · yes · also S1 |
| 171 | `Tegmark2000` | Tegmark | 2000 | Importance of quantum decoherence in brain processes | Physical Review E 61(4), 4194–4206 | doi:10.1103/PhysRevE.61.4194 | B · no |
| 172 | `Thrun2005` | Thrun, Burgard and Fox | 2005 | Probabilistic Robotics | MIT Press | ISBN 978-0-262-20162-9 | B · yes · also S1 |
| 173 | `Tjuatja2024` | Tjuatja et al. | 2024 | Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design | Transactions of the Association for Computational Linguistics 12, 1011–1026 | doi:10.1162/tacl_a_00685 | B · no |
| 174 | `Trueblood2011` | Trueblood and Busemeyer | 2011 | A Quantum Probability Account of Order Effects in Inference | Cognitive Science 35(8), 1518–1552 | doi:10.1111/j.1551-6709.2011.01197.x | T · E3 · no |
| 175 | `Trueblood2017a` | Trueblood, Yearsley and Pothos | 2017 | A quantum probability framework for human probabilistic inference | Journal of Experimental Psychology: General 146(9), 1307–1341 | doi:10.1037/xge0000326 | T · E3 · no |
| 176 | `Trueblood2017b` | Trueblood and Hemmer | 2017 | The generalized quantum episodic memory model | Cognitive Science 41(8), 2089–2125 | doi:10.1111/cogs.12460 | T · E3 · no |
| 177 | `Tversky1974` | Tversky and Kahneman | 1974 | Judgment under Uncertainty: Heuristics and Biases | Science 185(4157), 1124–1131 | doi:10.1126/science.185.4157.1124 | B · no |
| 178 | `Tversky1983` | Tversky and Kahneman | 1983 | Extensional versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment | Psychological Review 90(4), 293–315 | doi:10.1037/0033-295X.90.4.293 | B · no |
| 179 | `Uprety2021` | Uprety, Gkoumas and Song | 2020 | A Survey of Quantum Theory Inspired Approaches to Information Retrieval | ACM Computing Surveys 53(5), 98:1–98:39 | doi:10.1145/3402179 | Rv · yes |
| 180 | `Uprety2024` | Uprety et al. | 2024 | Investigating Context Effects in Similarity Judgements in Large Language Models | arXiv preprint | arXiv:2408.10711 | A · E4 · no |
| 181 | `vanderMeer2025` | van der Meer et al. | 2025 | Modeling the quantum-like dynamics of human reliability ratings in Human–AI interactions by interaction dependent Hamiltonians | arXiv preprint | arXiv:2504.13918 | A · E3 · yes |
| 182 | `Veloz2024` | Veloz and Sobetska | 2024 | Analyzing the conjunction fallacy as a fact | arXiv preprint | arXiv:2402.13615 | T · E3 · yes |
| 183 | `vonNeumann1932` | von Neumann | 1932 | Mathematische Grundlagen der Quantenmechanik | Springer | — | B · no |
| 184 | `Waddup2021` | Waddup et al. | 2021 | Sensitivity to Context in Human Interactions | Mathematics 9(21), 2784 | doi:10.3390/math9212784 | T · E3 · no |
| 185 | `Waddup2023` | Waddup et al. | 2023 | Temporal Bell inequalities in cognition | Psychonomic Bulletin & Review 30(5), 1946–1953 | doi:10.3758/s13423-023-02275-5 | T · E3 · no |
| 186 | `Wang2013a` | Wang et al. | 2013 | The Potential of Using Quantum Theory to Build Models of Cognition | Topics in Cognitive Science 5(4), 672–688 | doi:10.1111/tops.12043 | T · E1 · no |
| 187 | `Wang2013b` | Wang and Busemeyer | 2013 | A quantum question order model supported by empirical tests of an a priori and precise prediction | Topics in Cognitive Science 5(4), 689–710 | doi:10.1111/tops.12040 | T · E3 · no |
| 188 | `Wang2014` | Wang et al. | 2014 | Context effects produced by question orders reveal quantum nature of human judgments | Proceedings of the National Academy of Sciences 111(26), 9431–9436 | doi:10.1073/pnas.1407756111 | T · E3 · no |
| 189 | `Wang2016` | Wang and Busemeyer | 2016 | Interference effects of categorization on decision making | Cognition 150, 133–149 | doi:10.1016/j.cognition.2016.01.019 | T · E3 · no |
| 190 | `Wei2022` | Wei et al. | 2022 | Deep Reinforcement Learning with Quantum-Inspired Experience Replay | IEEE Transactions on Cybernetics 52(9), 9326–9338 | doi:10.1109/TCYB.2021.3053414 | A · E4 · no |
| 191 | `Wichert2020` | Wichert, Moreira and Bruza | 2020 | Balanced Quantum-Like Bayesian Networks | Entropy 22(2), 170 | doi:10.3390/e22020170 | A · E3 · no |
| 192 | `Widdows2003` | Widdows and Peters | 2003 | Word Vectors and Quantum Logic: Experiments with negation and disjunction | Proceedings of the 8th Mathematics of Language Conference (MOL 8) | — | A · E4 · no |
| 193 | `Widdows2021` | Widdows, Kitto and Cohen | 2021 | Quantum Mathematics in Artificial Intelligence | Journal of Artificial Intelligence Research 72, 1307–1341 | doi:10.1613/jair.1.12702 | Rv · yes |
| 194 | `Widdows2023` | Widdows, Rani and Pothos | 2023 | Quantum Circuit Components for Cognitive Decision-Making | Entropy 25(4), 548 | doi:10.3390/e25040548 | A · E5 · yes · also S1 |
| 195 | `Widdows2024` | Widdows et al. | 2024 | Quantum Natural Language Processing | KI – Künstliche Intelligenz 38(4), 293–310 | doi:10.1007/s13218-024-00861-w | Rv · no |
| 196 | `Yan2019` | Yan et al. | 2019 | Quantum Structure for Modelling Emotion Space of Robots | Applied Sciences 9(16), 3351 | doi:10.3390/app9163351 | A · E2 · no |
| 197 | `Yan2021a` | Yan, Iliyasu and Hirota | 2021 | Conceptual Framework for Quantum Affective Computing and Its Use in Fusion of Multi-Robot Emotions | Electronics 10(2), 100 | doi:10.3390/electronics10020100 | A · E2 · yes · also S1 |
| 198 | `Yan2021b` | Yan, Iliyasu and Hirota | 2021 | Emotion Space Modelling for Social Robots | Engineering Applications of Artificial Intelligence 100, 104178 | doi:10.1016/j.engappai.2021.104178 | Rv · no |
| 199 | `Yan2021c` | Yan et al. | 2021 | Emotion Generation and Transition of Companion Robots Based on Plutchik's Model and Quantum Circuit Schemes | Security and Communication Networks 2021, 6802521 | doi:10.1155/2021/6802521 | A · E2 · no |
| 200 | `Yan2024` | Yan et al. | 2024 | Quantum robotics: a review of emerging trends | Quantum Machine Intelligence 6(2), 86 | doi:10.1007/s42484-024-00225-5 | Rv · no · also S1 |
| 201 | `Yearsley2016a` | Yearsley and Busemeyer | 2016 | Quantum cognition and decision theories: A tutorial | Journal of Mathematical Psychology 74, 99–116 | doi:10.1016/j.jmp.2015.11.005 | T · E2 · no |
| 202 | `Yearsley2016b` | Yearsley and Pothos | 2016 | Zeno's paradox in decision-making | Proceedings of the Royal Society B: Biological Sciences 283(1828), 20160291 | doi:10.1098/rspb.2016.0291 | T · E3 · no |
| 203 | `Yearsley2017` | Yearsley | 2017 | Advanced tools and concepts for quantum cognition: A tutorial | Journal of Mathematical Psychology 78, 24–39 | doi:10.1016/j.jmp.2016.07.005 | T · E2 · no |
| 204 | `Yukalov2011` | Yukalov and Sornette | 2011 | Decision Theory with Prospect Interference and Entanglement | Theory and Decision 70(3), 283–328 | doi:10.1007/s11238-010-9202-y | T · E3 · no |
| 205 | `Yukalov2016` | Yukalov and Sornette | 2016 | Quantum probability and quantum decision-making | Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374(2058), 20150100 | doi:10.1098/rsta.2015.0100 | T · E2 · yes |
| 206 | `Yukalov2018` | Yukalov, Yukalova and Sornette | 2018 | Information Processing by Networks of Quantum Decision Makers | Physica A: Statistical Mechanics and its Applications 492, 747–766 | doi:10.1016/j.physa.2017.11.004 | A · E2 · no |
| 207 | `Yukalov2020` | Yukalov | 2020 | Evolutionary processes in quantum decision theory | Entropy 22(6), 681 | doi:10.3390/e22060681 | T · E2 · no |
| 208 | `Yukalov2022` | Yukalov, Yukalova and Sornette | 2022 | Role of collective information in networks of quantum operating agents | Physica A: Statistical Mechanics and its Applications 598, 127365 | doi:10.1016/j.physa.2022.127365 | A · E2 · no |
| 209 | `Yukalov2023` | Yukalov | 2023 | Quantum operation of affective artificial intelligence | Laser Physics 33(6), 065204 | doi:10.1088/1555-6611/accf7a | A · E2 · no |
| 210 | `Yun2022` | Yun et al. | 2022 | Quantum Multi-Agent Reinforcement Learning via Variational Quantum Circuit Design | Proceedings of the 2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS) | doi:10.1109/ICDCS54860.2022.00151 | E5 · yes · also S1 |
| 211 | `Zhang2018` | Zhang et al. | 2018 | A Quantum Many-body Wave Function Inspired Language Modeling Approach | Proceedings of the 27th ACM International Conference on Information and Knowledge Management (CIKM 2018) | doi:10.1145/3269206.3271723 | A · E4 · no |
| 212 | `Zhang2025` | Zhang et al. | 2025 | Quantum-Inspired Semantic Matching Based on Neural Networks with the Duality of Density Matrices | Engineering Applications of Artificial Intelligence 140, 109667 | doi:10.1016/j.engappai.2024.109667 | A · E4 · no |
