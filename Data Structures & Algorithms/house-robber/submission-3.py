class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def recurse(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i]= max(nums[i]+ recurse(i+2),recurse(i+1))
            return memo[i]
        return recurse(0)