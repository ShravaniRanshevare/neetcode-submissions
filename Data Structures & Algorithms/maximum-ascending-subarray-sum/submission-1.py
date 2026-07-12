class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res = nums[0]
        curSum = nums[0]
        for n in range(1,len(nums)):
            if nums[n] <= nums[n-1]:
                curSum = 0
            curSum += nums[n]
            res=max(res,curSum)
        return res