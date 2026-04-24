class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a_set = set()
        for i in nums:
            if i in a_set:
                return True
            a_set.add(i)
        return False