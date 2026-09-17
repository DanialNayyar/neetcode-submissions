class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        answer = []


        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i]=1
        
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda item:item[1], reverse = True))

        
        for key,value in sorted_hashmap.items():
            if len(answer) < k:
                answer.append(key)
            else:
                return answer
        
        return answer


     