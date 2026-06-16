class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #while loop go thru i = 0 if i == val then i == the  ahead num 
        #ahead ver wont work
        #max u can just cover it with underscore
        i = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 
