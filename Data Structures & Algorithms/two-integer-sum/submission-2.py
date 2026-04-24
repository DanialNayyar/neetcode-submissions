class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #hashmap to store number and index
        seen = {}
        
        #iterate through array num and index 
        for index,num in enumerate(nums):
            #create a check variable that checks if each index's number has been seen in the hashmap 
            check = target - num

            if check in seen:
                return [seen[check],index]
            else:
                seen[num] = index


        # Space - O(N)
        # Time - O(N)