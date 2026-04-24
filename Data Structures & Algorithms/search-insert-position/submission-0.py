class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        result = 0

        while l<=r:
            mid = (l+r) //2

            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                l = mid +1
                result = mid +1
            
            elif target < nums[mid]:
                r = mid - 1
                result = mid

            else:
                result = l+1
            
        return result

            