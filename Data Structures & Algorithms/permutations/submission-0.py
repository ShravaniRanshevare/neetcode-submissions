class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        b = [False]*len(nums)
        #am pretty sure we have to call it for each num in nums
        def dfs(sub,nums,b):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return 
            for v in range(0,len(nums)):
                if not b[v]:
                    b[v] = True
                    sub.append(nums[v])
                    dfs(sub,nums,b)
                    sub.pop()
                    b[v] = False

        
        dfs(sub,nums,b)
        return res 
            
