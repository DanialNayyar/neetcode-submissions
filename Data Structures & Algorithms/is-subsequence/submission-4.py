class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_pointer = 0

        for i in t:
            if s_pointer < len(s) and s[s_pointer] == i:
                s_pointer +=1
            
        return s_pointer == len(s)
