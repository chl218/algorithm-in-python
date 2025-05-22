""" 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""

# 2025/05/21
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        si, sj = 0, len(s)
        ti, tj = 0, len(t)

        matched = 0
        while si < sj and ti < tj:

            if s[si] == t[ti]:
                si += 1
                ti += 1
                matched += 1
            else:
                ti += 1

        return True if matched == sj else False