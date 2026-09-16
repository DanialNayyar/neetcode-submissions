class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_group = {}
        for word in strs:
            
            char_count = [0]*26

            letters_of_word = [char for char in word]

            for letter in letters_of_word:
                char_count[ord(letter)-ord("a")] +=1

            
            signature = tuple(char_count)

            
            if signature not in anagram_group:
                anagram_group[signature] = []

            
            anagram_group[signature].append(word)


        return(list(anagram_group.values()))           
        