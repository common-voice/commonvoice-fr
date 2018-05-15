#!/bin/sh

ls data/gutenberg/*.txt
ls_ret=$?
if [ $ls_ret -eq 0 ]; then
	python project-gutenberg.py $(find data/gutenberg/*.txt | sed -e 's/^data\/gutenberg\///g' -e 's/\.txt//g' | xargs echo "--bookid") -- data/gutenberg/
else
	python project-gutenberg.py --numbooks 1000 --random -- data/gutenberg/
fi;
