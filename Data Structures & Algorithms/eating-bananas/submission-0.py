import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high
        while low <=high:
            mid = (low+high)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <=h:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result 
