""" 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is no

"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        tmap = {}
        for idx, tt in enumerate(t):
            if tt not in tmap:
                tmap[tt] = [idx]
            else:
                tmap[tt].append(idx)
                
        minIdx = -1
        for ss in s:
            if ss in tmap:
                matched = False
                for idx in tmap[ss]:
                    if idx > minIdx:
                        minIdx = idx
                        matched = True
                        break    
                if not matched:
                    return False
            else:
                return False
            
        return True