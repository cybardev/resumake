#!/usr/bin/env bash

# variables
[ -z $INDIR ] && INDIR="."
[ -z $OUTDIR ] && OUTDIR="."
[ -z $TMPDIR ] && TMPDIR="."
[ -z $1 ] && INFILE="${INDIR}/resume.yml" || INFILE=${INDIR}/$1
[ -z $2 ] && MARGIN=2 || MARGIN=$2
AUTHOR="$(head -n 1 ${INFILE} | cut -f 2- -d ' ' | tr ' ' '_')"
TEMPFILE="${TMPDIR}/_resume.md"
OUTFILE="${OUTDIR}/Resume_${AUTHOR}.pdf"

# create metadata file with resume info
echo "---" >${TEMPFILE}
cat ${INFILE} >>${TEMPFILE}
echo "---" >>${TEMPFILE}

# generate resume PDF
pandoc -s "${TEMPFILE}" -t html \
  --template=resources/template.html \
  --metadata=title:Resume --variable papersize=letter \
  --variable margin-top=${MARGIN} --variable margin-right=0 \
  --variable margin-bottom=0 --variable margin-left=0 \
  --pdf-engine-opt=--enable-local-file-access \
  -o "${OUTFILE}"
