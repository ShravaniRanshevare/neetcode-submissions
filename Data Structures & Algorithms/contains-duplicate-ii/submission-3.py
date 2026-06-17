class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i,a in enumerate(nums):
            if a in h and i - h[a] <= k:
                return True
            h[a]=i
        return False