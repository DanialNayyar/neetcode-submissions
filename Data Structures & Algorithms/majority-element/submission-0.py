class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        hashmap = {}
        max_allowed = (len(nums))/2
        

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1

        for key, value in hashmap.items():
            if value > max_allowed:
                print(f"print worked: {hashmap}")
                print(f"Only Keys: {hashmap.keys()}")
                print(f"Only Values: {hashmap.values()} ")
                

                return key                