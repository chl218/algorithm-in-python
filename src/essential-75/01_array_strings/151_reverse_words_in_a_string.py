""" 151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the
words. Do not include any extra spaces.

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        words.reverse()
        words = [w for w in words if w != ""]
        
        return " ".join(words)
    

# 2025/05/14
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         slist = s.split(' ')
#         slist.reverse()
#         return ' '.join([x for x in slist if x != ''])
