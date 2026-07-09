class Solution:
    def candy(self, ratings: List[int]) -> int:
        #dp[i] = 1
        #if dp[0] ? or do u do start with one compare to prev an if greater incrase by one
        dp = [1] * len(ratings)
        #there r like two constraints left to right and right to leftf
        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                dp[i] = dp[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                dp[i] = max(dp[i],1+dp[i+1])
        
        return sum(dp)
