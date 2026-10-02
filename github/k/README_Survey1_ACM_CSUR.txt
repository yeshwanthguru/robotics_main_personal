SURVEY 1 – ACM COMPUTING SURVEYS (CSUR) SUBMISSION PACKAGE
Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints
(retitled from "Quantum Computing for ..."; title and authors are updated in all .docx files)
=====================================================================================================

FILES
  Survey1_CSUR_LaTeX_Overleaf.zip       Official submission source (ACM acmart, acmsmall format)
      main.tex                          Manuscript (\documentclass[acmsmall,screen,review]{acmart})
      supplement.tex                    Online supplementary material
      refs.bib                          172 verified BibTeX entries (full author names, DOIs)
      figures/                          Figures 1-6 + PRISMA flow diagram (PNG); fig7_years.png is
                                        generated from extraction_table.csv
  Survey1_ACM_CSUR_Manuscript.docx      Word version generated from main.tex (tools/build_word.sh), with every
                                        citation as a Mendeley citation field and the reference list as a
                                        Mendeley bibliography field (see "WORD + MENDELEY" below)
  Survey1_ACM_CSUR_Supplementary_Material.docx   Word version of the supplement
  extraction_table.csv                  Data-extraction table for the 72 primary studies (supplementary data),
                                        including the quantum-execution tag of each study
  Survey1_CSUR_Cover_Letter.docx        Cover letter to the Editor-in-Chief

  Survey1_missed_papers.md              Literature cross-check (Oct 2026); all listed studies are now in the survey
  Survey1_candidate_refs.bib            BibTeX for those studies (already merged into refs.bib)

  tools/make_figures.py                 Regenerates Figs. 1, 2 and 5 and the PRISMA diagram (timeline milestones are listed in the script)

WORD + MENDELEY
  1. In Mendeley Reference Manager, import Survey1_CSUR_LaTeX_Overleaf/refs.bib
     (File > Import > BibTeX) so the library holds the same 172 references.
  2. Open Survey1_ACM_CSUR_Manuscript.docx in Word with the Mendeley Cite add-in. The
     citations are Mendeley Desktop-style fields carrying full reference data; if Mendeley
     Cite asks to convert legacy citations, accept. Choose a citation style (e.g.
     "Association for Computing Machinery") and refresh to restyle citations and references.
  3. Narrative citations (\citet, e.g. "Clark et al. (2019) asked ...") are rendered in
     narrative form now, but a Mendeley refresh turns them into parenthetical citations;
     re-type the author names in front of those citations if needed.
  4. To regenerate the Word file after editing main.tex: run tools/build_word.sh from this
     folder (needs pandoc >= 3).
 (recommended route)
  1. overleaf.com -> New Project -> Upload Project -> select Survey1_CSUR_LaTeX_Overleaf.zip
  2. Set main.tex as the main document and compile (pdfLaTeX). acmart and
     ACM-Reference-Format.bst are pre-installed on Overleaf.
  3. Compile supplement.tex the same way (Menu -> Main document -> supplement.tex).
  Locally: pdflatex main; bibtex main; pdflatex main; pdflatex main

STRUCTURE (CSUR conventions)
  Unstructured abstract (241 words); CCS concepts (CCSXML); keywords; ACM author-year
  citations; taxonomy figure in Section 3; comparison table with earlier surveys (Table 1);
  evidence level x quantum execution cross-tabulation (Table 4); open problems derived from
  the taxonomy (Section 12); reporting checklist (Table 5); research roadmap (Table 6); figures carry \Description alt text (ACM accessibility);
  data-availability statement; detailed tables moved to the online supplement.
  Body ~12,600 words; about 30 pages of main text in acmsmall + ~14 pages of references.

BEFORE YOU SUBMIT (things only you can supply)
  [x] Authors: Yeshwanth Guru (g_yeshwanth@ch.students.amrita.edu) and Dev Kunwar Singh Chauhan
      (c_devsingh@ch.amrita.edu), Amrita Vishwa Vidyapeetham, Chennai, India.
  [ ] Add departments and ORCIDs (main.tex, docx title block, cover letter).
  [ ] The Word manuscript has the new title, authors and AI-use disclosure, but NOT the
      body changes of the review revision (Table 4, Fig. 2, Section 10.4, rewording).
      The LaTeX source is the authoritative version.
  [ ] Cover letter lists Yeshwanth Guru as corresponding author - change if needed.
  [x] Generative-AI use is disclosed in the acknowledgments, as ACM policy requires.
  [ ] Section 3.2: date of the last search.
  [ ] Section 3.4 and supplement Table S2 / Figure S1: PRISMA counts (records identified,
      duplicates, screened, full texts, exclusions by reason). These were not invented.
  [ ] Section 3.5: who extracted/scored the data and how disagreements were resolved.
  [ ] Quality appraisal is reported qualitatively (unmet criteria = Limitation column of
      Table S1). If you did score studies 0/1/2, restore the scores in supplement Table S3.
  [ ] Update the title in Survey1_ACM_CSUR_Manuscript.docx and the cover letter.
  [ ] Acknowledgments / funding, competing-interest statement, protocol registration (or say none).
  [ ] Cover letter: date and suggested reviewers.
  [ ] Check the live CSUR author-guidelines page (dl.acm.org/journal/csur/author-guidelines)
      for the current length limit and whether anonymized review is required. If it is,
      add "anonymous" to the \documentclass options (and use "Anonymous author(s)" in Word).
  [ ] Optionally regenerate the CCS concepts with the ACM CCS tool (dl.acm.org/ccs) and
      paste the new CCSXML into main.tex.
  All placeholders appear as red [FILL: ...] in the PDF and yellow-highlighted [FILL: ...] in Word.

REFERENCE VERIFICATION
  Six quantum computer-vision references added in the review revision (Golyanik2020, Birdal2021,
  Benkner2021, Doan2022, Zaech2022, Meli2022) were checked against the CVF open-access records.
  All 149 original references were checked against publisher, DOI, arXiv, or the local PDFs.
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
