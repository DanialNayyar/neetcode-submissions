class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        dictionary = {}
        
        if len(s) == len(t):

            for character in s:
                dictionary[character] = dictionary.get(character,0)+1

            for character in t:
                dictionary[character] = dictionary.get(character,0)-1

            return all(value == 0 for value in dictionary.values())

        else:
            return False