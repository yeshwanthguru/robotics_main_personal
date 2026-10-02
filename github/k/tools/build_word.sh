#!/bin/sh
# Build the Word manuscript and supplement with Mendeley citation fields from the LaTeX source.
# Usage: tools/build_word.sh   (run from github/k)
set -e
SRC=Survey1_CSUR_LaTeX_Overleaf

# build one document: build <tex> <output.docx> [caption prefix]
build() {
  TMP=$(mktemp -d)
  python3 tools/prep_tex_for_word.py $SRC/$1 $TMP/body.tex $TMP/meta.yaml $3
  sed -i '/^---$/d' $TMP/meta.yaml
  pandoc $SRC/refs.bib -t csljson -o $TMP/items.json
  cp -r $SRC/figures $TMP/
  (cd $TMP && pandoc body.tex -f latex -t docx --number-sections \
    --metadata-file=meta.yaml -M csl-items-file=$TMP/items.json \
    --bibliography=$OLDPWD/$SRC/refs.bib --citeproc \
    --lua-filter=$OLDPWD/tools/mendeley_fields.lua -o out.docx)
  cp $TMP/out.docx $2
  rm -rf $TMP
  echo "wrote $2"
}

build main.tex Survey1_ACM_CSUR_Manuscript.docx
build supplement.tex Survey1_ACM_CSUR_Supplementary_Material.docx S
