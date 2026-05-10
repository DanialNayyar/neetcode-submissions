class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        longest_consec = 0
        for i in nums:
            if (i-1) not in nums:
                

                current = i
                count = 1

                while current + 1 in nums:
                    current +=1
                    count +=1
                
                longest_consec = max(longest_consec, count)
        
        return longest_consec
