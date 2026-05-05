class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap ={}
        answer = []
        for i in arr:
            if i not in hashmap:
                hashmap[i] =1
            else:
                hashmap[i]+=1

        distinct_strings = []

        for string in arr:
            if hashmap[string] ==1:
                distinct_strings.append(string)
        
        if len(distinct_strings) < k:
            return ""
        else:
            return distinct_strings[k-1]
                    