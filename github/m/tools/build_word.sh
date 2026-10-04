#!/bin/sh
# Build the Word files of Survey 2 from the LaTeX source (run from github/m; needs pandoc >= 3).
#   Survey2_AIR_Manuscript.docx / Survey2_AIR_Online_Resource_1.docx : review copies, citations as plain text
#   Survey2_Word_for_Mendeley/*_cite_by_hand.docx : every citation in yellow, to re-insert with Mendeley Cite
set -e
SRC=Survey2_AIR_LaTeX_Overleaf
OUT=Survey2_Word_for_Mendeley

build() {  # build <tex> <output.docx> <lua filter> [caption prefix]
  TMP=$(mktemp -d)
  python3 tools/prep_tex_for_word.py $SRC/$1 $TMP/body.tex $TMP/meta.yaml $4
  sed -i '/^---$/d' $TMP/meta.yaml
  cp -r $SRC/figures $TMP/
  (cd $TMP && pandoc body.tex -f latex -t docx --number-sections \
    --metadata-file=meta.yaml --bibliography=$OLDPWD/$SRC/refs.bib --citeproc \
    --lua-filter=$OLDPWD/tools/$3 -o out.docx)
  cp $TMP/out.docx $2
  rm -rf $TMP
  echo "wrote $2"
}

mkdir -p $OUT
build main.tex Survey2_AIR_Manuscript.docx captions_only.lua
build supplement.tex Survey2_AIR_Online_Resource_1.docx captions_only.lua S
build main.tex $OUT/Survey2_Manuscript_cite_by_hand.docx highlight_citations.lua
build supplement.tex $OUT/Survey2_Online_Resource_1_cite_by_hand.docx highlight_citations.lua S
python3 tools/make_reference_lookup.py
