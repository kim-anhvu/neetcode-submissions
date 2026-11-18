class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = 0
        # right = len(prices) - 1

        # minLeft = 100
        # maxRight = 0

        # while(left <= right):
        #     if(maxRight < prices[right]):
        #         maxRight = prices[right]
        #     else:
        #         right-=1

        #     if(minLeft > prices[left]):
        #         minLeft = prices[left]
        #     else:
        #         left += 1
        
        # return max(0, maxRight - minLeft)
        
        # [6, 3, 1, 4, 5]
        maxProfit = 0
        for i in range(0, len(prices)-1):
            for j in range (i, len(prices)):
                if(prices[j]-prices[i] > maxProfit):
                    maxProfit = prices[j]-prices[i]

        return maxProfit