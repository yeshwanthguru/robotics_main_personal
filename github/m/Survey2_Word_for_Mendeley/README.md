# Word files for re-citing by hand in Mendeley Cite (Survey 2)

- `Survey2_Manuscript_cite_by_hand.docx`: 403 citations, each in yellow highlight (plain text, no fields).
- `Survey2_Online_Resource_1_cite_by_hand.docx`: 213 citations, same.
- `Survey2_reference_lookup.docx`: all 212 references (key, authors, year, title, DOI or arXiv id), to find each one in Mendeley.

How to use (same as Survey 1): import `../Survey2_AIR_LaTeX_Overleaf/refs.bib` into a **new** Mendeley
collection (File > Import > BibTeX); in Word, select a yellow citation, insert the same reference(s)
from the Mendeley Cite panel, delete the yellow text. For narrative citations ("Song et al. (2022)")
only the year part is yellow: insert the citation and, in Mendeley Cite, edit it to hide the author.
At the end, replace the yellow "Insert the Mendeley bibliography here" line with Mendeley Cite >
Insert Bibliography. Choose a Springer author-year style (e.g. "Springer - Basic (author-date)").

Rebuild from the LaTeX with: `sh tools/build_word.sh` (run from github/m).
