#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random
import re
from collections import Counter
from zipfile import ZipFile

FIRST = {}
SECOND = {}


def update_word_occurrence(word_dict, prefix, word):
    if prefix not in word_dict:
        word_dict[prefix] = Counter()
    word_dict[prefix].update([word])


with ZipFile('big.zip') as archive, archive.open('big.txt', 'r') as f:
    # https://stackoverflow.com/questions/25735644/python-regex-for-splitting-text-into-sentences-sentence-tokenizing
    SENTENCES = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', f.read().decode('utf-8'))
    for sentence in SENTENCES:
        words = re.findall(r'\w+', sentence.lower())
        if len(words) == 0:
            continue
        for i in range(len(words)):
            if i >= 1:
                update_word_occurrence(FIRST, words[i - 1], words[i])
            if i >= 2:
                update_word_occurrence(SECOND, f'{words[i - 2]} {words[i - 1]}', words[i])


def gen_random_from_tbl(t):
    # https://docs.python.org/3/library/random.html#random.choice
    return random.choices(list(t.keys()), weights=list(t.values()))[0]


if __name__ == '__main__':
    text = ["it", "is"]
    text_len = len(text)
    # generate at most 200 words:
    for i in range(200):
        last_idx = text_len - 1
        tmp = text[last_idx - 1] + " " + text[last_idx]
        if tmp in SECOND:
            new_word = gen_random_from_tbl(SECOND[tmp])
        else:
            # fall-back to 1st order
            tmp2 = text[last_idx]
            if tmp2 not in FIRST:
                # dead-end
                break
            new_word = gen_random_from_tbl(FIRST[tmp2])
        text.append(new_word)
        text_len = text_len + 1
    print(' '.join(text))
