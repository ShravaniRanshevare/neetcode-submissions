class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        s = set(nums)
        res=0
        for i in range(0,len(nums)+1):
            if i not in s:
                res=i
                break
        return res
