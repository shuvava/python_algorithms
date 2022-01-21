#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Longest Common Subsequence:
Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
So a string of length n has 2^n-1 different possible subsequences.

It is a classic computer science problem, the basis of diff
(a file comparison program that outputs the differences between two files),
and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

link https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

DP programming with using bottom-up principal
complicity O(n*m) where n and m length of strings
"""


def lcs(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0] * (n + 1), [0] * (n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                if cur[j - 1] > prev[j]:
                    cur[j] = cur[j - 1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]


def lcs_recursive(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for _ in range(m + 1)]

    '''Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]'''
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m or j == n:
                L[i][j] = 0
            elif s1[i] == s2[j]:
                L[i][j] = L[i + 1][j + 1] + 1
            else:
                L[i][j] = max(L[i + 1][j], L[i][j + 1])

    # L[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    return L[0][0]


def lcs_iterative(s1, s2, i1, i2):
    if i1 == 0 or i2 == 0:
        return 0
    if s1[i1 - 1] == s2[i2 - 1]:
        return 1 + lcs_iterative(s1, s2, i1 - 1, i2 - 1)
    return max(lcs_iterative(s1, s2, i1, i2 - 1), lcs_iterative(s1, s2, i1 - 1, i2))


def lcs_recursive2(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)
    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    '''Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]'''
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    return L[m][n]


def common_child(s1, s2):
    return lcs(s1, s2)


def tests():
    s1 = 'ABCD'
    s2 = 'ABDC'
    res = common_child(s1, s2)
    expected = 3
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'HARRY'
    s2 = 'SALLY'
    res = common_child(s1, s2)
    expected = 2
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'AA'
    s2 = 'BB'
    res = common_child(s1, s2)
    expected = 0
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'SHINCHAN'
    s2 = 'NOHARAAA'
    res = common_child(s1, s2)
    expected = 3
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'HNHAN'
    s2 = 'ANHAAAA'
    res = common_child(s1, s2)
    expected = 3
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'ANIANA'
    s2 = 'AANA'
    res = common_child(s1, s2)
    expected = 4
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'ANIANA'
    s2 = 'ANAA'
    res = common_child(s1, s2)
    expected = 4
    print(f'{expected == res} res={res} s1={s1} s2={s2}')
    s1 = 'ABDF'
    s2 = 'FBDA'
    res = common_child(s1, s2)
    expected = 2
    print(f'{expected == res} res={res} s1={s1} s2={s2}')


if __name__ == '__main__':
    # s1 = 'ANIANA'
    # s2 = 'ANAA'
    # res = common_child(s1, s2)
    # print(f'res={res} s1={s1} s2={s2}')
    tests()
