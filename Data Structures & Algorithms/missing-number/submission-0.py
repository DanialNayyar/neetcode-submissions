class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_sum = sum(range(len(nums)+1))
        acc_sum = sum(nums)
        missing_num = exp_sum - acc_sum
        return missing_num