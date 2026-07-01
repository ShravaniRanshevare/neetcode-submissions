class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        #dp[i][a] represents the number of ways to form amount a using coins from index i onward
        for row in range(n+1):
            dp[row][0] = 1 #ie only one way of making amt 0 from coin i choose no coins
        for c in range(n-1,-1,-1):
            for a in range(0,amount+1):
                if a>=coins[c]:
                    dp[c][a] = dp[c+1][a]
                    dp[c][a] += dp[c][a-coins[c]]
        return dp[0][amount]
