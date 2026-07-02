class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax,globMin = nums[0],nums[0]
        curM,curMi,total=0,0,0
        for num in nums:
            curM=max(curM+num,num)
            globMax = max(globMax,curM) #normal kadane
            curMi = min(curMi+num,num)
            globMin = min(globMin,curMi) # maximum wrapping sum
            total += num
        
        if globMax>0:
            return max(globMax,total-globMin) #whiever the max
        return globMax
