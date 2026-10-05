#!/bin/sh
# Build the Word files of Survey 3 from the LaTeX source (run from github/s; needs pandoc >= 3).
#   Survey3_TNNLS_Manuscript.docx / Survey3_TNNLS_Supplementary.docx : review copies, citations as IEEE numbers
#   Survey3_Word_for_Mendeley/*_cite_by_hand.docx : every citation in yellow, to re-insert with Mendeley Cite
set -e
SRC=Survey3_TNNLS_LaTeX_Overleaf
OUT=Survey3_Word_for_Mendeley

build() {  # build <tex> <output.docx> <lua filter> [caption prefix]
  TMP=$(mktemp -d)
  python3 tools/prep_tex_for_word.py $SRC/$1 $TMP/body.tex $TMP/meta.yaml $4
  sed -i '/^---$/d' $TMP/meta.yaml
  cp -r $SRC/figures $TMP/
  (cd $TMP && pandoc body.tex -f latex -t docx --number-sections \
    --metadata-file=meta.yaml --bibliography=$OLDPWD/$SRC/refs.bib --citeproc --csl=$OLDPWD/tools/ieee.csl \
    --lua-filter=$OLDPWD/tools/$3 -o out.docx)
  cp $TMP/out.docx $2
  rm -rf $TMP
  echo "wrote $2"
}

mkdir -p $OUT
build main.tex Survey3_TNNLS_Manuscript.docx captions_only.lua
build supplement.tex Survey3_TNNLS_Supplementary.docx captions_only.lua S
build main.tex $OUT/Survey3_Manuscript_cite_by_hand.docx highlight_citations.lua
build supplement.tex $OUT/Survey3_Supplementary_cite_by_hand.docx highlight_citations.lua S
python3 tools/make_reference_lookup.py
