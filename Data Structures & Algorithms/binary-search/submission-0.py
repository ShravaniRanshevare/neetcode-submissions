class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,target,low,high):
            if low>high:
                return -1
            
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                return binary(nums,target,mid+1,high)
            else:
                return binary(nums,target,low,mid-1)
            return -1
        return binary(nums,target,0,len(nums)-1)
