# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
#def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        #so i think what we do is we have 1 to n one of these nums is picked
        #we first initialise mid as our default we call guess
        #based on guess anwer we half the search space
        #instead of a target comparison we use guess output to half search space
        low = 0
        high = n - 1 
        while low<=high:
            mid = low + (high-low)//2
            if guess(mid+1) == 0:
                return mid+1
            elif guess(mid+1) == -1:
                high = mid - 1
            else:
                low = mid + 1

