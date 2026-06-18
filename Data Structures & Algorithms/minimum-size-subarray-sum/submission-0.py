class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #found the o n 2 sol 
        #on sol maybe l = 0 for r in l,len if l:r >= target add to res move ahead
        #if r = len then l += 1 and r = l+1 again?
        l, total = 0, 0
        res = float("inf") #litreally what i had done but while loop 

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l] #basically now that window size is tracked then move on ahead and start from end of window 
                l += 1

        return 0 if res == float("inf") else res