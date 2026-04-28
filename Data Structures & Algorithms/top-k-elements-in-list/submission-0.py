class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        answer = []
        for num in nums:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1



        sorted_vals = sorted(hashmap.items(), key= lambda x:x[1],reverse =True )

        for num,frequncy in sorted_vals[:k]:
            answer.append(num)
        #print(f"Answer is: {answer}")
        return answer

        #print(f"hashmap: {hashmap}")
        #print(f"Sorted Vals: {sorted_vals}")        