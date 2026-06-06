from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key in count:
            if count[key]>1:
                return key