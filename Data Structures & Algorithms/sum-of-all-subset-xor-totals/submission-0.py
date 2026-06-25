class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []
        def backtrack(i,subset):
            nonlocal res 
            tmp=0
            for elem in subset:
                tmp ^= elem
            res += tmp
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1,subset)
                subset.pop()

        backtrack(0,subset)
        return res

