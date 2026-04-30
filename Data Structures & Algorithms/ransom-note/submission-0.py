class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashmap = {}
        can_construct = False

        for letter in magazine:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] +=1
        
        #print(f"After loop 1: {hashmap}")
        
        
        for letter in ransomNote:
            if letter in hashmap:
                hashmap[letter] -=1
            else:
                return False
        
        #print(f"After second loop: {hashmap}")

        if all (value >= 0 for value in hashmap.values()):
            can_construct = True
            return can_construct
        else:
            return can_construct
