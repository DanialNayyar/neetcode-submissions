class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_seen = set()
#attempot 2
        for i in nums:
            if i not in num_seen:
                num_seen.add(i)
            else:
                return True
        return False