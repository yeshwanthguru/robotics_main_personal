SURVEY 2 – ARTIFICIAL INTELLIGENCE REVIEW (SPRINGER NATURE) SUBMISSION PACKAGE
Quantum-Like Cognition and Decision-Making for Autonomous Agents, from Robotics to AI/ML Systems:
A Systematic Review
(structure follows the authors' outline: Parts A-E, Sections 1-25, Appendices A-E; a PRISMA 2020
systematic review prepared the same way as Survey 1, with the methods in Section 1.5)
=============================================================================================================

FILES
  Survey2_AIR_LaTeX_Overleaf.zip       Submission source: main.tex (Springer Nature sn-jnl, sn-basic author-year),
                                       supplement.tex (Online Resource 1), refs.bib (212 entries), figures/
                                       (Fig1-Fig9 numbered as in the paper, FigS1 PRISMA flow), sn-jnl.cls, bst/
  Survey2_AIR_LaTeX_Overleaf/main.pdf  Compiled manuscript (80 pages incl. references); supplement.pdf (53 pages)
  Survey2_AIR_Manuscript.docx          Word review copy of the manuscript (citations as plain text)
  Survey2_AIR_Online_Resource_1.pdf/.docx   Supplement: Table S1 extraction table (67 studies), S2 PRISMA
                                       checklist, S3 + Fig S1 flow of records, S4-S5 appraisal criteria and
                                       judgements (61 studies), S6 search record, S7 E5 exclusions,
                                       S8 theory and evidence studies (71), S9 summary of every graded study
  Survey2_AIR_Online_Resource_2_code.py   Reproduces the worked examples; "--rl" reruns the RL experiment (Table C1)
  Survey2_AIR_Online_Resource_3_extraction_table.csv   Table S1 as CSV
  Survey2_AIR_Online_Resource_4_quality_appraisal.csv  Table S5 as CSV
  Survey2_AIR_Cover_Letter.docx        Cover letter to the Editor-in-Chief (mentions the companion review)
  Survey2_Word_for_Mendeley/           Yellow cite-by-hand Word files + reference lookup (see its README)
  Survey2_data_package/                extraction_table.csv, quality_appraisal.csv, theory_evidence_studies.csv,
                                       study_summaries.csv (209 works), codebook.md, search_strings.md, README.md (upload to Zenodo)
  Survey2_method_workbook/             OSF_protocol.md (field-by-field OSF text), Zenodo_description.md,
                                       targeted_search_record.md, retraction_check_list.md,
                                       Survey2_method_workbook.xlsx (search log, screening, PRISMA counts, kappa)
  Survey2_fulltexts/                   PRIVATE: PDFs of cited works found in the repo, named by key (17 of 67
                                       application studies; 57 other works); index.csv lists what is missing
  Survey2_reference_list.md            Every cited work (212) with group, evidence level and full-text status;
                                       download checklist (137 missing PDFs) and the 21 new papers found by the
                                       literature check of 4 Oct 2026 (not yet added; decide after reading)
  Survey2_download_links.md            Clickable DOI/arXiv/Google Scholar links for the 137 cited works without a
                                       full text in the repository and the 22 new candidates
  Survey2_source_drafts/               Paper write-ups (source of the extraction data) and the earliest full draft
  tools/                               make_schematics.py (Figs 1-6, 8, 9), make_figures.py (Fig 7 evidence,
                                       Fig S1 PRISMA), figstyle.py (shared style), make_supplement.py
                                       (supplement.tex from the CSVs), build_word.sh (all Word files)

HOW TO PRODUCE THE SUBMISSION PDF
  Overleaf > New Project > Upload Project > Survey2_AIR_LaTeX_Overleaf.zip; main document main.tex (pdfLaTeX);
  compile supplement.tex the same way. Locally: pdflatex main; bibtex main; pdflatex main; pdflatex main.
  After editing a CSV in Survey2_data_package: python3 tools/make_supplement.py; python3 tools/make_figures.py;
  sh tools/build_word.sh.

WHAT CHANGED (October 2026)
  - All ten figures redrawn by script in a plain journal style: drawn at the printed width (372 pt) with
    Latin Modern text matching the manuscript, thin outlines, white/grey fills, one muted accent colour,
    600 dpi; no flat colour blocks or slide-style graphics. Content and numbers unchanged (Fig 9 re-run:
    30 seeds, same values as Table C1; raw runs in Survey2_data_package/figure_data/). Fig 2 caption now
    says solid/dashed path instead of blue/orange.
  - Reviewer-style fixes: title now says "Quantum-Like" (the review's own term for its core; "quantum-
    inspired" is a different class); Section 1.4 states that robots are the motivating case but only 17 of
    67 studies; a one-rule I1/E5 boundary with the borderline case flagged (Daglarli2025, Online Resource 3);
    a sensitivity check without the 11 representation-only ML/NLP models (conclusions unchanged); the
    E1-E6 scale is justified and a second-rater sample is planned ([FILL] kappa); section roles stated
    (13 vs 23; 15 vs 22 vs 24); Case Studies 1-2 labelled worked examples and Case Study 3's limits stated;
    circuit-RL claim now rests on primary sources, not only the companion; Khrennikov2026 added to Table 9.
  - Summaries checked against full texts in the repository: Lanza2020/2021 (IBM Quantum Experience
    hardware; 10^6 simulated measurements), Ho2022 (design only), Lawless2023, Humr2025, vanderMeer2025
    (34 participants of the earlier study) now marked "Full text".
  - Evidence-based framing: headings that promised more than the evidence shows were reworded (Section 5.6
    "Where Quantum Models Outperform ..., and Where They Do Not"; 9.2, 10.3, 14.2, 16.2); the thesis that
    quantum cognition is the hardware-free quantum route whose value is representational, not computational,
    is stated in Sections 1.3, 2.5.4 and 25.2.
  - Tier 1 (Section 6) deepened to the deepest tier, with Table 4 (models, strongest evidence, agent
    studies and gap per function); Sections 10.1, 10.3, 21.4, 24 (Table 10, open problems with a first
    experiment each) and 25.1 (answers to RQ1-RQ5) expanded. All new statements come from the data package.
  - References: Maksymov2025 -> Maksymov2026 (Springer book, 2026); Busemeyer2012 notes the 2024 2nd edition.
  - Word build: section cross-references are now resolved before pandoc (forward references used to print
    as "[sec:...]"), and tables use relative column widths (absolute widths made pandoc drop text).
  - Restructured to the authors' outline (Part A Foundations 1-4, Part B Theory 5-7, Part C Applications and
    Validation 8-16, Part D Grounding 17-20, Part E Integration and Future 21-25, Appendices A-E), keeping all
    systematic-review content: methods in Section 1.5, evidence levels Table 1, glossary Table 3 (Section 4.4),
    evidence map and quality in Section 13.3, case studies and the RL experiment in Section 16, code in
    Appendix B, raw results in Appendix C, protocols and checklist in Appendix D.
  - Scope (Section 1.4) states that quantum-inspired optimisation heuristics (quantum-behaved PSO, quantum-inspired
    evolutionary algorithms for path planning, scheduling, SLAM) are outside this review; Survey 1 summarises them.
  - Content of the two source drafts (Survey2_source_drafts/) carried into the manuscript, Online Resource 1
    (Section S9, summary of every graded study) and Survey2_data_package/study_summaries.csv.
  - "Classical Approach (Deep Q-Learning)" in the outline is titled "(Q-Learning)" in Section 16.3, because the
    experiment uses tabular Q-learning; topics that belong to Survey 1 (variational-circuit RL, Grover
    planning) are pointers to the companion review only.
  - Systematic review: research questions RQ1-RQ5, four-stage search (incl. a logged targeted search on
    4 Oct 2026), eligibility criteria I1-I3 / E1-E6, selection, extraction, seven-criterion quality appraisal,
    evidence levels E1-E6, threats to validity, PRISMA 2020 checklist and flow diagram.
  - No Survey 1 content: new criterion E5 moves 11 quantum-computing studies (variational-circuit RL, QMARL,
    Grover planning, swarm circuits, quantum communication) out of the primary studies; they are cited once
    and listed in Table S7. Survey 1 is cited as the companion review (Guru2026). Text overlap with Survey 1
    checked: under 1%, method boilerplate only, which was reworded.
  - Four studies added by the targeted search: Kak 2018, Hoorn and Ho 2019, Essalmi et al. 2026,
    Nebli et al. 2026. Application studies: 74 -> 67; evidence levels E1 6, E2 18, E3 9, E4 29, E5 5, E6 0.
  - Authors, affiliation, e-mails, funding, competing interests and CRediT roles filled in.
  - All pseudo-maths (\ensuremath fragments that printed "|" as a dash) rewritten as proper LaTeX maths.
  - Abstract 249 words (limit 150-250); 6 keywords (limit 4-6).
  - Retraction check: all 212 references against Retraction Watch (22 Sep 2026): none retracted.
  - RL experiment re-run: all values of Table C1 reproduced (one total corrected from 8,162 to 8,163).

BEFORE YOU SUBMIT (red [FILL] in the PDF; yellow in the Word files)
  [ ] Second rater: independently re-grade a random 20% sample (28 of the 138 graded studies: evidence level
      and Q1-Q7) and report Cohen's kappa in Section 1.5.6 (red [FILL]). Ask the professor or a colleague.
  [ ] Essalmi2026: the full text is in Survey2_fulltexts/primary but the extraction used the abstract;
      re-extract from the PDF (counts "16 of 67 from full text" become 17).
  [ ] Professor to confirm: "the second author reviewed the inclusion decisions, evidence levels and appraisal
      judgements; disagreements were resolved by discussion" (Section 1.5.4), and the CRediT roles.
  [ ] OSF: register Survey 2 retrospectively from Survey2_method_workbook/OSF_protocol.md (new OSF project);
      fill the [CHECK] items (start month); put the OSF DOI in Section 1.5.
  [ ] Zenodo: new upload from Survey2_data_package (Zenodo_description.md); put the DOI in Data availability.
  [ ] Code repository URL and licence (Appendix B and Code availability), or delete those two [FILL]s.
  [ ] Cover letter: date and suggested reviewers. REMINDER: corresponding author still undecided (set to Yeshwanth).
  [ ] Full texts: 50 of the 67 application studies were extracted from abstracts (Survey2_fulltexts/README.md
      lists them). Add each PDF to the repository, then re-check the extraction and fill the Q6 "?" cells.
  [ ] Five records from the targeted search could not be retrieved (targeted_search_record.md); check them.
  [ ] Companion reference (Guru2026): update the note to "under review" once Survey 1 is submitted.
  [ ] Declare generative-AI assistance as the journal requires (Springer: in the Methods section or
      acknowledgements; check the current AIR policy).
  [ ] Check the live AIR submission guidelines (abstract 150-250 words and 4-6 keywords were confirmed; AIR is
      fully open access since 2024, so check the APC or institutional agreement).
  [ ] Optional: blind re-grading of the 20 studies in the workbook's Grading_Check sheet for a kappa value.
