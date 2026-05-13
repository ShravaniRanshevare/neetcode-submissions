class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kaftan =set()
        for n in nums:
            if n in kaftan:
                return True
            else:
                kaftan.add(n)
        return False