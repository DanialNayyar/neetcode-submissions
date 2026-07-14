class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        left = 0
        right = len(nums)-1
        ans = []
        while left <right:
            if nums[left] + nums[right] < target:
                left +=1
            elif nums[left] + nums[right] > target:
                right -=1
            
            else:
                ans.append(left+1)
                ans.append(right+1)
                return ans
