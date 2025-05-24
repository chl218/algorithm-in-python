""" 345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:
    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.
"""


# 2025/05/13
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        res = list(s)
        vowels = "aeiouAEIOU"

        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            elif s[i] in vowels and s[j] in vowels:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
            else:
                return ''.join(res)
        
        return ''.join(res)
            