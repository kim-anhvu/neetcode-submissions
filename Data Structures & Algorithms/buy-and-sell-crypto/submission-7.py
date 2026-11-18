class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        maxProfit = 0

        while(right < len(prices)):
            priceDiff = prices[right] - prices[left]
            if priceDiff >= 0:
                if(priceDiff > maxProfit):
                    maxProfit = priceDiff
                right +=1
            else:
                left +=1
                if (left == right):
                    right = left + 1

        return maxProfit
