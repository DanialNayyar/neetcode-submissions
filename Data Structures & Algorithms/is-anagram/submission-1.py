class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        

        letter_count_s = {}
        letter_count_t = {}

        for i in s:
            if i in letter_count_s:
                letter_count_s[i] += 1
            else:
                letter_count_s[i] = 1
        

        for j in t:
            if j in letter_count_t:
                letter_count_t[j] += 1
            else:
                letter_count_t[j] = 1

        return letter_count_s == letter_count_t