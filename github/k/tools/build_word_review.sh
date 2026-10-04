#!/bin/sh
# Clean Word versions for review (plain-text citations and reference list, no fields).
# Usage: sh tools/build_word_review.sh (from github/k)
set -e
SRC=Survey1_CSUR_LaTeX_Overleaf
OUT=Survey1_for_review
build() {
  TMP=$(mktemp -d)
  python3 tools/prep_tex_for_word.py $SRC/$1 $TMP/body.tex $TMP/meta.yaml $3
  sed -i '/^---$/d' $TMP/meta.yaml
  cp -r $SRC/figures $TMP/
  (cd $TMP && pandoc body.tex -f latex -t docx --number-sections \
    --metadata-file=meta.yaml --bibliography=$OLDPWD/$SRC/refs.bib --citeproc \
    --lua-filter=$OLDPWD/tools/captions_only.lua -o out.docx)
  cp $TMP/out.docx $OUT/$2; rm -rf $TMP; echo "wrote $OUT/$2"
}
mkdir -p $OUT
build main.tex Survey1_Manuscript_for_review.docx
build supplement.tex Survey1_Supplement_for_review.docx S
cp $SRC/main.pdf $OUT/Survey1_Manuscript.pdf
