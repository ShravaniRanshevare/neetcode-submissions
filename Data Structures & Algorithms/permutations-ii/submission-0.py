class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        b = [False]*len(nums)
        nums.sort() #duplicates grouped together 
        def backtrack(subset,b):
            if len(subset) == len(nums):
                if subset.copy() not in res:
                    res.append(subset.copy())
                return 
            for v in range(0,len(nums)):
                if not b[v]:
                    b[v] = True
                    subset.append(nums[v])
                    backtrack(subset,b)
                    subset.pop()
                    b[v] = False
            
        
        backtrack(subset,b)
        return res 
            