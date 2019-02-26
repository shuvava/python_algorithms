#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
# was stollen from https://yurichev.com/blog/markov/

import re
from collections import Counter
from zipfile import ZipFile

FIRST = {}
SECOND = {}
THIRD = {}

def update_word_occurrence(word_dict, prefix, word):
    if prefix not in word_dict:
        word_dict[prefix] = Counter()
    word_dict[prefix].update([word])

with ZipFile('big.zip') as archive, archive.open('big.txt', 'r') as f:
    #https://stackoverflow.com/questions/25735644/python-regex-for-splitting-text-into-sentences-sentence-tokenizing
    SENTENCES = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', f.read().decode('utf-8'))
    for sentence in SENTENCES:
        words = re.findall(r'\w+', sentence.lower())
        if len(words) == 0:
            continue
        for i in range(len(words)):
            if i >= 1:
                update_word_occurrence(FIRST, words[i-1], words[i])
            if i >= 2:
                update_word_occurrence(SECOND, f'{words[i-2]} {words[i-1]}', words[i])
            if i >= 3:
                update_word_occurrence(THIRD, f'{words[i-3]} {words[i-2]} {words[i-1]}', words[i])

def print_stat(t):
    total=float(sum(t.values()))
    for pair in t.most_common(5):
        print('%s %d%%' % (pair[0], (float(pair[1])/total)*100))


if __name__ == '__main__':
    test='i can tell'
    #test='who did this'
    #test='she was a'
    #test='he was a'
    #test='i did not'
    #test='all that she'
    #test='have not been'
    #test='who wanted to'
    #test='he wanted to'
    #test='wanted to do'
    #test='it is just'
    #test='you will find'
    #test='you shall'
    #test='proved to be'
    test_words = test.split(' ')
    test_len = len(test_words)
    last_idx = test_len-1
    if test_len >= 3:
        tmp = test_words[last_idx-2]+' '+test_words[last_idx-1]+' '+test_words[last_idx]
        if tmp in THIRD:
            print('* third order. for sequence:', tmp)
            print_stat(THIRD[tmp])

    if test_len >= 2:
        tmp = test_words[last_idx-1]+' '+test_words[last_idx]
        if tmp in SECOND:
            print('* second order. for sequence:', tmp)
            print_stat(SECOND[tmp])

    if test_len >= 1:
        tmp = test_words[last_idx]
        if tmp in FIRST:
            print('* first order. for word:', tmp)
            print_stat(FIRST[tmp])
    print('')
