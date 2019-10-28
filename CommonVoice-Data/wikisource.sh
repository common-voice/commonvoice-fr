#!/bin/sh

for f in $(find  "./data/wikisource/txt/" -type f -name "*.txt"  | sed 's/ /%/g');
do
    txtfile=$(echo "$f" | sed 's/%/ /g')
    epubfile=$(echo "$f" | sed -e 's/%/ /g' -e 's/\.txt$/.epub/g' -e 's/\/txt\//\/epub\//g')
    epubdir=$(dirname "${epubfile}")

    if [ ! -f "${epubfile}" ]; then
        http_root="https://tools.wmflabs.org/wsexport/tool/book.php?lang=fr&format=epub&page="
	epubfilename=$(basename "${epubfile}")
	epubhttpname=$(basename "${epubfile}" ".epub")
	http_epub="${http_root}${epubhttpname}"

        mkdir -p "${epubdir}" || true
        wget -O "${epubdir}/${epubfilename}" "${http_epub}"
    fi;
done;

for d in $(find "./data/wikisource/epub/" -mindepth 1 -type d);
do
    epubdir="$d"
    txtdir="$(echo "$d" | sed 's/\/epub\//\/txt\//g')"
    python wikisource.py "${epubdir}" "${txtdir}"
done;
