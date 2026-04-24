class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # nums_seen = [] => list not as fast as sets
        nums_seen = set()

        for i in nums: 
            if i not in nums_seen:
                #nums_seen.append(i)
                nums_seen.add(i)
            else:
                return True
        
        return False
        