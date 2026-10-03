# Word files for re-citing by hand in Mendeley Cite

- Survey1_Manuscript_cite_by_hand.docx: 404 citations, each in yellow highlight (plain text, no fields).
- Survey1_Supplement_cite_by_hand.docx: 211 citations, same.
- Survey1_reference_lookup.docx: all 185 references (author, year, title, DOI), to find each one in Mendeley.

How to use: import ../Survey1_CSUR_LaTeX_Overleaf/refs.bib into a Mendeley collection; in Word,
select a yellow citation, insert the same reference(s) from the Mendeley Cite panel, delete the
yellow text. For narrative citations ("Gerlach et al. (2025)") only the year part is yellow: insert
the citation and, in Mendeley Cite, edit it to hide the author. At the end, replace the yellow
"Insert the Mendeley bibliography here" line with Mendeley Cite > Insert Bibliography.

Rebuild from the LaTeX with: sh tools/build_word_highlight.sh (run from github/k).
