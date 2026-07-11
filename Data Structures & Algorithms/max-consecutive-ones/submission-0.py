class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for b in nums:
            if b != 1:
                count = 0
            else:
                count += 1
                maxCount = max(maxCount,count)
        return maxCount