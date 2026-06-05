class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res = nums[low]
        while low<=high:
            if nums[low]<nums[high]:
                res = min(res,nums[low])
                break
            m = (low+high)//2
            res = min(res,nums[m])
            if nums[m] >= nums[low]:
                low = m+ 1
            else:
                high = m - 1
        
        return res
