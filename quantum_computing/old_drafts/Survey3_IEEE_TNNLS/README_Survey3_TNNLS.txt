SURVEY 3 – IEEE TRANSACTIONS ON NEURAL NETWORKS AND LEARNING SYSTEMS (TNNLS) SUBMISSION PACKAGE
Adaptive Orchestration of Learning Modalities for Embodied Agents on Edge Hardware: A Survey
===============================================================================================

FILES
  Survey3_TNNLS_LaTeX_Overleaf.zip      Submission source: main.tex (IEEEtran, journal mode, two-column),
                                        refs.bib (180 entries, IEEE numbered style via IEEEtran.bst), figures/ (5 PNG, 300 dpi)
  Survey3_TNNLS_Manuscript.docx         Word version of the same manuscript (single-column review copy, line numbers)
  Survey3_TNNLS_Supplementary_routing_sim.py   Code for the illustrative routing simulation (supplementary material)
  Survey3_TNNLS_Cover_Letter.docx       Cover letter to the Editor-in-Chief

HOW TO PRODUCE THE SUBMISSION PDF
  1. overleaf.com -> New Project -> Upload Project -> Survey3_TNNLS_LaTeX_Overleaf.zip
  2. Compile main.tex with pdfLaTeX (IEEEtran.cls and IEEEtran.bst are built into Overleaf / TeX Live).
  Locally: pdflatex main; bibtex main; pdflatex main; pdflatex main

WHAT CHANGED FROM THE EARLIER SURVEY 3 DRAFT
  - Converted from a thesis-support review into a stand-alone journal survey: "thesis" framing removed;
    the four-modality architecture is now the survey's organizing framework; the LeKiwi section is now a
    "reference low-cost platform"; your own results/claims placeholders (perception stack, LeKiwi
    configuration, 50+ trials, ablation results) were removed – they belong in your thesis/experimental paper.
  - IEEE structure: Abstract (236 words, ≤250) and Index Terms; Sections I–XVI with A/B/C subsections;
    Appendix A (math) and Appendix B (simulation results); Acknowledgment; References; author biographies.
  - Added "Related Surveys and Contributions" and "Threats to Validity".
  - American spelling (IEEE style); numbered citations [1] in order of first appearance; all 180 cited.
  - Body ≈ 7,800 words + 6 tables + 5 figures; the test build gives ≈13 two-column pages of text plus
    ≈7 pages of references (≈20–21 pages in total).

BEFORE YOU SUBMIT
  [ ] Authors, IEEE membership grades, affiliations and e-mails (main.tex \author and \thanks).
  [ ] Section II: the search strings and hit counts per source (red [FILL]).
  [ ] Acknowledgment/funding; author biographies (required by IEEE Transactions).
  [ ] Cover letter: date, suggested reviewers, corresponding-author details.
  [ ] Check the current TNNLS Information for Authors (page limit and overlength page charges for
      regular/survey papers, and whether a separate "survey" category exists). I could not open the
      guidelines in this session; at ~20 pages the manuscript may exceed the free page allowance, in which
      case shorten Sections IV–XII or move Tables II–IV to supplementary material.
  [ ] Submit through ScholarOne Manuscripts (IEEE TNNLS); upload the PDF, source zip and the code file
      as "Supplementary material".

REFERENCES
  The 180 references come from the Survey 3 corpus that was checked against arXiv/publisher records
  when the survey was built (about twenty entries corrected then). No new online verification was
  possible in this session, so before submission please spot-check volume/pages for journal papers and
  add DOIs where IEEE Xplore shows them. Many conference papers are cited with their arXiv identifiers.
  Long author lists are shortened to "et al." (IEEE style allows this for more than six authors; for
  entries listing only the first three authors in the corpus, add the full author list if you prefer).
