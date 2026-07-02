class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #lowers
        s = "".join(s.split()) #removes whitespace
        s = ''.join(ch for ch in s if ch.isalnum())# removes punctuation

        left = 0
        right = len(s)-1

        while left <right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        return True