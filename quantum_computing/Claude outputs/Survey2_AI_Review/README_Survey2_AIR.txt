SURVEY 2 – ARTIFICIAL INTELLIGENCE REVIEW (SPRINGER NATURE) SUBMISSION PACKAGE
Quantum-like cognition and decision-making for autonomous agents: a survey from robotics to machine learning
=================================================================================================

FILES
  Survey2_AIR_LaTeX_Overleaf.zip          Submission source: main.tex (Springer Nature template, sn-basic
                                          author-year references), refs.bib (205 entries), figures/ (9 PNG, 300 dpi)
  Survey2_AIR_Manuscript.docx             Word version of the same manuscript (A4, 1.5 spacing, line numbers)
  Survey2_AIR_Online_Resource_1.pdf/.docx Supplement: Table S1 (74 application studies classified), Table S2 (glossary)
  Survey2_AIR_Online_Resource_2_code.py   Python code reproducing every worked example and the RL experiment
  Survey2_AIR_Online_Resource_3_classification.csv   Table S1 as CSV
  Survey2_AIR_Cover_Letter.docx           Cover letter to the Editor-in-Chief

HOW TO PRODUCE THE SUBMISSION PDF
  The Springer Nature class file (sn-jnl.cls) is not part of standard TeX distributions, so:
  1. On Overleaf, open the template gallery and start a project from
     "Springer Nature LaTeX Template" (it contains sn-jnl.cls and the sn-*.bst files).
  2. Delete its sample .tex/.bib files, then upload the contents of Survey2_AIR_LaTeX_Overleaf.zip
     (main.tex, refs.bib and the figures folder) into that project.
  3. Set main.tex as the main document and compile (pdfLaTeX).
  Alternatively, download the template zip from Springer Nature's LaTeX author support page and put
  sn-jnl.cls and sn-basic.bst next to main.tex.
  Springer journals also accept Word: Survey2_AIR_Manuscript.docx carries the identical text.

WHAT WAS CHANGED FROM THE EARLIER SURVEY 2 DRAFT
  - Restructured into a journal review: Introduction (with related-survey table and contributions),
    Review methodology (+ threats to validity), History, Mathematical foundations, Core phenomena and
    evidence, Framework, seven application sections, Synthesis and comparison with classical models,
    Limitations, Ethics, Biological grounding, Research agenda, Conclusion, Declarations, Appendices A–B.
  - Removed "Part"/"Tier" labels, references to "Survey 1", and lab-specific placeholders.
  - Abstract cut to 214 words (Springer limit 150–250); 6 keywords (Springer 4–6).
  - Mandatory Springer "Declarations" section added (funding, competing interests, ethics, consent,
    data, materials, code, author contributions).
  - The long evidence table moved to Online Resource 1; code moved to Online Resource 2.
  - Author-year citations; all 205 references cited in the text. Body ≈ 14,400 words, 9 figures, 9 tables.

BEFORE YOU SUBMIT (only you can supply these; red [FILL: …] in the PDF, yellow in Word)
  [ ] Authors, affiliations, corresponding e-mail, ORCIDs.
  [ ] Section 2: date of the final search and database-level hit counts.
  [ ] Declarations: funding, competing interests, author contributions (CRediT); repository URL and
      licence for the code; acknowledgements (or delete the heading).
  [ ] Cover letter: date, suggested reviewers, corresponding-author details.
  [ ] Check the live submission guidelines (link.springer.com/journal/10462/submission-guidelines) –
      I could not open that page (rate-limited), so length, open-access/APC terms and any review-article
      requirements should be confirmed there.
  [ ] About 92 of the 205 works were classified from abstracts in the earlier draft; read the full text of
      any study you discuss in detail (see the earlier write-ups file, which marks each one).
  [ ] The RL experiment (Section 10.5, Appendix B) is illustrative and run for this survey; rerun it with
      Online Resource 2 before submission.

REFERENCE VERIFICATION
  All 205 references were checked; 147 were confirmed online or against your PDFs. Corrections include:
  Cerezo2021 DOI (…21728-w), Uprety2021 → 2020 (ACM Comput. Surv. 53(5):98), Sinha2023 → Quantum Mach.
  Intell. 7:19 (2025), Khrennikov2023b → R. Soc. Open Sci. 11:231953 (2024), Ozawa2021, Fuyama2025,
  Busemeyer2025, Yukalov2016, Khrennikov2025c, Henderson2018, Aerts2011c now cite the published versions;
  Huang2025c DOI completed from your PDF (10.1109/QCE65121.2025.10486).
  Could not be confirmed online in this session (session web-search limit reached) – please spot-check:
    Gao2025 (Eng. Appl. Artif. Intell. 157:111368) – NOT FOUND in any index; verify the DOI or drop it.
    Epping2023 – the journal version could not be found; a CogSci 2022 paper with the same title exists.
    Details (volume/pages/DOI) taken from the earlier verified list for: Aerts2011b, Aerts2017b,
    Trueblood2017b, Kellen2018, Moreira2014, Moreira2017a, Meghdadi2022, Widdows2003, Lo2025, Dong2012,
    Jerbi2021, Hohenfeld2024, Lukac2007, Hangl2016, Lanza2021, Yan2021c, Chella2022, Song2022, Widdows2023,
    Mannone2024, Daglarli2025, DeCarolis2025, Chella2026, Eisert1999, MartinezMartinez2016, Yukalov2018,
    Ried2019, Khoshnoud2020, LopezIncera2020, Lawless2020, Waddup2021, Yukalov2023, Essalmi2025,
    Lawless2025, Dreossi2019, Humr2023, Humr2025, Humr2026, Bergholm2018, Broughton2020, Khrennikov2025a,
    Khrennikov2022, Chen2024, Yan2024, Huang2025b, Maksymov2025, Khrennikov2026 and standard textbooks.
