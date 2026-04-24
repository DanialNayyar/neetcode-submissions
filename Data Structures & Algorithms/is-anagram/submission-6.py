class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # length check - Worked
        if len(s) != len(t):
            return False
        """        
        else:#Anagram check - Didnt work for every test case, failed when s had more than one of a letter but t only had one of that same letter.
            #e.g. s="bbcc"
            #    t="ccbc"
            for letter in s:
                if letter not in t:
                    return False
                else:
                    continue
                
            return True 
        """


        # Anagram check attempt 2 - hashmap(i.e. dictionary)

        # hashmap
        letters_in_s = {}

        #filling the hashmap
        for letter in s:
            if letter not in letters_in_s:
                letters_in_s[letter] = 1
            else:
                letters_in_s[letter] +=1

        #print(letters_in_s)   # runs as expected, output is correct  
        

        # checking if element in hashmap is in t

        for character in t:
            if (character not in letters_in_s) or (letters_in_s[character] <= 0):
                return False
            else:
                letters_in_s[character] -=1
        return True