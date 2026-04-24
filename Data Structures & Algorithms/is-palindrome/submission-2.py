class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string+=char
            
        new_string = new_string.lower()
            
            
        return new_string == new_string[::-1]
                




            


