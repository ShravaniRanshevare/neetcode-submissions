class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #so per boat = 2 peeps == total weight == <limit 
        #infinite boats return min boats coverig all peeps
        #my diff approach was correct bish
        l = 0
        r = len(people)-1
        res = 0
        people.sort()
        while l <= r :
            remain = limit - people[r]
            r -= 1
            res += 1 
            if l<=r and remain>=people[l]:
                l += 1
        return res 

            

