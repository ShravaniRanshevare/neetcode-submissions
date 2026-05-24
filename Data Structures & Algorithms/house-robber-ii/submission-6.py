class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob_linear(arr):
            memo={}
            def recurse(i):
                if i in memo:
                    return memo[i]
                if i >= len(arr):
                    return 0
                memo[i]= max(arr[i]+ recurse(i+2),recurse(i+1))
                return memo[i]
            return recurse(0)

        c1= rob_linear(nums[:-1])
        c2 = rob_linear(nums[1:])

        return max(c1,c2)