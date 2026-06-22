class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>=nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary(target,low,high):
            while low<=high:
                m = low + (high-low)//2
                if nums[m] == target:
                    return True
                elif nums[m]>target:
                    high = m - 1
                else:
                    low = m + 1
            return False

        res = binary(target,0,pivot-1)
        if res:
            return res
        return binary(target,pivot,len(nums)-1)