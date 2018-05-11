#!/bin/sh

if [ ! -f "SyceronBrut.xml" ]; then
    echo "Please download SyceronBrut.xml from http://data.assemblee-nationale.fr/travaux-parlementaires/debats"
    exit 1
fi;

ls data/debats-assemblee-nationale/*.txt
ls_ret=$?
if [ $ls_ret -eq 0 ]; then
    echo "Please cleanup data/debats-assemblee-nationale/*.txt"
    exit 1
fi;

python syceron.py SyceronBrut.xml data/debats-assemblee-nationale/
