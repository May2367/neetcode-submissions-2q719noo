class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force

        max_profit = -float('inf')
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        
        if max_profit > 0:
            return max_profit
        else:
            return 0