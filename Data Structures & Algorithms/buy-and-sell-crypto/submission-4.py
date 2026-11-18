class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices)-1):
            for j in range (i, len(prices)):
                if(prices[j]-prices[i] > maxProfit):
                    maxProfit = prices[j]-prices[i]

        return maxProfit