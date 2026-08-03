class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #loop through nums
        # method 1: square i then sort
        # method 2: use two pointer to sort instead of .sort()
                # left and right pointers, 
                    # left at the start,
                    # right = left +=1
                    # if left < right
# method 1 @ work
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        
        nums.sort()
        return nums

            
            