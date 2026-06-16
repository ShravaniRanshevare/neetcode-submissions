class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        p=0
        prev = float("-inf")
        #wait figured a pattern ..... buy on the lowest stock day thats when ur do to multiple p but when no other only one p 
        #per stock check selling days ahead of it ( u cant go back to previous day)
        #since now we can sell it on the same day maybe that is included too
        #diff from prev prob now we can make multiple sells udhar it was one sell u can make
        
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
