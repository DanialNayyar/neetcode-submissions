class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_seen = {}

        for index, num in enumerate(nums):
            check = target - num #new check for each array

            if check in num_index_seen:
                return [num_index_seen[check],index] # will return as a list

            else:
                num_index_seen[num] = index # add the number for the current index to num_index_seen 


