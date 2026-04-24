class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #attempt 2
        num_seen = {}
        for index,num in enumerate(nums):
            check = target - num
            if check in num_seen:
                return [num_seen[check],index]
            else:
                num_seen[num] = index
        