class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canWe(mid):
            sub,sum=1,0
            for n in nums:
                sum += n
                if sum > mid:
                    sub += 1
                    if sub > k:
                        return False
                    sum = n 
            return True

        low = max(nums)
        high = sum(nums)
        res = high
        while low<=high:
            mid = low + (high-low)//2
            if canWe(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res 
        

