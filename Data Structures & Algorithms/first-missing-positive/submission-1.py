class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #ans must be in range    1 as positive smallest integer to n+1 
        #hence default is 1 or n+1
        #kinda like dp
        #if len is 3 then all nums from 1 - 3 shud be there bcz going above that range no longer smallest then
        #one more is to just sort then check
        for n in range(1,len(nums)+1):
            if n not in nums:
                return n 
        return len(nums) + 1
            