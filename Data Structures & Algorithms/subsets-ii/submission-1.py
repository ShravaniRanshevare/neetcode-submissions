class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub=[]
        nums.sort()
        def dfs(i,prev=None):
            if i>=len(nums):
                res.append(sub.copy())
                return 
            
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res 