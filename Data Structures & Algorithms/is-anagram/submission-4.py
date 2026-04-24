class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        # length check
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] +=1
        #is_anagram = False
        for i in t:
            if (i not in count) or (count[i] <=0): 
                #return is_anagram
                return False
            else:
                count[i] -=1
        return True
        
        
        