class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)

        #check 1- length of lists
        if len(list_s) != len(list_t):
            print("False")
            return False
        #check 2- anagram check
        for i in list_s:
            if i in list_t:
                list_t.remove(i)
            else: 
                return False 
        return True
        