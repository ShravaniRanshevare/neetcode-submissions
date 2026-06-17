class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #first idea was to just use k as pivot index and keep on swapping k and l till l < pivot or smth so pretty close
        #def shift (nums):
            #for i in range(len(nums)-2, -1,-1):
                #nums[i+1]=nums[i]
        #count = 0
        #l = 0
        #r = len(nums)-1
        #while count<k:
            #last = nums[r]
            #shift(nums)
            #nums[l]= last
            #count += 1 second idea was this lowkey cool but they did not want it
        n = len(nums)
        tmp = [0]*n
        for i in range(n):
            ind = (i+k)%n
            tmp[ind] = nums[i]
        
        nums[:] = tmp