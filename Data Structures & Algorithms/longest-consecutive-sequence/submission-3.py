import random
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                current_num = n
                count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1
                longest = max(longest, count)
        return longest