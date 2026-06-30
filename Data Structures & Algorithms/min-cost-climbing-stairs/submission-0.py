class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n<=1:
            return cost[-1]
        dp = [0] * (n+1) #min cost to reach step i
        dp[0]=0
        dp[1] = 0
        for i in range(2,n+1):
            cost1 = dp[i-1]+cost[i-1] #what it took to reah here by one step+prevcost to reach here 
            cost2 = dp[i-2]+cost[i-2] #what it took to reach here by two step+precost to reach here
            dp[i] = min(cost1,cost2)
        return dp[n]
        