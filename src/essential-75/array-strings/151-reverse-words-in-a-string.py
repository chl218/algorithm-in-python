class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        words.reverse()
        words = [w for w in words if w != ""]
        print(words)
        
        return " ".join(words)