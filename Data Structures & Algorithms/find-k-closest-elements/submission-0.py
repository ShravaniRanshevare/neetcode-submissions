class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #we have a sorted array = two pointers
        #finding k integers that r x close ie a-x < == b-x and a<b ofc
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l: r + 1]
        