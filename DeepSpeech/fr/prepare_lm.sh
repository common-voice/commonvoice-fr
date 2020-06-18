#!/bin/bash

set -xe

if [ ! -f "wiki_fr_lower.txt" ]; then
	curl -sSL https://github.com/Common-Voice/commonvoice-fr/releases/download/lm-0.1/wiki.txt.xz | pixz -d | tr '[:upper:]' '[:lower:]' > wiki_fr_lower.txt
fi;

if [ ! -f "debats-assemblee-nationale.txt" ]; then
	curl -sSL https://github.com/Common-Voice/commonvoice-fr/releases/download/lm-0.1/debats-assemblee-nationale.txt.xz | pixz -d | tr '[:upper:]' '[:lower:]' > debats-assemblee-nationale.txt
fi;

if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	mv wiki_fr_lower.txt wiki_fr_lower_accents.txt
	# Locally force LANG= to make iconv happy and avoid errors like:
	# iconv: illegal input sequence at position 4468
	# Also required locales and locales-all to be installed
	head -n 5 wiki_fr_lower_accents.txt
	iconv -f UTF-8 -t ASCII//TRANSLIT//IGNORE < wiki_fr_lower_accents.txt > wiki_fr_lower.txt
	head -n 5 wiki_fr_lower.txt
	> wiki_fr_lower_accents.txt
fi;

cat wiki_fr_lower.txt debats-assemblee-nationale.txt > sources_lm.txt
