""" 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

 
Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""        
        l1 = len(word1)
        l2 = len(word2)

        i = 0
        while i < l1 or i < l2:
            if i < l1:
                result += word1[i]
            if i < l2:
                result += word2[i]
            i += 1

        return result
    

# Attempt: 2025/05/05
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         len1_b, len1_e = 0, len(word1)
#         len2_b, len2_e = 0, len(word2)
#         res = [""] * (len1_e + len2_e) 
#         alt = True
#         i = 0
#         while len1_b < len1_e and len2_b < len2_e:
#             if alt:
#                 res[i] = word1[len1_b]
#                 len1_b += 1
#             else:
#                 res[i] = word2[len2_b]
#                 len2_b += 1
#             alt = not alt
#             i += 1
#         while len1_b < len1_e:
#             res[i] = word1[len1_b]
#             i += 1
#             len1_b += 1
#         while len2_b < len2_e:
#             res[i] = word2[len2_b]
#             i += 1
#             len2_b += 1
#         return ''.join(res)