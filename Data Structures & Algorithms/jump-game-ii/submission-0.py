class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        steps=0
        
        #assume ur curr farthest is 4 so u add it to ur pos and moves r now 2
        #and ur at last index ending condition ?
        l,r = 0,0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            l = r+1
            r = farthest
            steps += 1
        
        return steps
        

        
