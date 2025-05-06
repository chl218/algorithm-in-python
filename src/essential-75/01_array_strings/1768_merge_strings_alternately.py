""" 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
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