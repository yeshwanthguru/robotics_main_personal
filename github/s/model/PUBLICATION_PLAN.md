# Publication plan — model paper

**Working title:** Order-Aware Human Models for Robot Questioning and Trust: A Quantum-Like Model with
Classical Baselines, Simulation Studies and Quantum-Circuit Execution

**Authors:** Yeshwanth Guru (corresponding; ORCID 0009-0007-6353-4033) and Dev Kunwar Singh Chauhan
(ORCID 0000-0002-1466-4567), Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai.

## 1. Place in the research programme

| Paper | Question | Status |
|---|---|---|
| Survey 1 (ACM Computing Surveys) | What can quantum technologies do for autonomous robots? | Manuscript in `github/k` |
| Survey 2 (Artificial Intelligence Review) | What can quantum-like (quantum-probability) models of decision-making do for autonomous agents? | Manuscript in `github/m` |
| Survey 3 (IEEE TNNLS) | Can a meta-learned orchestrator route between learning modalities on a resource-constrained robot? | Manuscript in `github/s` |
| **This paper** | Does an order-aware (quantum-like) human model help a robot that asks people questions, and what does it add over classical models? | Code, simulations and manuscript in `github/s/model` |

The paper turns the main open question of Survey 2 (quantum-like models have human evidence but almost
no tests in robots) into a testable model, and supplies Survey 3 with its fifth confidence signal: the
predictive uncertainty of a human model (Survey 3, Section XVII, and the dashed input of its Fig. 1).

## 2. What the paper can and cannot claim

Can claim (from the simulations and the published aggregate data):
- a complete, tested implementation of the quantum-like question-order model, three classical
  baselines and two trust-dynamics models, with circuit versions that reproduce the analytic
  probabilities on simulators and under realistic hardware noise models;
- when the models can be told apart, how many people that needs, and how individual differences
  change the answer;
- which questioning design a robot should use to recover unprimed answers;
- that asking about trust changes later trust under open-system dynamics but not under Markov
  dynamics, and how much data distinguishes the two.

Cannot claim until a human study is run: that real people in human–robot interaction follow the
quantum-like model, or that a robot using it performs better with real users. No result in the paper
comes from human participants other than the two published aggregate data sets (Clinton–Gore poll;
Prisoner's Dilemma disjunction effect).

## 3. Target venues (in order)

1. **IEEE Transactions on Cognitive and Developmental Systems** (computational models of cognition for
   robots; simulation papers with a clear model contribution are in scope). Template: IEEEtran
   journal, as prepared in `paper/`.
2. **Cognitive Systems Research** (Elsevier) or **Topics in Cognitive Science** (if the emphasis moves
   to the model comparison and identifiability results).
3. After a human study: **ACM Transactions on Human-Robot Interaction** or the **ACM/IEEE HRI
   conference** (full paper), with the simulation paper cited as the model basis.

A short version of the trust result can go to the **IEEE RO-MAN** conference or an HRI late-breaking
report while the journal paper is under review (check each venue's dual-submission rules).

## 4. Steps to submission

1. Run `python3 experiments/run_all.py` with `QLMODEL_REPS=30` (or more) and check that the numbers in
   `paper/main.tex` match `results/*.json` (the paper quotes them directly).
2. Optional but valuable: run the circuits on real hardware (Section 6 of `README.md`) and add the
   hardware row to Table II and Fig. 7. Hardware results must be reported as measured, with the
   backend name, date, job id and calibration data.
3. Fill the `[FILL]` fields in `paper/main.tex` (acknowledgment, funding, biographies).
4. Decide on the statement on the use of generative AI tools required by the journal.
5. Deposit the code on Zenodo (concept DOI) and cite it in the Data Availability section.
6. Submit through the journal's ScholarOne site with the source zip and the code as supplementary material.

## 5. Human study that would complete the programme (proposed, not run)

- Pre-registered online study (N about 400 per order, from the power analysis of Experiment 1) with
  the three domains as video vignettes of a robot asking questions; both orders between subjects; the
  QQ test and model comparison as primary analyses.
- Laboratory hand-over study on the LeKiwi platform (Survey 3, Section XV) with and without an
  intermediate trust question (Experiment 4 design), 100–400 participants per condition.
- Ethics approval from the institutional review board before any data collection.
