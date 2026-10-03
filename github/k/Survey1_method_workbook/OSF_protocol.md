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

**Entities to extract** (Extraction section; columns of extraction_table.csv and
quality_appraisal.csv)
1. Metadata: study label (first author, year), year of publication, publication status (journal
   article, conference paper, book or chapter, preprint), venue, and DOI or arXiv identifier.
2. Study design and methods: robotic function and task; quantum technology and platform (e.g.,
   quantum annealer, gate-based processor, quantum sensor, quantum link); quantum or
   quantum-inspired method; experimental set-up (theory, simulation, hardware run, robot simulator,
   physical robot, field trial); problem size (robots, tasks, nodes, qubits); data used; classical
   baselines compared.
3. Results: key quantitative or qualitative result as reported (e.g., solution quality, runtime,
   success rate, parameter count, positioning error), and the comparison with the classical
   baseline where reported. No effect sizes were computed, because studies use different tasks
   and metrics.
4. Deployment details where reported: hardware access (cloud or on-premise), latency, number of
   shots, noise and error mitigation, size, weight, power, and cooling.
5. Limitations: the principal limitation, stated or unstated.
6. Derived classifications (assigned by the reviewers): evidence level (L1-L6) and quantum-execution
   tag (none / simulated / QPU / sensor or link hardware / classical).
7. Risk-of-bias / quality indicators: seven appraisal criteria (problem formulation, classical
   baseline, experimental realism, hardware and noise reporting, performance metrics,
   reproducibility including code or data availability, critical discussion), each met / partly
   met / not met.

**Extraction stages**
1. Primary data extraction (human): the first author read each included primary study in full and
   recorded the entities listed above in the extraction table (Excel), following the codebook.
2. Classification (human): the first author assigned each study an evidence level (L1-L6) and a
   quantum-execution tag; when in doubt, the lower level was assigned.
3. Quality appraisal (human): the first author judged each application study against the seven
   appraisal criteria (met / partly met / not met).
4. Review (human): the second author reviewed the extracted data, levels, tags, and appraisal
   judgments sequentially (after the first author), and disagreements were resolved by discussion.
5. Verification (human): every full text was checked against its bibliographic record, and all
   references were verified against publisher, DOI, or arXiv records.
6. Export (computer, supervised by a human): the final tables were exported to CSV; counts and
   cross-tabulations for the figures and tables were computed with Python scripts and checked
   against the tables by the first author.
There was no separate training or reliability-verification stage.

**Extractor instructions**
The first author extracted the data and the second author reviewed it, so no separate written
instructions were prepared beyond the codebook (provided with the dataset on Zenodo). The extractor
followed these rules:
1. Fill every column of the extraction table as defined in the codebook; record only what the study
   reports, and write "not reported" for missing details (hardware, shots, latency, code).
2. Evidence level: assign the highest level the study's own evidence supports (L1 theory; L2
   simulation; L3 part run on quantum hardware or a quantum sensor or link; L4 closed loop with a
   robot or high-fidelity robot simulator; L5 physical robot, vehicle, or mechanical control system;
   L6 end-to-end field deployment with a measured advantage over a classical baseline). When in
   doubt, assign the lower level. Mark simulated robot environments "(sim.)", laboratory set-ups
   "(lab)", and simulated circuits on real robot data "+ real data".
3. Execution tag: record where the quantum component actually ran (none, simulated, QPU, sensor or
   link hardware, classical); tag quantum-inspired algorithms on conventional hardware "classical",
   whatever the paper calls them.
4. Key result: report the main result in the study's own metric, together with the baseline it was
   compared with; do not convert results to a common scale.
5. Limitation: record the principal limitation, including any appraisal criterion not met.
6. Appraisal: judge each application study on the seven criteria as met, partly met, or not met;
   use "n/a" for hardware and noise reporting when the method runs on classical hardware; do not sum
   the judgments into a score.
7. Grade the version kept after de-duplication and record its publication status.
8. Pass the completed table to the second author for review; resolve disagreements by discussion.

**Extractor masking**
No masking was used. Both extractors are the authors of the review and knew its research questions
throughout. To limit the resulting bias, extraction recorded only what each study reported, the
evidence level and execution tag were defined by observable criteria (where the quantum component
ran and on what platform) rather than by judgment of a study's claims, the lower level was assigned
when in doubt, and all extracted data and judgments are published for checking.

**Extraction reliability**
- Primary data extraction: one extractor (first author).
- Evidence levels and execution tags: assigned by one extractor (first author).
- Quality appraisal: one extractor (first author).
- Review: the second author reviewed all extracted data, levels, tags, and appraisal judgments
  after the first author (sequential, not independent); disagreements were resolved by discussion.
No round was carried out independently by two extractors, so extractor agreement could not be
measured and no agreement statistic (e.g., Cohen's kappa) is reported. This is stated as a
limitation in the article's threats to validity.

**Extraction reconciliation procedure**
Each round had one extractor, so there were no parallel extractions to reconcile. Where the second
author, reviewing the extracted data, levels, tags, or appraisal judgments, disagreed with the
first author, the two authors re-read the relevant part of the study and discussed it against the
codebook until they reached consensus; the agreed value was entered in the table. For evidence
levels, if doubt remained, the lower level was assigned. No third reviewer was involved.

**Extraction procedure justification**
- Entities: each entity serves a research question. Robotic function, task, and method answer RQ1;
  set-up, platform, evidence level, and execution tag answer RQ2; the execution tag and the
  baseline comparison separate genuinely quantum from quantum-inspired or dequantizable results
  (RQ3); deployment details (latency, shots, noise, size, weight, power, cooling) answer RQ4; and
  key results, limitations, and appraisal judgments inform the agenda (RQ5). Metadata (year,
  publication status) are needed because the field is young and many results are preprints.
  Results were recorded in each study's own metric, not converted to effect sizes, because the
  tasks and metrics differ too much to be put on one scale.
- Evidence scale and execution tag: a single ordered scale lets very different studies (theory,
  simulation, hardware runs, field trials) be compared, and recording where the quantum component
  ran prevents simulated or quantum-inspired results from being read as quantum-hardware results.
  The appraisal judgments are reported per criterion rather than summed, because a total score
  would hide which criterion a study fails.
- Extraction rounds: one extraction round followed by a review was proportionate for a two-person
  team and a corpus of 72 primary studies.
- Reliability assurance: sequential review by the second author, rather than independent double
  extraction, was a pragmatic choice without funding or additional reviewers. Its cost is that
  agreement cannot be measured; to compensate, the levels are defined by observable criteria, the
  lower level is assigned when in doubt, and every extracted value and judgment is published.
- Reconciliation: with two authors, discussion to consensus, with re-reading of the study, was the
  simplest workable procedure.

**Data management and sharing (extracted entities)**
All extracted entities are shared on Zenodo (DOI to be added), licence CC BY 4.0, without embargo or
access conditions; the dataset is published no later than the submission of the article.
Files: extraction_table.csv (all extracted entities, metadata, levels, and tags for every primary
study; CSV, UTF-8), quality_appraisal.csv (appraisal judgments; CSV, UTF-8), codebook.md
(definitions of every column and code; Markdown), search_strings.md, and README.md. The working
Excel file is not shared; the CSV files contain the same final data.
FAIR:
- Findable: persistent DOI from Zenodo, rich metadata (title, creators with ORCIDs, description,
  keywords), and a link from the article's Data Availability section and from this registration.
- Accessible: open access over HTTPS from Zenodo, with no login required; metadata remain available
  even if files were withdrawn.
- Interoperable: open, non-proprietary formats (CSV, Markdown); controlled vocabularies for evidence
  level, execution tag, publication status, and appraisal judgments, defined in the codebook.
- Reusable: CC BY 4.0 licence, codebook, provenance described in the README and the article, and
  each study identified by its DOI or arXiv identifier.
5-star open data: three stars (open licence, structured data, non-proprietary format); each study
row carries a DOI or arXiv identifier, so the data link to the sources, but the files are not
published as linked data (RDF).

**Miscellaneous extraction details**
- Which studies received which steps: all 72 primary studies were extracted; the 7 reviews were
  extracted but not assigned an evidence level; the 6 purely theoretical (L1) studies were graded
  but not quality-appraised, leaving 59 appraised application studies.
- Preprints: 16 primary studies were preprints when graded; the version available at the search
  date was used, and the publication status column records this, so levels may change once these
  studies are published.
- Full-text access: for 3 studies (Windmann et al. 2023; Mannone et al. 2023; Mannone et al. 2025)
  the full text was not yet available at registration; two appraisal criteria that need the full
  text (hardware and noise reporting; reproducibility) will be completed when it is obtained, before
  the dataset is published.
- Code and data availability: checked for the 56 studies whose full texts could be examined.
- Before extraction, every PDF was matched against its bibliographic record; mislabeled files and
  wrong metadata were corrected.

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

**Planned data transformations** (Synthesis and Quality Assessment section)
No effect sizes were computed or converted, because the studies use different tasks, metrics, and
baselines. The extracted data were transformed as follows:
1. Recoding into the taxonomy: each study's robotic task was coded into one of five robotic
   functions (optimization; planning; learning; sensing and communication; decision-making and
   reasoning), and its method into a method family (quantum optimization; quantum search; quantum
   learning, including machine learning and reinforcement learning; quantum sensing and
   communication; hybrid quantum-classical architectures; quantum cognition and quantum-probability
   models), with quantum-inspired classical methods tagged separately.
2. Counting: numbers of studies per evidence level, per execution tag, per robotic function, per
   method family, per publication year, and per publication status.
3. Cross-tabulation: evidence level by execution tag, to show how many results at each level used
   quantum hardware, simulation, or classical hardware.
4. Appraisal summaries: for each of the seven criteria, the number of appraised studies judged met,
   partly met, and not met (no total score per study).
5. Timescales: reported or documented latencies (control and planning loop rates, cloud queueing,
   compilation, shots, optimizer iterations) placed on one time axis to compare quantum processing
   times with robot loop budgets.
6. Resource estimate: for one representative algorithm (Grover-based localization), logical and
   physical resources and wall-clock time were estimated from published fault-tolerance cost
   models and compared with the classical alternative.

**Missing data**
Authors were not contacted, and missing information was not imputed.
- Unreported details (e.g., hardware, number of shots, latency, noise, code availability) were
  recorded as "not reported". Missing reporting is treated as a finding in itself: it lowers the
  relevant quality-appraisal judgment (e.g., hardware and noise reporting, reproducibility) and is
  counted in the appraisal summaries.
- Evidence levels were assigned only from what was reported; when the information needed to place a
  study at a higher level was missing, the lower level was assigned.
- Where no classical baseline was reported, the study was recorded as having none, and no
  comparison with classical methods was inferred.
- Where a full text could not be obtained, the study was assessed from the available record, and
  any appraisal criterion that could not be judged was left blank and reported as such rather than
  guessed.
- Counts and percentages state their denominator (e.g., 14 of the 56 studies whose full texts could
  be checked released code or data).

**Data validation**
1. Source identity: every full text was matched against its bibliographic record; mislabeled files
   and wrong metadata were corrected, and all references were verified against publisher, DOI, or
   arXiv records.
2. Versions: for each preprint, a published version was searched for; where one existed, the most
   complete version was used (E3), and the publication status column records which version was
   graded.
3. Review: the second author checked every extracted value, level, tag, and appraisal judgment
   against the source; errors were corrected by consensus.
4. Triangulation with later work: claims of quantum advantage were checked against later studies
   that reproduced or challenged them (e.g., classical simulation or dequantization results), and
   such challenges are reported next to the original claim.
5. Internal consistency: the counts in the text, tables, figures, and CSV files were cross-checked
   against one another, and the figures were regenerated from the final data.
6. File checks: the shared CSV files were checked automatically for structure (every row has the
   same number of columns) and for an identifier (DOI, arXiv, URL, or citation) in every row; errors
   were corrected.
Validity criteria: a data point is valid if it is traceable to a specific passage, table, or figure
of the graded source. Values that could not be traced were removed or recorded as "not reported".
Studies whose results were contradicted by later work were kept, with the contradiction reported,
and their evidence level reflects only what they themselves demonstrated.
Retractions: on 3 October 2026, the DOIs (148) and titles of all 185 references, including the 72
primary studies, were matched against the full Retraction Watch Database (Crossref open dataset,
72,870 records, current to 22 September 2026); none had been retracted.

**Quality assessment**
Standard tools (Cochrane Risk of Bias, GRADE, GRADE-CERQual) were not used, because they are designed
for clinical trials and health evidence and do not fit theoretical, simulation, and hardware
studies in computing and robotics. Quality was instead assessed on two levels:
1. Strength of evidence (per study): every non-review primary study was placed on a six-level
   evidence scale (L1 argued; L2 simulated; L3 run on quantum hardware; L4 closed loop with a robot
   or robot simulator; L5 physical robot or vehicle; L6 end-to-end deployment with a measured
   advantage over a classical baseline), with a quantum-execution tag recording where the quantum
   component ran. This plays the role GRADE plays in health reviews: it states how far each result
   is from a deployed, validated benefit.
2. Risk of bias and reporting quality (per study): each of the 59 application studies was appraised
   against a seven-criterion rubric (supplementary Table S4), each judged not met, partly met, or met:
   Q1 problem formulation (task unclear / simplified without justification / fully specified);
   Q2 classical baseline (none / basic or untuned / state-of-the-art and tuned);
   Q3 experimental realism (theory or toy example / simulation or small QPU run / physical robot or
   realistic field setting);
   Q4 hardware and noise reporting (not reported / partly / device, qubits, shots, noise, and
   mitigation reported);
   Q5 performance metrics (qualitative only / task metric only / task metric plus runtime, latency,
   or resources);
   Q6 reproducibility (no details / partial parameters / code and data or full parameters);
   Q7 critical discussion (absent / brief / explicit limitations and threats to validity).
   Q4 is "n/a" for quantum-inspired methods on classical hardware.
How quality is weighed in the synthesis: judgments are not summed into a score; the unmet criteria
are reported as each study's principal limitation; each claim in the synthesis is stated with the
evidence levels of the studies behind it; results without a state-of-the-art classical baseline
(Q2) are not taken as evidence of advantage; and the appraisal summaries (number of studies meeting
each criterion) are reported to show where the field's evidence is weakest.

**Synthesis plan**
Narrative synthesis, structured by the taxonomy; no meta-analysis, because tasks, metrics, and
baselines are too heterogeneous to pool. No subgroup or moderator analyses, no statistical model,
and no analysis code beyond the scripts that count studies and draw the figures.

Tier 1, primary synthesis (answers RQ1-RQ3):
1. Method-by-method synthesis: for each method family (quantum optimization; quantum search;
   quantum learning; quantum sensing and communication; hybrid architectures; quantum cognition),
   the studies are described with their robotic task, evidence level, execution tag, strongest
   baseline, key result, and principal limitation (RQ1).
2. Synthesis across robotic functions: for each of the five functions, the highest evidence level
   reached, the number of studies at each level, and whether any genuinely quantum result has been
   shown on hardware or on a robot (RQ1, RQ2).
3. Evidence hierarchy: the distribution of studies over L1-L6, cross-tabulated with the execution
   tag (RQ2).
4. Claims versus evidence: each advantage claim is compared with its evidence level, its baseline
   (Q2), and later classical-simulation or dequantization results, to separate genuinely quantum
   benefits from quantum-inspired or removable ones (RQ3).

Tier 2, cross-cutting analyses (answers RQ4):
5. Latency gap: robot control and planning loop budgets compared with documented quantum
   processing times (queueing, compilation, shots, optimizer iterations).
6. Scalability: problem sizes reached on hardware compared with the sizes of real robot problems.
7. Worked resource estimate: fault-tolerant resources and wall-clock time for one representative
   algorithm (Grover-based localization), compared with the classical alternative.

Tier 3, agenda (answers RQ5):
8. Research agenda and reporting checklist derived from the gaps found in tiers 1-2, with directions
   ordered by time horizon (near term to 2030, and beyond).

Interpretation rules: a result counts as evidence of quantum advantage only if it was obtained on
quantum hardware, against a state-of-the-art classical baseline, with end-to-end time reported;
claims are always stated with the evidence levels behind them; conclusions resting on few studies,
on preprints, or on a single unreplicated result are labelled as tentative.

If parts of the plan cannot be executed: where a function has too few studies for a synthesis, it
is described study by study and the gap is reported; where studies do not report the data needed
for the latency or scalability analyses, documented platform figures are used and labelled as
such; where the resource estimate cannot be made precise, it is presented as an order-of-magnitude
estimate with its assumptions stated.

**Criteria for conclusions / inference criteria**
No statistical criteria (effect size, significance level) apply, because there is no meta-analysis.
Conclusions follow these qualitative criteria:
1. Quantum advantage: a result is accepted as evidence of a quantum advantage for a robotic function
   only if (a) the quantum component ran on quantum hardware (execution tag QPU or sensor/link
   hardware), (b) it was compared with a state-of-the-art, tuned classical baseline (Q2 met), and
   (c) the advantage holds end to end, including embedding, queueing, and post-processing time.
   Results that fail (a) are reported as simulated or quantum-inspired; results that fail (b) or (c)
   are reported as unconfirmed.
2. Deployment readiness: a function is described as demonstrated on robots only if at least one
   study reaches L5 (physical robot or vehicle), and as deployed only at L6.
3. Robustness of a finding: a conclusion is stated firmly only if it rests on more than one
   independent study and not solely on preprints; otherwise it is labelled tentative or as
   awaiting replication.
4. Dequantization: a claimed speed-up is not counted as quantum if a classical algorithm under the
   same input assumptions matches it.
5. Saturation: no formal saturation criterion was used; the search closed in October 2026, before
   submission.

**Synthesist blinding**
No blinding was used. The synthesis was carried out by the two authors, who designed the review and
knew its research questions; no external analyst was involved. To limit the resulting bias, the
inference criteria for quantum advantage, deployment readiness, and robustness were applied to
every study in the same way, each claim is reported with the evidence levels behind it, and all
extracted data and judgments are published so that others can repeat the synthesis.

**Synthesis reliability**
Two synthesists, not independent. The first author drafted the synthesis (the method-by-method
synthesis, the cross-cutting analyses, and the agenda); the second author reviewed it against the
extracted data, and disagreements were resolved by discussion. No independent parallel synthesis was
carried out and no agreement measure was computed. The counts, cross-tabulations, and figures were
generated by scripts from the shared data files, so they can be reproduced exactly.

**Synthesis reconciliation procedure**
Where the second author disagreed with a synthesis decision (e.g., how a result was interpreted,
whether a claim met the criteria for quantum advantage, or how firmly a conclusion was stated), the
two authors returned to the extracted data and the original studies and discussed the point against
the pre-specified inference criteria until they reached consensus. Where doubt remained, the more
cautious interpretation was adopted (e.g., labelling a conclusion as tentative). No third person was
involved.

**Publication bias analyses**
No statistical publication-bias analysis (e.g., funnel plots, Egger's test, trim-and-fill, PET-PEESE,
selection models) was performed, because these methods need comparable effect sizes and there is
no meta-analysis. Publication bias was addressed qualitatively: (1) preprints were included (16 of
the 72 primary studies), which reduces dependence on what journals accept; (2) negative and null
results found in the literature, such as classical solvers matching or beating quantum annealers,
are reported alongside positive claims; (3) the threats-to-validity section states that publication
bias probably favors positive results and that unpublished industrial work is missing; and
(4) advantage claims are weighed by their evidence level and baseline rather than taken at face
value.

**Sensitivity analyses / robustness checks**
No statistical sensitivity analyses apply (no meta-analysis). Three robustness checks were made:
1. Excluding preprints: the evidence distribution was recomputed without the 16 preprints (56 studies
   remain: L1 6, L2 14, L3 19, L4 8, L5 3, L6 0, reviews 6). The main conclusion does not change: no
   quantum computational method reaches a physical robot with a measured advantage in either set.
   The only L6 study (quantum magnetic navigation) is a preprint, so the sensing result depends on a
   single unreplicated preprint; this is stated in the article.
2. Conservative grading: levels were assigned at the lower level when in doubt, so the reported
   distribution is, if anything, a lower bound on the evidence; the conclusions about the absence of
   end-to-end advantage would not be weakened by this choice.
3. Resource estimate under favorable assumptions: the fault-tolerant estimate for Grover-based
   localization was computed under two oracle-cost scenarios (table lookup and a hypothetical
   logarithmic-time qRAM) and with an error-corrected gate time more optimistic than published
   estimates (10 microseconds versus about 170 microseconds), so that the conclusion (no practical
   advantage at realistic map sizes) holds even under assumptions that favor the quantum algorithm.

**Synthesis procedure justification**
- Transformations: results were kept in each study's own metric and not converted to effect sizes,
  because the studies differ in task, metric, and baseline, and any common scale would rest on
  assumptions the data cannot support. The transformations used (coding into the taxonomy, counts,
  cross-tabulations) need no such assumptions; the latency comparison uses documented timescales,
  and the resource estimate uses published fault-tolerance cost models, with its assumptions stated
  and chosen to favor the quantum algorithm.
- Data integrity and missing data: unreported details are recorded as "not reported" rather than
  imputed, because missing reporting is itself one of the review's findings; bibliographic
  verification, version checks, the retraction check, and automatic file checks make the shared data
  traceable and usable.
- Synthesis plan: a narrative synthesis structured by method family and robotic function is the
  standard approach when studies are too heterogeneous to pool; the cross-cutting analyses
  (latency, scalability, resource estimate) were added because these constraints decide whether a
  quantum method can work on a robot, and individual studies rarely address them.
- Inference criteria: requiring hardware execution, a state-of-the-art classical baseline, and
  end-to-end timing before accepting an advantage reflects the main weaknesses of the literature
  (simulated results, weak baselines, and ignored overheads), and the dequantization criterion
  follows established results showing that some claimed quantum speed-ups vanish against the best
  classical algorithms.
- Blinding, reliability, and reconciliation: an external analyst was not available to a two-person
  unfunded team; instead, the same written criteria were applied to every study, the second author
  reviewed the synthesis, disagreements were resolved toward the more cautious interpretation, and
  all data and judgments are published so the synthesis can be repeated.

**Synthesis data management and sharing**
Shared on Zenodo with the dataset (DOI to be added), licence CC BY 4.0, no embargo:
- make_figures.py and figstyle.py (Python 3 scripts, plain text): read extraction_table.csv and
  reproduce the counts, the evidence-level and publication-year figures, and the flow diagram.
- The outputs of the synthesis are the article and its supplementary material (tables of counts,
  cross-tabulations, appraisal summaries, synthesis table, reporting checklist, and roadmap).
There are no separate analysis notes beyond the shared data files and the article; the synthesis is
narrative, so there is no statistical analysis script.
[ALTERNATIVE if the scripts are not shared: "The figure scripts (Python) are available from the
authors on request."]

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
