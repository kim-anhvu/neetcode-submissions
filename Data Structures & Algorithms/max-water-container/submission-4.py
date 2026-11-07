class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        k = len(heights) - 1
        currentLargestArea = 0

        while(j < k):
            currentArea = min(heights[j], heights[k]) * (k - j)
            if(currentArea > currentLargestArea):
                currentLargestArea = currentArea
            if(heights[j] < heights[k]):
                j+=1
            elif(heights[j] == heights[k]):
                if(heights[j + 1] > heights[j + 1]):
                    j+=1
                else:
                    k -= 1
            else:
                k-=1
        return currentLargestArea

