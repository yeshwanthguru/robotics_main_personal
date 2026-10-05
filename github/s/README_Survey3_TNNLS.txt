SURVEY 3 – IEEE TRANSACTIONS ON NEURAL NETWORKS AND LEARNING SYSTEMS (TNNLS) SUBMISSION PACKAGE
Meta-Learning Orchestration of Learning Modalities on Resource-Constrained Robots: A Systematic Review
(a PRISMA 2020 systematic review prepared the same way as Surveys 1 and 2; section outline from
Survey3_source_drafts/Survey3_Adaptive_Orchestration_Outline.docx)
=============================================================================================================

FILES
  Survey3_TNNLS_LaTeX_Overleaf.zip     Submission source: main.tex (IEEEtran journal, two columns), supplement.tex,
                                       refs.bib (185 entries: 180 reviewed works, 2 method references, 3 companion
                                       manuscripts), figures/ (Fig1-Fig6)
  Survey3_TNNLS_LaTeX_Overleaf/main.pdf  Compiled manuscript (21 pages incl. references); supplement.pdf (59 pages)
  Survey3_TNNLS_Manuscript.docx        Word review copy of the manuscript (IEEE numbered citations)
  Survey3_TNNLS_Supplementary.docx     Word copy of the supplement: S1 PRISMA checklist, S2 search strategy,
                                       S3 corrections, S4 coding of all 180 works, S5 appraisal, S6 summaries
  Survey3_TNNLS_Supplementary_routing_sim.py   Illustrative simulation (part 1: calibrated vs miscalibrated
                                       routing; part 2: meta-learned calibration on new tasks); writes routing_results.json
  Survey3_TNNLS_Cover_Letter.docx      Cover letter to the Editor-in-Chief
  Survey3_Word_for_Mendeley/           Cite-by-hand Word files (every citation in yellow) and reference lookup
  Survey3_data_package/                extraction_table.csv (180), quality_appraisal.csv (161), study_summaries.csv,
                                       codebook.md, search_strings.md, README.md (upload to Zenodo)
  Survey3_method_workbook/             OSF_protocol.md (field-by-field OSF text and the list of corrections),
                                       Zenodo_description.md, targeted_search_record.md (4 Oct 2026),
                                       retraction_check_list.md (no retracted work)
  Survey3_fulltexts/                   PRIVATE: index.csv of every cited work; no full text of the 180 reviewed
                                       works is in the repository (searched by arXiv id and first-page title)
  Survey3_reference_list.md            Every cited work with level, identifier, full-text status and verification note
  Survey3_download_links.md            Download checklist (real-robot studies first) with DOI/arXiv/Scholar links,
                                       and the four candidates of the targeted search
  Survey3_source_drafts/               Structured write-ups of the 180 works (generated from the data package),
                                       section outline, thesis outline
  tools/                               make_data_package.py, make_figures.py, figstyle.py, make_supplement.py,
                                       make_reference_list.py, make_writeups_doc.py, retraction_check.py,
                                       build_word.sh (+ prep_tex_for_word.py, Lua filters, ieee.csl);
                                       data/ holds the write-ups, the hand-coding files and the counts
  model/                               Companion model paper: order-aware human models for robot questioning and
                                       trust (code, simulations, quantum circuits, cloud scripts, manuscript).
                                       See model/README.md and model/PUBLICATION_PLAN.md

HOW TO PRODUCE THE SUBMISSION PDF
  Overleaf > New Project > Upload Project > Survey3_TNNLS_LaTeX_Overleaf.zip; compile main.tex and supplement.tex
  with pdfLaTeX (IEEEtran is built in). Locally: pdflatex main; bibtex main; pdflatex main; pdflatex main.
  After changing tools/data (write-ups or coding): python3 tools/make_data_package.py; python3 tools/make_figures.py;
  python3 tools/make_supplement.py; python3 tools/make_reference_list.py; sh tools/build_word.sh (run from github/s).

WHAT CHANGED (October 2026)
  - New title and framing around meta-learning orchestration on resource-constrained robots; the orchestrator is
    treated as a meta-learner throughout (Sections I-B, XI, XIV-F, XVIII).
  - Systematic review method (Section II): PRISMA 2020, eligibility criteria I1-I3 / X1-X5, three search stages
    (initial list 108; structured searches 72; logged targeted search on 4 Oct 2026 with four candidates
    recorded), structured extraction, evidence levels E1-E6 + R/S, quality appraisal Q1-Q7 (Table II),
    threats to validity, retraction check, PRISMA flow (Fig. 2) and checklist (supplement S1).
  - New evidence profile (Section III, Figs. 3-4): every non-review work hand-coded for the platform its
    inference needs and the confidence signal it exposes. Of 65 real-robot studies, 5 run on a Pi-class
    processor and 2 of those expose a confidence signal; no work arbitrates between more than two
    heterogeneous learning modalities with a learned, calibrated, budgeted gate.
  - Meta-learning section rewritten (Section XI): bilevel formulation, Table VI comparing meta-learners by
    the on-robot cost of adaptation, and meta-learned calibration with a new simulation (Fig. 6(b), Table B2):
    a calibration prior meta-learned on 50 tasks gives 0.82 success in the first 25 steps of a new task,
    against 0.77 when learning from scratch (oracle 0.85).
  - Answers to the five research questions (Section XVI); new open problem on human-model uncertainty as an
    orchestration signal, linked to the model paper in model/ (Section XVII-E).
  - Conclusion states the final verdict: supported in principle, not demonstrated; the decisive test is a
    real-robot study showing the orchestrated system beats its strongest single modality at equal compute.
  - Authors, affiliation, ORCIDs and biographies placeholders filled; Data Availability added.
  - All figures redrawn by script at IEEE print sizes (Times-like text, muted palette, 600 dpi); the old
    qualitative positioning figure was replaced by the data-based Fig. 4.
  - Wording: neutral and impersonal throughout; notes in the data package rewritten as plain verification
    notes; spelling fixes (generalist, realistic, characteristic, specialist, optimism).
  - Checks: no reviewed work overlaps Survey 1 or Survey 2 (title match); text overlap with both manuscripts
    under 0.3% (markup only); LanguageTool (en-US) findings fixed or false positives; retraction check clean.

BEFORE SUBMITTING
  [ ] OSF registration DOI and Zenodo DOI in main.tex (red [FILL] fields), cover letter and OSF text.
  [ ] Second-rater sample and Cohen's kappa for evidence levels and edge class (Section II-D).
  [ ] Download the full texts (Survey3_download_links.md), confirm the appraisal codes and the write-ups
      based on abstracts, and screen the four stage-3 candidates; rerun the tools if anything changes.
  [ ] Acknowledgment/funding, biographies, manuscript dates, statement on generative-AI use if required.
  [ ] Check the current TNNLS page limits for survey papers (the manuscript is 21 pages with references).
  [ ] Submit through ScholarOne with the PDF, the source zip, the supplement and the simulation code.
