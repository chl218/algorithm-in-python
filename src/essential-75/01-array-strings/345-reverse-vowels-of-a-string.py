""" 345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        b, e = 0, len(s)-1
        
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        slst = [c for c in s]
        
        while b < e:
            if s[b] in vowels and s[e] in vowels:
                slst[b], slst[e] = slst[e], slst[b]
                b += 1
                e -= 1
            elif s[b] in vowels:
                e -= 1
            elif s[e] in vowels:
                b += 1
            else:
                b += 1
                e -= 1
                
        return ''.join(slst)