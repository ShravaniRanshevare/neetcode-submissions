class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        dp = [False] * n
        dp[0] = True #starting point
        j = 0
        for i in range(n):
            if dp[i] == False:
                continue
            #if we can reach at starting point
            j = max(j,i+minJump) #furthest reach , i + min jump from i min furthest reach
            while j < min(i+maxJump+1,n):
                if s[j] == "0":
                    dp[j] = True
                j += 1
        return dp[n-1] #if end reached 
                
