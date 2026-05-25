class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        max_so= nums[0]
        for num in nums[1:]:
            curSum= max(num,curSum+num)
            #choosing between running sum and curr elem and choosing max one to restart if that approves
            max_so=max(max_so,curSum) 
        return max_so