#!/usr/bin/env bash

echo "---" >resume.md
cat resume.yml >>resume.md
echo "---" >>resume.md

AUTHOR=$(head -n 1 resume.yml | cut -f 2- -d " " | tr " " "_")

pandoc -s resume.md -t html \
  --template=resources/template.html --css=resources/template.css \
  --metadata=title:Resume --variable papersize=letter \
  --variable margin-top=0 --variable margin-right=0 \
  --variable margin-bottom=0 --variable margin-left=0 \
  --pdf-engine-opt=--enable-local-file-access \
  -o static/assets/Resume_${AUTHOR}.pdf

rm -f resume.md
