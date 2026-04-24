class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = []

        for i in nums: 
            if i not in nums_seen:
                nums_seen.append(i)
            else:
                return True
        
        return False