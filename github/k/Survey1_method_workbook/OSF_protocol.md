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

**Dependent variable(s) / outcome(s) / main variables**
This is a descriptive review, not a review of associations, so these are the main variables
extracted from each primary study (defined in the codebook of the data package):
1. Robotic function and task (optimization and planning; learning; sensing and communication;
   decision-making and reasoning).
2. Quantum method and technology type (e.g., quantum annealing, QAOA, Grover search, variational
   circuits, quantum reinforcement learning, quantum sensing, quantum key distribution,
   quantum-probability models; genuinely quantum vs. quantum-inspired).
3. Evidence level, L1-L6 (L1 theoretical; L2 simulation; L3 run on quantum hardware; L4 closed loop
   with a robot or high-fidelity robot simulator; L5 physical robot or vehicle; L6 end-to-end field
   deployment with a measured advantage over a classical baseline).
4. Quantum execution venue (none; simulated; QPU; quantum sensor or link hardware; classical).
5. Publication status (journal, conference, book chapter, preprint).
6. Setup and baselines (hardware or simulator, problem size, classical comparator).
7. Key reported result, including performance against the classical baseline where reported.
8. Principal limitation.
9. Quality-appraisal judgments on seven criteria (problem formulation, classical baseline,
   experimental realism, hardware and noise reporting, performance metrics, reproducibility,
   critical discussion), each met / partly met / not met.
Deployment constraints (qubit counts, noise, latency, quantum-classical communication, size,
weight, power, and cooling) are recorded where studies report them.

**Additional variable(s) / covariate(s)**
No formal covariates, moderators, or mediators were analyzed (descriptive review, no meta-analysis).
Additional study characteristics recorded and used to describe or stratify the corpus:
- Publication year (to describe the growth of the field over time).
- Publication status (preprint vs. peer-reviewed), used when interpreting the strength of a claim.
- Quantum hardware platform and vendor where reported (e.g., D-Wave annealer, IBM superconducting
  processor), and problem size (number of robots, tasks, nodes, or qubits).
- Availability of code or data (checked for studies whose full text was accessible).
- Primary study vs. review of the topic (reviews are included but not graded on L1-L6).

**Software**
- Database web interfaces (IEEE Xplore, ACM Digital Library, Scopus, Web of Science, SpringerLink,
  ScienceDirect, arXiv) for searching and exporting records.
- Mendeley Reference Manager 2.149.0 for storing references, removing duplicates, and citing.
- Microsoft Excel 2024 (Survey1_method_workbook.xlsx) for screening decisions, data
  extraction, quality appraisal, and evidence grading; exported to CSV (UTF-8) for sharing.
- Python 3.11 with matplotlib 3.11 and NumPy for counts, cross-tabulations, and figures.
- LaTeX (pdfTeX, TeX Live 2023; ACM acmart class) on Overleaf for the manuscript; pandoc 3.1.3 for
  the Word version.
- Git and GitHub (private repository) for version control of the manuscript, data, and decisions.
Operating system: [CHECK, e.g., Windows 11].

**Databases** (Search strategy section)
1. IEEE Xplore Digital Library
2. ACM Digital Library
3. Scopus
4. Web of Science Core Collection
5. SpringerLink
6. ScienceDirect
7. arXiv (categories quant-ph, cs.RO, cs.LG)
Supplemented by backward and forward citation searching from key surveys (Tandon et al. 2017;
Petschnigg et al. 2019; Meyer et al. 2022; Yan et al. 2024) and by targeted searches in application
areas where quantum-robotics work appears outside robotics venues. Coverage: 1982 to October 2026.

**Interfaces**
1. IEEE Xplore Digital Library: IEEE Xplore (ieeexplore.ieee.org)
2. ACM Digital Library: ACM Digital Library (dl.acm.org)
3. Scopus: Scopus, Elsevier (scopus.com)
4. Web of Science Core Collection: Web of Science, Clarivate (webofscience.com)
5. SpringerLink: SpringerLink, Springer Nature (link.springer.com)
6. ScienceDirect: ScienceDirect, Elsevier (sciencedirect.com)
7. arXiv: arXiv advanced search (arxiv.org)
Subscription databases accessed through an institutional subscription; arXiv is open access.

**Grey literature**
- Preprints: arXiv was searched directly (categories quant-ph, cs.RO, cs.LG); preprints were
  included and flagged by publication status, and the published version was used where one existed.
- Conference proceedings: covered through IEEE Xplore, the ACM Digital Library, and SpringerLink,
  which index the main robotics, quantum-computing, and evolutionary-computation conferences.
- Citation chasing: backward and forward citation searching from key surveys and included studies,
  which can surface preprints and proceedings papers not returned by the database searches.
- Targeted searches in application areas (drones and UAVs, multi-agent and autonomous mobility,
  autonomous driving, control benchmarks, automated storage and retrieval) where quantum-robotics
  work appears outside robotics venues.
Not searched systematically: dissertations and theses, university repositories, and government or
industry reports. Industry announcements without a technical paper were not included as primary
studies.

**Information sources**
IEEE Xplore, ACM Digital Library, Scopus, Web of Science, SpringerLink, ScienceDirect, arXiv
(quant-ph, cs.RO, cs.LG); backward and forward reference chasing from key papers and earlier
surveys; targeted searches in application areas where quantum-robotics work appears outside
robotics venues. Coverage: 1982 to October 2026.

**Query strings** (as in supplementary Table S6; adapted to each database's syntax)
Core string (CORE):
("quantum computing" OR "quantum algorithm*" OR "quantum annealing" OR QAOA OR "variational quantum"
OR "quantum machine learning" OR "quantum reinforcement learning" OR "quantum-inspired" OR "quantum
sensing" OR "quantum cognition" OR "quantum probability") AND (robot* OR "autonomous vehicle*" OR
"mobile robot*" OR swarm OR UAV OR AGV OR manipulator) AND (planning OR navigation OR localization OR
"path planning" OR "task allocation" OR routing OR control OR learning OR "decision making" OR SLAM
OR kinematics)

Foundations string (FOUND):
("quantum computing" OR "quantum algorithm*") AND (review OR survey OR tutorial) AND (NISQ OR "error
mitigation" OR "barren plateau*" OR "fault-tolerant" OR dequantiz*)

Per database / interface:
1. IEEE Xplore / IEEE Xplore: CORE in "All Metadata"; years 1982 to 2026.
2. ACM Digital Library / ACM DL: CORE in Title, Abstract, and Author Keywords.
3. Scopus / Scopus: TITLE-ABS-KEY( CORE )
4. Web of Science Core Collection / Web of Science: TS=( CORE )
5. SpringerLink / SpringerLink: CORE in full text; content type Article and Conference Paper.
6. ScienceDirect / ScienceDirect: CORE in full text; article types Research articles and
   Conference papers. [CHECK: ScienceDirect allows at most 8 Boolean connectors per field and no
   wildcards, so state how the string was shortened or split.]
7. arXiv / arXiv advanced search: categories quant-ph, cs.RO, cs.LG; CORE terms in title and
   abstract.
Foundations string: run in [CHECK which databases].
Targeted searches: the quantum block of CORE combined with each application area: drones and UAVs;
multi-agent and autonomous mobility; autonomous driving; control benchmarks (cart-pole); automated
storage and retrieval.
Citation chasing: backward and forward from Tandon et al. 2017, Petschnigg et al. 2019,
Meyer et al. 2022, and Yan et al. 2024.

**Search validation procedure**
No formal validation set of known studies was defined before the search. The search was checked in
two ways after the database searches:
1. Coverage of existing reviews: the reference lists of earlier quantum-robotics surveys (Tandon et
   al. 2017; Petschnigg et al. 2019; Meyer et al. 2022; Yan et al. 2024) were screened through
   backward and forward citation searching, to confirm that the relevant studies they cite were
   found or added.
2. Cross-check for missed studies (October 2026): a web search across every branch of the taxonomy
   was compared against the reference list. It identified 12 additional primary studies, mostly in
   application areas published outside robotics venues (drones and UAVs, autonomous mobility,
   autonomous driving, control benchmarks, automated storage and retrieval). Targeted searches for
   these areas were then run and the 12 studies were added; they are reported separately in the
   flow diagram (supplementary Figure S1) and Table S6.
No further validation (e.g., a predefined test set or measured recall) was performed.

**Other search strategies**
1. Ascendancy (backward citation searching): reference lists of earlier surveys (Tandon et al. 2017;
   Petschnigg et al. 2019; Meyer et al. 2022; Yan et al. 2024) and of key included studies were
   screened against the eligibility criteria.
2. Descendancy (forward citation searching): studies citing the same surveys and key included
   studies were screened, using the "cited by" function of [CHECK: e.g., Google Scholar / Scopus].
3. Targeted searches: the quantum block of the core string combined with application areas where
   quantum-robotics work appears outside robotics venues (drones and UAVs; multi-agent and
   autonomous mobility; autonomous driving; control benchmarks (cart-pole); automated storage and
   retrieval).
Co-citation tools (e.g., CoCites) were not used.

**Procedures to contact authors**
Authors of included studies were not contacted. Data were extracted only from what each study
reported; where a detail (e.g., hardware, number of shots, latency, or code availability) was not
reported, it was recorded as not reported, and the evidence level was assigned conservatively (the
lower level when in doubt). Where a full text could not be obtained, the study was assessed from the
available record. Because no authors were contacted, there is no
communication metadata to share.

**Results of contacting authors**
Not applicable: no authors were contacted, so there are no outcomes to report.

**Search expiration and repetition**
This is not a living review, and no repeat search is planned. The search closed in October 2026, and
the evidence levels describe the literature at that date. The field moves quickly (25 of the 72
primary studies appeared in 2025 alone), so if the review is revised more than six months after the
search closed, or if reviewers ask, the database searches will be re-run from October 2026 with the
same strings, and any studies added will be reported separately with the new search date.

**Search strategy justification**
- Databases: quantum robotics sits between robotics, computer science, and physics, so the search
  combined the main engineering and computing publishers (IEEE Xplore, ACM Digital Library,
  SpringerLink, ScienceDirect), two multidisciplinary indexes (Scopus, Web of Science) to catch work
  in physics and general-science journals, and arXiv, because many key quantum-computing results
  appear first, or only, as preprints.
- Interfaces: each database was searched through its own publisher interface, which gives the full
  field and filter options; no aggregator was needed.
- Grey literature: arXiv was included because the field is young and fast moving (16 primary
  studies were preprints when graded). Conference proceedings were covered because robotics and
  quantum computing publish heavily at conferences. Theses and industry reports were not searched
  systematically because they rarely report enough technical detail to grade; this is a stated
  limitation.
- Query strings: the field's terminology is loose ("quantum", "quantum-inspired", "quantum-like"),
  so the strings were deliberately broad, combining a quantum-methods block, a robot block, and a
  robotic-function block, and were refined iteratively as the scope settled. Because broad strings
  still missed work published outside robotics venues, citation chasing and targeted searches in
  application areas were added.
- Author contact: authors were not contacted because the review grades what each study reports; an
  unreported detail is itself a reporting finding, and studies were graded conservatively.
- Expiration: the search closed in October 2026, immediately before submission, so the corpus is as
  current as possible; given the field's pace, a conditional update is planned if the review is
  revised more than six months later.

**Miscellaneous search strategy details**
- Record counts: because the searches were run iteratively while the scope was refined, the number
  of records returned by each database and the numbers excluded at each screening stage were not
  logged. The flow diagram (supplementary Figure S1) therefore shows the stages followed and only
  the counts that can be documented.
- De-duplication: records from all sources were merged in Mendeley Reference Manager and duplicates
  removed; where a study existed in several versions (preprint, conference, journal), the most
  complete version was kept.
- Record verification: every retrieved full text was checked against its bibliographic record;
  mislabeled files and wrong metadata were corrected before extraction, and all references were
  verified against publisher, DOI, or arXiv records.
- Limits applied: English only; no restriction on publication type; coverage 1982 to October 2026.

**Inclusion and exclusion criteria** (wording follows Section 3.3 of the manuscript)
Inclusion:
- I1. Proposes, evaluates, or reviews a quantum or quantum-inspired method applied to a robotic
  function (primary studies; graded on L1-L6).
- I2. Provides algorithms, hardware, or theory on which such methods depend (foundational works;
  not graded).
- I3. Supplies the classical baselines needed for comparison (foundational works; not graded).
Exclusion:
- E1. Uses "quantum" only metaphorically.
- E2. Not in English.
- E3. Duplicates an included study (the most complete version is kept, e.g., the journal version of
  a conference paper or preprint).
- E4. Addresses quantum communication without a robotic application.
Scope boundaries: robots that manipulate quantum systems, and classical robotics used to build
quantum hardware, are out of scope. Quantum computer-vision studies without a robotic application
fail I1. No restriction on publication type (journal, conference, book chapter, preprint) or year
(coverage 1982 to October 2026).

Framework: no formal framework was used to set the criteria. The search query was built from three
concept blocks that correspond to an adapted PICO structure: Intervention (quantum and
quantum-inspired methods), Population (robots and autonomous systems), and Outcome/context (robotic
functions such as planning, navigation, localization, task allocation, routing, control, learning,
and decision-making). Comparison (classical baselines) was not a search block; it was extracted from
each study.

**Screening stages**
1. De-duplication (software, checked by a human): records from all sources merged in Mendeley
   Reference Manager; duplicates removed with its duplicate check and confirmed by the first author;
   for studies in several versions, the most complete version kept (E3).
2. Title and abstract screening (human): the first author screened each record against criteria
   I1-I3 and E1-E4; records that were clearly irrelevant were excluded, uncertain ones were kept.
3. Full-text screening (human): the first author read the full text of the remaining records and
   applied the criteria; included studies were classified as primary studies (I1) or foundational
   works (I2/I3 only).
4. Additional records from citation chasing and the targeted searches went through the same stages
   2-3 (human).
5. Review by the second author (human): the second author reviewed the inclusion decisions and the
   classification of every included record (primary study or foundational work); disagreements were
   resolved by discussion.
No automated or AI-based screening tool was used for inclusion decisions. Numbers excluded at each
stage were not logged.

**Screened fields / blinding**
No blinding was applied. During title and abstract screening, all bibliographic fields were visible
(title, abstract, keywords, authors, venue, and year); during full-text screening, the complete
article was visible. Blinding was not practical because screening was done in the reference manager
and on publisher pages, where these fields are always shown.

**Used exclusion criteria** (applied in this order; a record is excluded at the first one it meets)
1. E3. Duplicate or earlier version of an included study (most complete version kept).
2. E2. Not in English.
3. E1. "Quantum" used only metaphorically (no quantum or quantum-inspired method).
4. Out of scope: robots that manipulate quantum systems, or classical robotics used to build
   quantum hardware.
5. E4. Quantum communication without a robotic application.
6. No robotic application AND not foundational (reformulated I1-I3): the record does not apply a
   quantum or quantum-inspired method to a robotic function, does not provide algorithms, hardware,
   or theory on which such methods depend, and does not supply a classical baseline needed for
   comparison.
Records that pass 1-6 are kept: as primary studies if they apply a method to a robotic function
(I1, graded L1-L6), otherwise as foundational works (I2/I3, not graded). Quantum computer-vision
studies without a robotic application are not primary studies and are discussed, ungraded, in the
supplementary material.

**Screener instructions**
Screening was done by a single screener (the first author), so no separate written instructions
were prepared for other screeners. The screener applied the following decision rules:
1. Apply the exclusion criteria in the listed order and record the first one met.
2. At title and abstract stage, exclude only records that clearly meet an exclusion criterion; when
   in doubt, keep the record for full-text screening.
3. At full-text stage, decide inclusion and classify each included record as a primary study (I1)
   or a foundational work (I2/I3).
4. Treat "quantum-inspired" classical algorithms as in scope (I1) but tag them separately from
   genuinely quantum methods.
5. When several versions of a study exist, keep the most complete one (usually the journal version).
6. Pass all inclusion decisions and classifications to the second author for review; resolve
   disagreements by discussion.
The eligibility criteria and the extraction codebook are provided with the dataset (Zenodo).

**Screening reliability**
- De-duplication: one screener (first author), assisted by Mendeley's duplicate check.
- Title and abstract screening: one screener (first author).
- Full-text screening: one screener (first author); the second author then reviewed the inclusion
  decisions and classifications, and disagreements were resolved by discussion.
Screening was not independent: no round was carried out by two screeners working separately, so
screener agreement could not be measured and no agreement statistic (e.g., Cohen's kappa) is
reported. This is stated as a limitation in the article's threats to validity.

**Screening reconciliation procedure**
- De-duplication and title/abstract screening: one screener, so no reconciliation was needed.
- Full-text screening: where the second author, reviewing the first author's inclusion decisions
  and classifications, disagreed, the two authors discussed the record against the eligibility
  criteria until they reached consensus. No third screener was involved.

**Sampling and sample size**
No sampling was used: all sources that passed screening were kept. The final corpus is 72 primary
studies (65 empirical or theoretical studies and 7 reviews) and 107 foundational works. All 72
primary studies were extracted and classified; the 65 non-review studies were assigned an evidence
level (L1-L6), and the 59 application studies (excluding six purely theoretical L1 studies) were
quality-appraised. No sample-size or power analysis applies, because the synthesis is narrative and
no statistical test or meta-analysis was performed. Where a function or method is supported by only
a few studies, or only by low evidence levels, conclusions are stated as tentative and the number of
studies and their evidence levels are reported with each claim.

**Screening procedure justification**
- Screening rounds: a two-stage process (title and abstract, then full text) is standard and was
  proportionate to the size of the literature. Many studies use "quantum" loosely or bury the
  robotic application in the body of the paper, so uncertain records were kept for full-text
  reading rather than excluded early.
- Blinding: not applied. Screening was done in a reference manager and on publisher pages that do
  not hide authors, venues, or years, and the bias blinding guards against was addressed instead by
  grading every included study on the same evidence scale and publishing all judgments.
- Inclusion and exclusion criteria: inclusion was deliberately broad (genuinely quantum and
  quantum-inspired methods, all publication types including preprints) because the field is young
  and a narrower scope would miss much of its evidence; quantum-inspired results were then tagged
  separately so they cannot be mistaken for quantum results. Foundational works were kept but not
  graded, so that the review can compare claims with the underlying algorithms and baselines.
- Assurance: a single screener with review by the second author was a pragmatic choice for a
  two-person team without funding. Its cost is that screening reliability cannot be measured; this
  is stated as a limitation, and every included study and its grading and appraisal are published so readers can
  check it.
- Reconciliation: with two authors, discussion to consensus was the simplest workable procedure; no
  third reviewer was available.

**Data management and sharing**
Shared openly on Zenodo (DOI to be added), licence CC BY 4.0, no embargo or access conditions:
- extraction_table.csv (CSV, UTF-8): every included primary study with its evidence level,
  execution tag, publication status, task, method, setup, key result, limitation, and DOI.
- quality_appraisal.csv (CSV, UTF-8): the appraisal judgment for each appraised study on each of the
  seven criteria.
- codebook.md (Markdown): definitions of all columns and codes.
- search_strings.md (Markdown): databases, fields, and query strings.
- README.md (Markdown): description of the files.
The same files are submitted with the article as supplementary material.
Not shared: (1) the raw records returned by each database search, because they were not exported
and saved at each search; (2) the screening decisions on excluded records, because exclusions were
not logged; and (3) full texts of the included studies, because of publishers' copyright. The full
bibliographic records of all included studies and foundational works are given in the article's
reference list.

**Miscellaneous screening details**
- Screening and search were iterative: the scope and strings were refined while records were being
  screened, and new records found by citation chasing or targeted searches were screened as they
  appeared, until the corpus closed in October 2026.
- Records excluded at full text fell under E1 (metaphorical use of "quantum"), E2 (not in English),
  E3 (duplicate or earlier version), or E4 (no robotic application); their numbers were not logged.
- Six quantum computer-vision studies without a robotic application were excluded from the primary
  studies (they fail I1) but are discussed, ungraded, in the supplementary material, so readers can
  see the boundary of the inclusion criteria.
- The PRISMA flow diagram (supplementary Figure S1) shows the stages followed and the counts that
  can be documented.

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

**Funding**
This research received no external funding. It was carried out as part of the authors' work at
Amrita Vishwa Vidyapeetham, Chennai, India.

**Conflicts of interest**
The authors declare no conflicts of interest. Neither author has financial ties to, or receives
funding, equipment, or cloud credits from, any quantum-hardware or quantum-software company, and
neither author is an author of any of the primary studies included in the review. No outcome of the
review affects the authors' funding or opportunities.

**Overlapping authorships**
None. Neither author (Yeshwanth Guru, Dev Kunwar Singh Chauhan) is an author or co-author of any of
the 72 primary studies or of the 107 foundational works in the review; this was checked against the
full reference list. Because there is no overlap, no reviewer had to be excluded from screening,
data extraction, quality assessment, or synthesis of any study.
