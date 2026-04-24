class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result, solution = [],[]

        def backtracking(i):
            #base case - edge of array/leaf of tree
            if i == n:
                result.append(solution[:])
                return
            
            # not i -
            backtracking(i+1)
            # i -
            # append the num at 
            # backtract index, i+1
            # pop/remove the ith index to avoid duplicates
            solution.append(nums[i])
            backtracking(i+1)
            solution.pop()

        backtracking(0)
        return result
