""" 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        l1 = len(word1)
        l2 = len(word2)
        n = max(l1, l2)

        for i in range(n):
            if i < l1:
                result += word1[i]
            if i < l2:
                result += word2[i]

        return "".join(result)