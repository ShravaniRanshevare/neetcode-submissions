class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [ 1 for _ in range(2*(len(nums)))]
        l = 0
        leng = len(nums)
        while l < len(nums):
            ans[l]=nums[l]
            ans[l+leng] = nums[l]
            l += 1
        
        return ans 