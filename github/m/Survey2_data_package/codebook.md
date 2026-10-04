# Codebook

All files are UTF-8 (with BOM), comma-separated.

## extraction_table.csv (one row per application study, 67 rows)

| Column | Definition |
|---|---|
| Study | Study label (first author et al. (year)); the full reference is in refs.bib of the article. |
| Key | Citation key in refs.bib. |
| Evidence level | E1 conceptual (position or proposal without a formal model or data); E2 formal model (mathematical model or algorithm, analytic or toy illustration only); E3 human data (model fitted to or tested on human behavioural or neural data); E4 simulation or benchmark (simulated agents, ML benchmark datasets or LLM probes); E5 physical system (physical robot or real hardware system in the laboratory); E6 field deployment (real-world deployment or large-scale study with real users). |
| Model type | Quantum-like (quantum-probability mathematics on classical computers); Quantum-inspired (classical algorithm borrowing quantum ideas); Quantum circuit (design or simulation); Quantum circuit (QPU) (at least partly run on a quantum processing unit). |
| Publication status | Journal article; Conference paper; Book chapter; Doctoral thesis; Preprint. |
| Domain | Decision models and networks; ML, NLP and IR; Deep learning and LLMs; Reinforcement learning and agent learning; Robots and embodied agents; Multi-agent systems and teams; Human-AI trust. |
| Task or phenomenon | Agent task or cognitive phenomenon addressed. |
| Method | Method in brief. |
| Setup and data | Set-up, data and baselines. |
| Key result | Main quantitative or qualitative result as reported. |
| Limitation | Principal limitation. |
| Basis | Full text (extracted from the full text) or Abstract (extracted from the abstract and publisher page). |
| Also in companion survey | Yes if the study is also discussed in the companion survey (Guru and Chauhan, quantum technologies for autonomous robotics). |
| DOI or identifier | DOI or arXiv identifier. |

## quality_appraisal.csv (61 rows)

| Column | Definition |
|---|---|
| Study key | Citation key. |
| Basis | Source of the judgements (Full text or Abstract). |
| Q1 Model specification | State space, operators and free parameters stated. |
| Q2 Classical comparison | A classical Bayesian, Markov, utility or neural model evaluated on the same task. |
| Q3 Empirical grounding | Human data or a realistic agent or AI task rather than a toy example. |
| Q4 Parameter discipline | Parameters predicted or constrained a priori, or validated on held-out data. |
| Q5 Quantitative evaluation | Metrics with some measure of variability. |
| Q6 Reproducibility | Code and data released (P: one of them, or model fully specified; "available on request" counts as N). |
| Q7 Critical discussion | Limitations and classical alternatives discussed. |

Codes: M met; P partly met; N not met; ? not assessable without the full text. The six E1 studies are not appraised.

## theory_evidence_studies.csv (71 rows)

Study, Key, Evidence level (as above), Phenomenon, Method, Setup and data, Key result, Limitation,
Basis and DOI or identifier, defined as for the extraction table.

## study_summaries.csv (209 rows)

| Column | Definition |
|---|---|
| Key | BibTeX key in refs.bib |
| Study | Author(s) and year |
| Group | application; theory and evidence; review; background; excluded (E5) |
| Basis | Full text or Abstract: the source the summary was written from |
| Summary | Plain-text summary (problem, method, setup, main result, limitation where reported) |
| Summary_keyed | The same text with cited works marked `[CITE:key]`, used to typeset Section S9 of Online Resource 1 |
| Verification_note | Empty if the summary was checked against the source; otherwise what still needs checking |
