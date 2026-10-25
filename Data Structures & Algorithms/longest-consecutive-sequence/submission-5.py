class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0

        numSet = set(nums)

        longestSeq = 1
        currentLen = 0
        currentBeginning = None
        currentEnd = None
        beginBlock = False
        endBlock = False

        while(len(numSet) > 0):
            if(currentBeginning is None and currentEnd is None):
                # print(numSet)
                currentBeginning = list(numSet)[0]
                # print("currentBeginning ", currentBeginning)
                currentEnd = currentBeginning
                currentLen += 1
                numSet.remove(currentBeginning)
                # print(numSet)

            if(not beginBlock and currentBeginning - 1 in numSet):
                currentBeginning -= 1
                # print("currentBeginning - 1 ", currentBeginning)
                currentLen += 1
                numSet.remove(currentBeginning)
                # print(numSet)
            else:
                beginBlock = True

            if (not endBlock and currentEnd + 1 in numSet):
                currentEnd += 1
                # print("currentEnd + 1 ", currentEnd)
                currentLen += 1
                numSet.remove(currentEnd)
                # print(numSet)
            else:
                endBlock = True
            
            if (beginBlock and endBlock):
                longestSeq = max(longestSeq, currentLen)
                beginBlock = False
                endBlock = False
                currentBeginning = None
                currentEnd = None
                currentLen = 0
        return max(longestSeq, currentLen)
