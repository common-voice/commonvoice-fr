#!/bin/sh

if [ ! -f "SyceronBrut.xml" ]; then
    echo "Please download SyceronBrut.xml from http://data.assemblee-nationale.fr/travaux-parlementaires/debats"
    exit 1
fi;

ls "data/debats-assemblee-nationale/*.txt" 2>/dev/null 1>/dev/null
if [ $? -gt 0 ]; then
    echo "Please cleanup data/debats-assemblee-nationale/*.txt"
    exit 1
fi;

python syceron.py SyceronBrut.xml data/debats-assemblee-nationale/
