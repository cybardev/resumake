#!/usr/bin/env bash

# variables
[ -z $1 ] && MARGIN=2 || MARGIN=$1
AUTHOR='$(head -n 1 resume.yml | cut -f 2- -d " " | tr " " "_")'
TEMPFILE="resources/_resume.md"
OUTFILE="static/assets/Resume_${AUTHOR}.pdf"

# create metadata file with resume info
echo "---" >${TEMPFILE}
cat resume.yml >>${TEMPFILE}
echo "---" >>${TEMPFILE}

# generate resume PDF
pandoc -s ${TEMPFILE} -t html \
  --template=resources/template.html --css=resources/template.css \
  --metadata=title:Resume --variable papersize=letter \
  --variable margin-top=$MARGIN --variable margin-right=0 \
  --variable margin-bottom=0 --variable margin-left=0 \
  --pdf-engine-opt=--enable-local-file-access \
  -o ${OUTFILE}

# clean up intermediate files
rm -f ${TEMPFILE}
