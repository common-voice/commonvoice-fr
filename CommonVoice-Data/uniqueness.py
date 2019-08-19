#!/usr/bin/env python3

import os
import re
from collections import Counter

WORD_REGEX = re.compile("[^\w\d\'\-]+")
def splitIntoWords(text):
    return WORD_REGEX.split(text)

enable = []
with open("02_enable.txt", "r") as enable_file:
    enable = set(enable_file.read().splitlines())

words = []

for (dirpath, dirnames, filenames) in os.walk("data/"):
    for filename in filenames:
        print(dirpath + "/" + filename)
        with open(dirpath + "/" + filename, "r") as f:
            words += splitIntoWords(f.read().lower())


frequencies = Counter(words)
by_frequency = frequencies.most_common()

csv = open("05_frequencies_common_voice.csv", "w")

wordcount_total = len(words)
wordcount = 0
for word,freq in by_frequency:
    if word.upper() in enable:
#        print("{:10d} {:.5} {}".format(freq, freq / wordcount_total, word))
        csv.write("{},{:.10f},{}\n".format(freq, freq / wordcount_total, word))
        wordcount += 1
csv.close()

print("WORDS: {} (UNIQUE: {}, IN DICTIONARY: {})".format(wordcount_total, len(by_frequency), wordcount))
