#!/usr/bin/env python3

import os
import re

from operator import itemgetter
from collections import Counter

dimensions = []

WORD_REGEX = re.compile("[^\w\d\'\-]+")
def splitIntoWords(text):
    return WORD_REGEX.split(text)

for (dirpath, dirnames, filenames) in os.walk("data"):
    for filename in filenames:
        print(dirpath + "/" + filename)
        with open(dirpath + "/" + filename, "r") as f:
            for line in f.readlines():
                words = len(list(filter(lambda x: len(x) > 0, splitIntoWords(line))))
                dimensions += [ words ]

frequencies = Counter(dimensions)
by_frequency = frequencies.most_common()

total = 0
csv = open("sentences-lengths.csv", "w")
for dim, freq in sorted(frequencies.items(), key=itemgetter(0)):
  total += freq
  print("DIM: {} FREQ: {} TOTAL: {}".format(dim, freq, total))
  csv.write("{},{:.10f}\n".format(dim, freq))
csv.close()
