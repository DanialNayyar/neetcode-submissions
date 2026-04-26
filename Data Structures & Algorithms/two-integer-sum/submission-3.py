class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #storing y's
        # x+y = target => y = target-x
        storage = {}
        
        for pos, x in enumerate(nums):
            y = target - x
            if y in storage:
                return [storage[y],pos]
            else:
                storage[x] = pos
                    