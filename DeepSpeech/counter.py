#!/usr/bin/env python3

import sys

from collections import Counter

def main(input_file, output_file, top_count=100000):
    counter = Counter()
    print('Reading {}'.format(input_file))
    fcontent = None
    with open(input_file, 'r', encoding='utf-8') as input:
        fcontent = input.readlines()
    all_file = len(fcontent)
    print('Ingesting {}: {}'.format(input_file, all_file))
    current = 0
    for line in fcontent:
        print('Feeding {}: {}/{} ({:.2f}%)'.format(input_file, current, all_file, (current / all_file) * 100), end='\r')
        counter.update(line.split())
        current += 1
    print('Counting {}'.format(input_file))
    vocab_str = '\n'.join(word for word, count in counter.most_common(top_count))
    print('Writing {}'.format(output_file))
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(vocab_str)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
