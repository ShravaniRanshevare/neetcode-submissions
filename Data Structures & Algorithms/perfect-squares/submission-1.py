class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [0] + [float('inf')] * n #dp[t] = minimum number of perfect squares needed to sum to t.
        for t in range(1, n+1):
            for i in range(1, int(t**0.5)+1):
                sq = i*i
                dp[t] = min(dp[t], 1 + dp[t - sq])
        return dp[n]
