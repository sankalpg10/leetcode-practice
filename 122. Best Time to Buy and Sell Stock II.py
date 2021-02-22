class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        totProfit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                totProfit += prices[i] - prices[i - 1]
        
        return totProfit
        
        
        
# 1 3 4 5 6 7
"""
for each buying price find the max amount of profit you can have.
add that profit to totprofit
and return total profit
O(n*n)

greedy strategy:
buy a share and sell it as soon as you get best price
"""
