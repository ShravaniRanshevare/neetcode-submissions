class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #since sorted uk ones at the left r smaller
        # 3 sum so for one move two other pointers across the list
        res = []
        for i,a in enumerate(nums):
            if a >0: #see u always check aage ke aka greater than so if a is positive no way aage ke will give sum 0 
                break
            if i>0 and a == nums[i-1]: #duplicates maybe 
                continue
            j = i+1
            k = len(nums)-1
            while j<k :
                three = a+nums[j]+nums[k]
                if three<0:
                    j += 1
                elif three>0:
                    k -=1
                else:
                    res.append([a,nums[j],nums[k]])
                    j += 1
                    k -=1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                    
        
        return res
                

        
        