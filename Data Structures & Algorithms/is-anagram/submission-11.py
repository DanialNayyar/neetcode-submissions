class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] +=1
        

        for i in t:
            if i not in s_dict:
                return False
            else:
                s_dict[i] -=1
        
        if all(count == 0 for count in s_dict.values()):
            return True
        else:
            return False
