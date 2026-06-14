class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #so at each stage two choices pos or neg of num and then that leads to its own path towards sum
        #if found add to res and return len(res)
        def backtrack(i, total):
            if i ==len(nums):
                return  total == target
            return (backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i]))

        return backtrack(0, 0)
                
            