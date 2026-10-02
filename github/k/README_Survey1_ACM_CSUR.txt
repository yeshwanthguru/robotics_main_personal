SURVEY 1 – ACM COMPUTING SURVEYS (CSUR) SUBMISSION PACKAGE
Quantum Technologies for Autonomous Robotics: A Systematic Survey of Methods, Evidence, and Deployment Constraints
(retitled from "Quantum Computing for ..."; title and authors are updated in all .docx files)
=====================================================================================================

FILES
  Survey1_CSUR_LaTeX_Overleaf.zip       Official submission source (ACM acmart, acmsmall format)
      main.tex                          Manuscript (\documentclass[acmsmall,screen,review]{acmart})
      supplement.tex                    Online supplementary material
      refs.bib                          185 verified BibTeX entries (full author names, DOIs)
      figures/                          Figures 1-10 of the paper + PRISMA flow diagram (PNG); fig7_years.png
                                        is generated from extraction_table.csv; fig8-fig11 are redrawn
                                        "adapted from" schematics of methods in the cited studies (QUBO
                                        fleet pipeline, Grover search, variational policy, order effect),
                                        drawn in the paper's own style and credited in each caption
  Survey1_ACM_CSUR_Manuscript.docx      Word version generated from main.tex (tools/build_word.sh), with every
                                        citation as a Mendeley citation field and the reference list as a
                                        Mendeley bibliography field (see "WORD + MENDELEY" below)
  Survey1_ACM_CSUR_Supplementary_Material.docx   Word version of the supplement, generated from supplement.tex
                                        with Mendeley citation fields (tools/build_word.sh)
  extraction_table.csv                  Data-extraction table for the 72 primary studies (supplementary data),
                                        including the quantum-execution tag of each study
  Survey1_CSUR_Cover_Letter.docx        Cover letter to the Editor-in-Chief

  Survey1_method_workbook/              Search/screening workbook and targeted_search_record.md (provenance of the 12 targeted-search studies)
  Survey1_data_package/                 Archive-ready dataset: extraction table, codebook, search
                                        strings and README for a Zenodo deposit (DOI goes in Data Availability)

  tools/make_figures.py                 Regenerates the data-driven figures (timeline, yearly counts, evidence) and the PRISMA diagram
  tools/make_schematics.py              Redraws the schematic figures (taxonomy, architecture, latency, fig8-fig11)

WORD + MENDELEY
  1. In Mendeley Reference Manager, import Survey1_CSUR_LaTeX_Overleaf/refs.bib
     (File > Import > BibTeX) so the library holds the same 185 references.
  2. Open Survey1_ACM_CSUR_Manuscript.docx in Word with the Mendeley Cite add-in. The
     citations are Mendeley Desktop-style fields carrying full reference data; if Mendeley
     Cite asks to convert legacy citations, accept. Choose a citation style (e.g.
     "Association for Computing Machinery") and refresh to restyle citations and references.
  3. Narrative citations (\citet, e.g. "Clark et al. (2019) asked ...") are rendered in
     narrative form now, but a Mendeley refresh turns them into parenthetical citations;
     re-type the author names in front of those citations if needed.
  4. To regenerate both Word files after editing main.tex or supplement.tex: run
     tools/build_word.sh from this folder (needs pandoc >= 3).
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
  [ ] *** PAGE LIMIT ***: CSUR author guidelines: long surveys "must not exceed 35 pages, including
      references" (dl.acm.org/journal/csur/author-guidelines). main.pdf is 47 pages (text and tables
      end on p. 37, references pp. 38-47). Either cut about 12 pages or move material to an
      electronic supplement and mark which pages form the 35 published pages.
  [x] Authors: Yeshwanth Guru (g_yeshwanth@ch.students.amrita.edu) and Dev Kunwar Singh Chauhan
      (c_devsingh@ch.amrita.edu), Amrita Vishwa Vidyapeetham, Chennai, India.
  [~] ORCIDs: Yeshwanth added (0009-0007-6353-4033). Still needed: Dev's ORCID and both departments.
  [ ] Cover letter lists Yeshwanth Guru as corresponding author - change if needed.
  [ ] Generative-AI use is no longer disclosed in the manuscript (acknowledgments removed).
      ACM policy requires disclosure: declare it in the submission system or cover letter.
  [x] PRISMA reporting (Oct 2026): the per-stage record counts were never logged, so the paper
      now says so openly (Section 3.4, Section 3.7 "Selection and grading", Table S2, Figure S1)
      instead of leaving [n] blanks. Search window: 1982 to October 2026 (latest study August 2026).
      Screening and extraction by the first author; evidence levels and appraisal reviewed by the
      second author (Dev, supervisor), disagreements resolved by discussion (confirmed Oct 2026).
      Protocol "not registered". Inter-rater kappa still unmeasured: the blind Grading_Check below
      would add it.
  [ ] OPTIONAL UPGRADE (strongly recommended before submission): re-run the searches in one day
      and log them in Survey1_method_workbook/Survey1_method_workbook.xlsx. With real counts and a
      second grader (kappa), the paper can report a full PRISMA flow - send me the workbook and I
      will put the numbers back in.
  [ ] Quality appraisal (supplement Table S5 and Survey1_data_package/quality_appraisal.csv):
      Q4 and Q6 judged from the full texts for 56 of the 59 studies; Q1, Q2, Q3, Q5 and Q7 were
      drafted from the extraction table - check them. Section 3.5 quotes 12 / 19 / 6 of 59
      (Q2, Q3) and 14 of 56 (Q6): update if any judgment changes.
  [ ] Full texts still missing: Yan2024 (review), Windmann2023, Mannone2023, Mannone2025.
      The last three have red Q4/Q6 cells in Table S5. See Survey1_fulltexts/index.csv for the
      40 cited references that are also still missing.
  [ ] Section 11.6 resource estimate: the assumptions (10 us per Toffoli, 10 ns per cell,
      1,000 Toffolis per qRAM call) are ours and stated in Table 6; check you are comfortable
      defending them, or ask a quantum-compilation colleague to read the section.
  [ ] Table 5 (studies run on a QPU): confirm the device, instance and baseline cells against
      the full texts, especially Windmann2023, Gerlach2025 and Antero2025.
  [x] Update the title in Survey1_ACM_CSUR_Manuscript.docx and the cover letter.
  [x] Competing interests: "The authors declare no competing interests" (checklist item 26, cover letter).
  [ ] Funding statement (checklist item 25, cover letter). The
      acknowledgments section was removed at the authors' request.
  [ ] Cover letter: date and suggested reviewers.
  [ ] Deposit Survey1_data_package on Zenodo and paste the DOI into Data Availability.
  [x] Published versions checked (Oct 2026): Wang2021 now carries a note pointing to J. Navigation 76(1), 2023;
      Innan2025 is still arXiv-only.
  [ ] Check the live CSUR author-guidelines page (dl.acm.org/journal/csur/author-guidelines)
      for the current length limit and whether anonymized review is required. If it is,
      add "anonymous" to the \documentclass options (and use "Anonymous author(s)" in Word).
  [ ] Optionally regenerate the CCS concepts with the ACM CCS tool (dl.acm.org/ccs) and
      paste the new CCSXML into main.tex.
  Placeholders for facts only the authors can supply appear in red brackets, e.g. [n], in the PDF.

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
