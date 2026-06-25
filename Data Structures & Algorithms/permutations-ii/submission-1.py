class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        b = [False]*len(nums)
        nums.sort() #duplicates grouped together 
        def backtrack(subset,b):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 
            for v in range(0,len(nums)):
                if b[v] :
                    continue
                if v and nums[v] == nums[v-1] and not b[v-1]: #if v basically to avoid 0 minus 1 error 
                    continue
                b[v] = True
                subset.append(nums[v])
                backtrack(subset,b)
                subset.pop()
                b[v] = False
            
        
        backtrack(subset,b)
        return res 
            