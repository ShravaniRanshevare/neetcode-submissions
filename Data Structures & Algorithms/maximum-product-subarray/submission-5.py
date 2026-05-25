class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far=float("-inf")
        maxi=1
        mini=1
        for i in range(len(nums)):
            m,mi=maxi,mini 
            maxi=max(nums[i],m*nums[i],mi*nums[i]) 
            mini = min(nums[i],m*nums[i],mi*nums[i])
            max_so_far=max(max_so_far,maxi)
           
        return max_so_far