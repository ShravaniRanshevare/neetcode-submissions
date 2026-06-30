class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        #Alice maximizes her score while Bob minimizes Alice's score. We track the score difference (Alice minus Bob) throughout the game
        #dp[i] = alice - bob at i
        n = len(stoneValue)
        dp= [float("-inf")]*(n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            total =0
            for j in range(i,min(i+3,n)):
                total += stoneValue[j]
                dp[i] = max(dp[i],total - dp[j+1]) #alice takes max between 
                                                    #total = sum of stones she takes.
                                                    #dp[j+1] = Bob’s optimal response from the next position.
                                                    #So Alice’s net gain = total - dp[j+1].
                                                    #She picks the max of these options.
        result = dp[0]
        if result == 0:
            return "Tie"
        return "Alice" if result>0 else "Bob"


