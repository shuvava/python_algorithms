#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
# was stollen from http://norvig.com/spell-correct.html
# source code from https://github.com/norvig/pytudes
# https://yurichev.com/blog/fuzzy_string/
"""
The Levenshtein distance is a string metric for measuring difference between two
sequences. Informally, the Levenshtein distance between two words is
the minimum number of single-character edits
(i.e. insertions, deletions or substitutions)
required to change one word into the other.
"""

################ Spelling Corrector

import re
from collections import Counter
from zipfile import ZipFile

words = lambda text: re.findall(r'\w+', text.lower())

with ZipFile('big.zip') as archive, archive.open('big.txt', 'r') as f:
    WORDS = Counter(words(f.read().decode('utf-8')))

COUNT_OF_WORDS = sum(WORDS.values())


def P(word, N=COUNT_OF_WORDS):
    """Probability of `word`."""
    return WORDS[word] / N


def correction(word):
    """Most probable spelling correction for word."""
    return max(candidates(word), key=P)


def candidates(word):
    """Generate possible spelling corrections for word."""
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS)


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


## To rewrite
################ Test Code

def unit_tests():
    assert correction('speling') == 'spelling'  # insert
    assert correction('korrectud') == 'corrected'  # replace 2
    assert correction('bycycle') == 'bicycle'  # replace
    assert correction('inconvient') == 'inconvenient'  # insert 2
    assert correction('arrainged') == 'arranged'  # delete
    assert correction('peotry') == 'poetry'  # transpose
    assert correction('peotryy') == 'poetry'  # transpose + delete
    assert correction('word') == 'word'  # known
    assert correction('quintessential') == 'quintessential'  # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
        Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))
    assert len(WORDS) == 32198
    assert COUNT_OF_WORDS == 1115585
    assert WORDS.most_common(10) == [
        ('the', 79809),
        ('of', 40024),
        ('and', 38312),
        ('to', 28765),
        ('in', 22023),
        ('a', 21124),
        ('that', 12512),
        ('he', 12401),
        ('was', 11410),
        ('it', 10681)]
    assert WORDS['the'] == 79809
    assert P('quintessential') == 0
    assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'


if __name__ == '__main__':
    print(unit_tests())
