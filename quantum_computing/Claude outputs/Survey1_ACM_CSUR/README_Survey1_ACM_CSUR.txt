SURVEY 1 – ACM COMPUTING SURVEYS (CSUR) SUBMISSION PACKAGE
Quantum Computing for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints
=====================================================================================================

FILES
  Survey1_CSUR_LaTeX_Overleaf.zip       Official submission source (ACM acmart, acmsmall format)
      main.tex                          Manuscript (\documentclass[acmsmall,screen,review]{acmart})
      supplement.tex                    Online supplementary material
      refs.bib                          149 verified BibTeX entries (full author names, DOIs)
      figures/                          Figures 1-5 + PRISMA flow diagram (300 dpi PNG)
  Survey1_ACM_CSUR_Manuscript.docx      Word version of the same manuscript, in acmsmall page layout
  Survey1_ACM_CSUR_Supplementary_Material.docx   Word version of the supplement
  extraction_table.csv                  Data-extraction table for the 58 primary studies (supplementary data)
  Survey1_CSUR_Cover_Letter.docx        Cover letter to the Editor-in-Chief

HOW TO PRODUCE THE SUBMISSION PDF (recommended route)
  1. overleaf.com -> New Project -> Upload Project -> select Survey1_CSUR_LaTeX_Overleaf.zip
  2. Set main.tex as the main document and compile (pdfLaTeX). acmart and
     ACM-Reference-Format.bst are pre-installed on Overleaf.
  3. Compile supplement.tex the same way (Menu -> Main document -> supplement.tex).
  Locally: pdflatex main; bibtex main; pdflatex main; pdflatex main

STRUCTURE (CSUR conventions)
  Unstructured abstract (241 words); CCS concepts (CCSXML); keywords; ACM author-year
  citations; taxonomy figure in Section 3; comparison table with earlier surveys (Table 1);
  open problems derived from the taxonomy (Section 12); reporting checklist (Table 4);
  research roadmap (Table 5); figures carry \Description alt text (ACM accessibility);
  data-availability statement; detailed tables moved to the online supplement.
  Body ~12,600 words; about 30 pages of main text in acmsmall + ~14 pages of references.

BEFORE YOU SUBMIT (things only you can supply)
  [ ] Authors, affiliations, ORCIDs, e-mails (main.tex "AUTHORS" block; docx title block).
  [ ] Section 3.2: date of the last search.
  [ ] Section 3.4 and supplement Table S2 / Figure S1: PRISMA counts (records identified,
      duplicates, screened, full texts, exclusions by reason). These were not invented.
  [ ] Section 3.5: who extracted/scored the data and how disagreements were resolved.
  [ ] Supplement Table S3/S4: per-study quality scores, if you want to report them.
  [ ] Acknowledgments / funding, competing-interest statement, protocol registration (or say none).
  [ ] Cover letter: date, suggested reviewers, corresponding-author details.
  [ ] Check the live CSUR author-guidelines page (dl.acm.org/journal/csur/author-guidelines)
      for the current length limit and whether anonymized review is required. If it is,
      add "anonymous" to the \documentclass options (and use "Anonymous author(s)" in Word).
  [ ] Optionally regenerate the CCS concepts with the ACM CCS tool (dl.acm.org/ccs) and
      paste the new CCSXML into main.tex.
  All placeholders appear as red [FILL: ...] in the PDF and yellow-highlighted [FILL: ...] in Word.

REFERENCE VERIFICATION
  All 149 references were checked against publisher, DOI, arXiv, or the local PDFs.
  Corrections made relative to the earlier Survey 1 list include, for example:
    Tian2023 -> Physical Review Letters 133, 200801 (2024); Sinha2023 (Nav-Q) -> Quantum Machine
    Intelligence 7 (2025); Yu2025 (HQC-NBV) -> CVPR 2026; Antero2025 -> Robotics and Autonomous
    Systems 192 (2025); Larocca2025 -> Nature Reviews Physics 7 (2025); Mannone2025b -> retitled
    "Density Matrix-Based Dynamics for Quantum Robotic Swarms", RAS 200 (2026);
    Rebentrost2014 co-authors corrected (Mohseni, Lloyd); Fowler2012 -> Physical Review A;
    Garrett2021 full seven-author list; Henderson2020 4th author Tristan Cook; Lloyd 2013 (arXiv).
  Six entries could not be fully re-confirmed online and should be spot-checked:
    Wiebe2015 (pages), Nielsen2010 (DOI), Kaelbling1998 (pages/DOI), Tandon2017 (series volume),
    Wang2021 (a retitled journal version exists: J. Navigation 76(1):91-102, 2023 — consider citing it),
    Benioff2002 (chapter pages).
