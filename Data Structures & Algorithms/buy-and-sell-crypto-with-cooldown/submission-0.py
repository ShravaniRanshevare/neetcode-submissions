class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #pretty sure u pick one and dfs or u dont pick that one and dfs
        #i think its like the second one but instead of i-1 its i-2 cz of cooldown
        n = len(prices)
        dp1b,dp1s = 0,0
        dp2b = 0
        for i in range(n-1,-1,-1):
            dp_buy = max(dp1s - prices[i],dp1b)
            dp_sell = max(dp2b + prices[i],dp1s)
            dp2b = dp1b
            dp1b,dp1s = dp_buy,dp_sell
        
        return dp1b