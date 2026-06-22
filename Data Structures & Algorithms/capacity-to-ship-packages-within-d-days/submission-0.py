import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #its like koko eating banana so limit is days so u calculate weight boat estimate days and go for smaller num of boats 
        #capacity is what ur binary search space is 
        #one ship goes in one day 

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True


        low = max(weights)
        high = sum(weights)
        res = float("inf")
        while low<=high:
            mid = (low + high) //2
            if canShip(mid):
                res = min(res,mid)
                high = mid - 1 
            else:
                low = mid + 1 
        return res 
