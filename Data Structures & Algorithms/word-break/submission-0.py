class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]= True
        #dp[i] true or f can sub s[:i] into words from dict
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] is True and s[j:i] in wordDict:
                    dp[i]= True
                
        
        
        return dp[len(s)]
            


