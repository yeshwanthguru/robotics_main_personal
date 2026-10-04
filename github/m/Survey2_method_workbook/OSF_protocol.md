# OSF registration text — Survey 2 (retrospective)

Paste each section into the matching field of the OSF "Generalized Systematic Review Registration"
form, in the same order as for Survey 1. Items marked **[CHECK]** need a fact only you know.

---

**Title**
Quantum-Like Cognition and Decision-Making for Autonomous Agents, from Robotics to AI/ML Systems: A Systematic Review — review protocol

**Authors**
Yeshwanth Guru (ORCID 0009-0007-6353-4033); Dev Kunwar Singh Chauhan (ORCID 0000-0002-1466-4567).
Department of Mechanical Engineering, Amrita Vishwa Vidyapeetham, Chennai, India.

**Contributors (OSF project > Contributors)**
Yeshwanth Guru (Admin, bibliographic) first; Dev Kunwar Singh Chauhan (Read + Write, bibliographic)
second. Use a new OSF project, separate from the Survey 1 project.

**License**
CC-By Attribution 4.0 International. Copyright holders: Yeshwanth Guru, Dev Kunwar Singh Chauhan. Year: 2026.

**Description / Summary**
Protocol for a systematic review of quantum-cognition (quantum-probability) models applied to
autonomous agents: decision networks, machine learning and language models, quantum-inspired
reinforcement learning, robot perception and emotion, multi-agent and human–machine teams, and human
trust in AI. The review grades 67 application studies and 71 theory and evidence studies on a
six-level evidence scale (E1 conceptual to E6 field deployment) and appraises the application studies
against seven quality criteria. Registered retrospectively after the review was completed (corpus
closed 4 October 2026). It is the companion of a separate review of quantum technologies for
autonomous robotics by the same authors (registered separately).

**Registration timing / Stage of review**
Review completed. Registered retrospectively after the corpus was closed (4 October 2026), to
document the methods as applied. If asked "Has data collection started?": Yes, completed.
Review stage: tick Completed for every stage.

**Review stages (free text)**
All stages were completed before this retrospective registration.
1. Preparation: research questions (RQ1–RQ5), eligibility criteria (I1–I3, E1–E6), six-level evidence
   scale (E1–E6), model-type tags and extraction codebook defined.
2. Search: curated reading list (102 items, each verified); authors' PDF collection identified by
   first-page text; structured searches of Google Scholar, Semantic Scholar, arXiv, PubMed and publisher
   sites with citation chasing, in two streams; targeted search on 4 October 2026.
3. Screening: title/abstract, then full text where available, by the first author; inclusion
   decisions reviewed by the second author **[CHECK]**.
4. Extraction: by the first author, using the codebook; 16 of the 67 application studies extracted
   from full texts and the rest from abstracts and publisher pages.
5. Critical appraisal and evidence grading: seven criteria (met / partly met / not met / not
   assessable); each study assigned an evidence level and a model-type tag.
6. Synthesis: narrative synthesis by agent function and domain; evidence map; comparison with
   classical models; worked examples and an illustrative reinforcement-learning experiment. No
   meta-analysis.
7. Reporting: manuscript prepared following PRISMA 2020.
One amendment was made during the review: exclusion criterion E5 (quantum computation used only as
an accelerator, without a cognitive or decision model) was added so that the review does not repeat
its companion review; 11 studies of the earlier corpus moved out of the primary studies under E5.

**Current review stage**
All stages completed; the manuscript is ready for journal submission. This is a retrospective
registration, and the first and only registration of this review.

**Start date**
**[CHECK]** month the Survey 2 work started (the exact day was not recorded).

**End date**
2026-10-04 (corpus closed; manuscript ready for submission).

**Type of review**
Systematic review with narrative synthesis (no meta-analysis), reported following PRISMA 2020.
Evidence graded on a six-level scale (E1 conceptual, E2 formal model, E3 human data, E4 simulation or
benchmark, E5 physical system, E6 field deployment); quality appraised against seven criteria.

**Discipline / Subjects**
Engineering > Robotics; Computer science > Artificial intelligence; Social and behavioral sciences >
Psychology (cognitive psychology).

**Background**
Autonomous robots and AI systems decide under ambiguity and with people whose judgements violate
classical probability: question-order effects, conjunction and disjunction fallacies, and violations
of the sure-thing principle. Quantum cognition models beliefs as vectors in a Hilbert space and
judgements as measurements; these quantum-probability (QP) models run on classical computers and
reproduce several such effects with few parameters. Since about 2016 the models have been carried
into autonomous agents: quantum-like Bayesian networks, quantum-inspired machine learning and
language-model audits, quantum-inspired reinforcement learning, robot perception and emotion models,
multi-agent and human–machine teams, and trust in AI. Existing reviews cover the psychology or the
quantum-computing side, but none grades how far the evidence for these applications goes. This
review fills that gap.

**Primary research question(s)** (wording identical to Section 1.5.1 of the manuscript)
RQ1: Which quantum-like, quantum-inspired and quantum-circuit models of cognition and decision have
been applied to autonomous agents, and to which agent functions (perception and fusion,
decision-making and planning, learning, embodied and social behaviour, multi-agent coordination, and
human–AI trust)?
RQ2: How strong is the psychological evidence for the QP phenomena on which these applications rely,
and which classical explanations compete with it?
RQ3: How far does the evidence for each application go, from conceptual proposal to field deployment,
and how well do the studies meet basic quality criteria?
RQ4: Under which conditions do QP models outperform, match or underperform classical alternatives?
RQ5: Which validation programme, benchmarks and reporting standards are needed to move the field
towards deployed agents?
PICOS — Population: artificial agents, AI systems and human–agent interaction. Intervention:
quantum-like, quantum-inspired and quantum-circuit models of cognition and decision. Comparator:
classical (Bayesian, Markov, utility-based, neural) models, where reported. Outcomes: evidence level,
model type, task results, quality criteria. Study designs: any (formal models, human experiments,
simulations, benchmarks, physical systems, reviews).

**Secondary research question(s)**
None.

**Expectations / hypotheses**
No formal hypotheses were tested. We expected (i) strong human-data evidence for order effects and
interference but contested evidence for conjunction fallacies and contextuality; (ii) most agent
applications at the level of formal models and simulations; and (iii) few controlled comparisons with
classical models.

**Dependent variable(s) / outcome(s) / main variables**
For each application study: evidence level (E1–E6); model type (quantum-like, quantum-inspired,
quantum circuit design or simulation, quantum circuit on a QPU); domain; task; key result; limitation;
publication status; basis of extraction; and seven appraisal judgements (Q1 model specification, Q2
classical comparison, Q3 empirical grounding, Q4 parameter discipline, Q5 quantitative evaluation, Q6
reproducibility, Q7 critical discussion). For each theory and evidence study: evidence level,
phenomenon, key result, limitation.

**Additional variable(s) / covariate(s)**
Year; venue; whether the study is also discussed in the companion review.

**Software**
- Web search interfaces (Google Scholar, Semantic Scholar, arXiv, PubMed, publisher sites).
- Mendeley Reference Manager 2.149.0 for references and citing.
- Microsoft Excel 2024 (Survey2_method_workbook.xlsx) for screening and extraction; exported to CSV.
- Python 3 with NumPy and matplotlib for counts, figures and the worked examples.
- LaTeX (pdfTeX, TeX Live 2023; Springer Nature sn-jnl class) for the manuscript; pandoc for Word.
- Git and GitHub (private repository) for version control.

**Databases**
Google Scholar; Semantic Scholar; arXiv; PubMed; publisher sites (Springer, Elsevier, Frontiers, MDPI,
IEEE, ACM, Royal Society); supplemented by citation chasing from Pothos and Busemeyer (2022), Huang
et al. (2025), Widdows et al. (2021) and Meyer et al. (2022). Coverage: 1932 (background) and 1999
(theory) to October 2026.

**Interfaces**
Google Scholar (scholar.google.com); Semantic Scholar (semanticscholar.org); arXiv (arxiv.org);
PubMed (pubmed.ncbi.nlm.nih.gov); publisher websites. All accessed through their public web
interfaces.

**Grey literature**
Preprints (arXiv) included and flagged by publication status; doctoral theses included when they are
the most complete version (one thesis); project web pages and other unpublished documents excluded
(E6).

**Information sources**
As above, plus the authors' PDF collection and a cross-check against the companion review's corpus.

**Query strings**
The strings of the main searches were not logged. Concept blocks that reproduce their scope, and the
exact queries of the targeted search of 4 October 2026, are in search_strings.md and
targeted_search_record.md (Online Resource 1, Table S6).

**Search validation procedure**
Every record was checked against publisher, arXiv or repository records; PDFs were identified by
their first-page text. The targeted search of October 2026 served as a check of the earlier searches
and found four further application studies.

**Other search strategies**
Backward and forward citation chasing; cross-check against the companion review's corpus.

**Procedures to contact authors**
Authors of included studies were not contacted.

**Results of contacting authors**
Not applicable.

**Search expiration and repetition**
Not a living review. If the review is revised more than six months after 4 October 2026, the
targeted queries will be re-run and new studies reported separately with the new date.

**Search strategy justification**
Quantum cognition spans psychology, AI and physics and is published in venues that the engineering
databases index poorly (psychology journals, Royal Society and Frontiers journals, Quantum Interaction
proceedings, arXiv). Multidisciplinary search engines, PubMed and citation chasing from the main
reviews were therefore used instead of engineering databases alone.

**Miscellaneous search strategy details**
The search was iterative; the scope was refined while records were screened.

**Inclusion and exclusion criteria** (as Section 1.5.3 of the manuscript)
Included: (I1) proposes, evaluates or reviews a quantum-like, quantum-inspired or quantum-circuit
model of cognition, decision or learning applied to an artificial agent, an ML or AI system, or
human–AI or human–robot interaction (application studies); (I2) theory, empirical tests or critiques
of QP models of human judgement and decision (theory and evidence studies); (I3) reviews, classical
baselines, hardware, software or background (not graded).
Excluded: (E1) "quantum" used only as a metaphor; (E2) not in English; (E3) duplicate (most complete
version kept); (E4) physical quantum processes in the brain without a cognitive model; (E5) quantum
computation used only to accelerate a robot or learning task, without a cognitive or decision model;
(E6) not published in a journal, conference, book, thesis or preprint server.

**Screening stages**
Title and abstract, then full text where available.

**Screened fields / blinding**
Title, abstract, full text; no blinding.

**Used exclusion criteria**
E1–E6, applied in order; the first criterion met is recorded.

**Screener instructions**
Single screener (first author). Keep uncertain records for full-text reading; classify each included
work as I1, I2 or I3; tag quantum-inspired work separately from quantum-like and circuit work; keep the
most complete version; pass decisions to the second author for review **[CHECK]**.

**Screening reliability**
One screener; no independent second screening, so no agreement statistic is reported. Stated as a
limitation in the article.

**Screening reconciliation procedure**
Disagreements between the authors resolved by discussion **[CHECK]**.

**Sampling and sample size**
No sampling: all works that met the criteria were kept: 67 application studies, 71 theory and
evidence studies, 17 reviews and 43 background works (plus 11 E5 exclusions and 3 method references
cited). 61 application studies (levels E2–E6) were appraised.

**Screening procedure justification**
Two-stage screening is proportionate to a corpus of about 200 works; a single screener with review by
the second author was a pragmatic choice for a two-person unfunded team; every judgement is published
so that readers can check it.

**Data management and sharing**
Shared on Zenodo **[CHECK: Zenodo DOI]**, licence CC BY 4.0, no embargo: extraction_table.csv,
quality_appraisal.csv, theory_evidence_studies.csv, codebook.md, search_strings.md, README.md. Not
shared: full texts (copyright) and the records of the main searches (not logged).

**Miscellaneous screening details**
Eleven studies of the earlier corpus were moved out of the primary studies under E5 and are listed
in Online Resource 1 (Table S7).

**Entities to extract**
Study label, citation key, evidence level, model type, publication status, domain, task or
phenomenon, method, setup and data, key result, limitation, basis of extraction, overlap with the
companion review, DOI or identifier; appraisal judgements Q1–Q7.

**Extraction stages**
One stage, by the first author, using the codebook; the second author reviewed the evidence levels
and appraisal judgements **[CHECK]**.

**Extractor instructions**
Record only what each study reports; assign the lower level when the evidence is ambiguous; record
the basis of extraction; mark Q6 as not assessable when the full text is not available.

**Extractor masking**
None.

**Extraction reliability**
Single extractor; no agreement statistic.

**Extraction reconciliation procedure**
Discussion between the authors **[CHECK]**.

**Extraction procedure justification**
As for screening.

**Data management and sharing (extracted entities)**
As above (Zenodo, CC BY 4.0).

**Miscellaneous extraction details**
51 of the 67 application studies were extracted from abstracts and publisher pages because their full
texts were not available to the authors; their Q6 judgements are marked not assessable.

**Planned data transformations**
Counts by evidence level, domain and model type; counts of appraisal judgements per criterion.

**Missing data**
Not-reported details recorded as not reported; lower level assigned when ambiguous; Q6 marked "?"
without a full text.

**Data validation**
All references checked against publisher, arXiv or repository records; all 212 references checked
against the Retraction Watch database (4 October 2026; no retractions).

**Quality assessment**
Seven criteria (Q1–Q7), judged met / partly met / not met / not assessable; not summed into a score.

**Synthesis plan**
Narrative synthesis by agent function (Sections 7–13) and domain; evidence map (Figure 8); comparison
with classical models (Table 4); decision guide; worked examples and an illustrative reinforcement-
learning experiment (code in Online Resource 2).

**Criteria for conclusions / inference criteria**
Claims are stated with the number of studies and their evidence levels; conclusions from E1–E2
studies are labelled tentative.

**Synthesist blinding**
None.

**Synthesis reliability**
Synthesis written by the first author and reviewed by the second.

**Synthesis reconciliation procedure**
Discussion.

**Publication bias analyses**
Not possible (no pooled effect); publication bias noted as a threat to validity.

**Sensitivity analyses / robustness checks**
None formal; the effect of extracting from abstracts is discussed as a limitation.

**Synthesis procedure justification**
Heterogeneous tasks and metrics prevent meta-analysis.

**Synthesis data management and sharing**
As above.

**Miscellaneous synthesis details**
The illustrative reinforcement-learning experiment (30 seeds) was run for this review; its code is
released as Online Resource 2.

**Data availability**
Zenodo **[CHECK: DOI]**.

**Funding**
This research received no external funding. It was carried out as university work.

**Conflicts of interest**
The authors declare no conflicts of interest.

**Overlapping authorships**
The authors are the authors of the companion review (quantum technologies for autonomous robotics),
which is cited in this review to mark the boundary between the two reviews; it is not an included
study. Neither author is an author of any of the 67 application studies or 71 theory and evidence
studies.
