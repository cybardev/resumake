#!/usr/bin/env bash

echo "---" >resume.md
cat resume/cybardev.yml >>resume.md
echo "---" >>resume.md

pandoc -s resume.md \
  -t html --template=template/resume.html \
  --metadata=title:Resume --variable papersize=letter \
  --variable margin-top=0 --variable margin-right=0 \
  --variable margin-bottom=0 --variable margin-left=0 \
  --pdf-engine-opt=--enable-local-file-access \
  -o resume.pdf

rm -f resume.md
