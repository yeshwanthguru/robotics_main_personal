#!/bin/sh
# Build Word versions with yellow-highlighted plain-text citations (no fields), for
# re-inserting every citation by hand with Mendeley Cite. Usage: tools/build_word_highlight.sh (from github/k)
set -e
SRC=Survey1_CSUR_LaTeX_Overleaf
OUT=Survey1_Word_for_Mendeley

build() {
  TMP=$(mktemp -d)
  python3 tools/prep_tex_for_word.py $SRC/$1 $TMP/body.tex $TMP/meta.yaml $3
  sed -i '/^---$/d' $TMP/meta.yaml
  cp -r $SRC/figures $TMP/
  (cd $TMP && pandoc body.tex -f latex -t docx --number-sections \
    --metadata-file=meta.yaml --bibliography=$OLDPWD/$SRC/refs.bib --citeproc \
    --lua-filter=$OLDPWD/tools/highlight_citations.lua -o out.docx)
  cp $TMP/out.docx $OUT/$2
  rm -rf $TMP
  echo "wrote $OUT/$2"
}

mkdir -p $OUT
build main.tex Survey1_Manuscript_cite_by_hand.docx
build supplement.tex Survey1_Supplement_cite_by_hand.docx S
