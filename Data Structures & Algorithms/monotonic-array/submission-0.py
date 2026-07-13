class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pattern = None
        if nums[0] <= nums[-1]:
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True
        else:
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]:
                    return False
            return True
        
        