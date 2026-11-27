class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
            
        left = 0
        right = 1
        maxProfit = 0

        while(right < len(prices)):
            currentProfit = prices[right] - prices[left]
            if(currentProfit < 0):
                left +=1
                if(left == right):
                    right = left + 1
            else:
                maxProfit = max(maxProfit, currentProfit)
                right += 1
        return maxProfit
