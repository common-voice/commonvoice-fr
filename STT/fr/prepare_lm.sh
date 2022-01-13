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

if [ ! -f "mls_lm_french.txt" ]: then

	if [ ! -d "/mnt/extracted/data/MLS/mls_lm_french" ]; then
		./import_mls.sh
	fi;
	
	cat /mnt/extracted/data/MLS/mls_lm_french/data.txt | tr '[:upper:]' '[:lower:]' > mls_lm_french.txt
fi;

# Remove special-char <s> that will make KenLM tools choke:
# kenlm/lm/builder/corpus_count.cc:179 in void lm::builder::{anonymous}::ComplainDisallowed(StringPiece, lm::WarningAction&) threw FormatLoadException.
# Special word <s> is not allowed in the corpus.  I plan to support models containing <unk> in the future.  Pass --skip_symbols to convert these symbols to whitespace.
if [ ! -f "sources_lm.txt" ]; then
	cat wiki_fr_lower.txt debats-assemblee-nationale.txt mls_lm_french.txt | sed -e 's/<s>/ /g' > sources_lm.txt
fi;
