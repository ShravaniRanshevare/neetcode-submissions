class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #ok len of combos is k
        #n is range
        res = []
        nums = [ i for i in range(1,n+1)]
        subset=[]
        def backtrack(i,subset):
            nonlocal res
            if i >=len(nums):
                if len(subset) == k:
                    res.append(subset.copy())
                return 
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            backtrack(i+1,subset)
        
        backtrack(0,subset)
        return res 
