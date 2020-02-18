#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
'''
Longest Palindromic Substring

Solution:
    The time complexity can be reduced by storing results of subproblems.
    We maintain a boolean table[n][n] that is filled in bottom up manner.
    The value of table[i][j] is true, if the substring is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.
    https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


def longestPalSubstr(st: str) -> str:
    n = len(st)  # get length of input string

    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y in range(n)]

    # All substrings of length 1 are
    # palindromes
    max_length = 1
    i = 0
    while i < n:
        table[i][i] = True
        i = i + 1

    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1:
        if st[i] == st[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2
        i = i + 1

    # Check for lengths greater than 2.
    # k is length of substring
    k = 3
    while k <= n:
        # Fix the starting index
        i = 0
        while i < (n - k + 1):
            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1

            # checking for sub-string from
            # ith index to jth index iff
            # st[i+1] to st[(j-1)] is a
            # palindrome
            if table[i + 1][j - 1] and st[i] == st[j]:
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k
            i = i + 1
        k = k + 1
    return st[start: start + max_length]


if __name__ == '__main__':
    actual = longestPalSubstr('babad')
    print(f'expected=bab; actual={actual}')
