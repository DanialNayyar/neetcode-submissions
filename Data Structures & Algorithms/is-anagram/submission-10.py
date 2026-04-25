class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #default setting
        is_anagram = False
        hash_map = {}

        #length check
        if len(s) != len(t):
            return is_anagram

        #anagram check
        for char in s:
            if char in hash_map:
                hash_map[char] +=1
            else:
                hash_map[char] =1
        
        for char in t:
            if char in hash_map:
                hash_map[char] -=1
            else: # if a char is in t but not s, not an anagram
                return is_anagram
        
        #hashmap check

        if all(value == 0 for value in hash_map.values()):
            is_anagram = True
            return is_anagram
        else:
            return is_anagram        