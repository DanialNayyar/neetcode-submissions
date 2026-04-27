class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            count = [0]*26            
            chars = list(word)
            for i in chars:
                index = ord(i)-ord("a")
                count[index] +=1
            
            signature = tuple(count)

            if signature not in hashmap:
                hashmap[signature] = []
            
            hashmap[signature].append(word)
            

      

        
        #print(signature) 
                

        
        #print(count)
        return(list(hashmap.values()))
           