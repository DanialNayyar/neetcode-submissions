class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        bucket = [[] for i in range(len(nums)+1)] # bucket method
        answer = []

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i]=1
    


        for number, freq in hashmap.items():
            bucket[freq].append(number)
        
        

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                if len(answer)<k:
                    answer.append(num)
                else:
                    break
        
        return(answer)
                
        