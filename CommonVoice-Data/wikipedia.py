import urllib.request
import urllib.parse
import json
import re
import random
import os
from collections import Counter

#WORDCOUNT_GOAL = 10000000
WORDCOUNT_GOAL = 150000000
WORD_REGEX = re.compile("[^\w\d\'\-]+")

cache_listing = os.listdir("cache")
random.shuffle(cache_listing)

pagecount = 0
pages = []
def getPage():
    global pages
    if len(pages) < 1:
        response = json.loads(urllib.request.urlopen("https://fr.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&grnlimit=1000").read())
        pages += [page["title"] for id,page in response["query"]["pages"].items()]

    return pages.pop()

def getPageText(title):
    print(title)
    response = json.loads(urllib.request.urlopen("https://fr.wikipedia.org/w/api.php?action=query&titles=" + urllib.parse.quote(title) + "&prop=extracts&format=json&explaintext=1&exsectionformat=plain&redirects=1").read())
    page_id = list(response["query"]["pages"].values())[0]["pageid"]
    text = list(response["query"]["pages"].values())[0]["extract"].lower()

    with open("cache/{}.txt".format(page_id), "w") as cache:
        cache.write(text)

    return text

def splitIntoWords(text):
    return WORD_REGEX.split(text)

def getWordsInRandomArticle():
    global pagecount

    pagecount += 1
    if len(cache_listing) > 0:
        cache_file = cache_listing.pop()
        print(cache_file)
        with open("cache/" + cache_file, "r") as f:
            return splitIntoWords(f.read())
    else:
        return splitIntoWords(getPageText(getPage()))


enable = []
with open("02_enable.txt", "r") as enable_file:
    enable = enable_file.read().splitlines()
# These words are used abnormally often on Wikipedia, so exclude them
blacklist = ["externes", "liens", "références", "bibliographie", "portail"]
enable = set([item for item in enable if item not in blacklist])

words = []

while len(words) < WORDCOUNT_GOAL:
    print('WORDCOUNT: {}'.format(len(words)))
    words += getWordsInRandomArticle()

frequencies = Counter(words)
by_frequency = frequencies.most_common()

csv = open("01_frequencies_wikipedia.csv", "w")

wordcount_total = len(words)
wordcount = 0
for word,freq in by_frequency:
    if word in enable:
#        print("{:10d} {:.5} {}".format(freq, freq / wordcount_total, word))
        csv.write("{},{:.10f},{}\n".format(freq, freq / wordcount_total, word))
        wordcount += 1
csv.close()

print("WORDS: {} (UNIQUE: {}, IN DICTIONARY: {})".format(wordcount_total, len(by_frequency), wordcount))
print("PAGES: {}".format(pagecount))
