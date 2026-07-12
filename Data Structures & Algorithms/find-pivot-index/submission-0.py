class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] *(n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        for i in range(n):
            left = prefixSum[i]
            right = prefixSum[n] - prefixSum[i + 1]
            if left == right:
                return i
        return -1