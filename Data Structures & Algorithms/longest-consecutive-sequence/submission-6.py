class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in numSet:
            if not num - 1 in numSet:
                currentLen = 1
                currentNum = num

                while currentNum + 1 in numSet:
                    currentLen += 1
                    currentNum += 1
                longestSeq = max(longestSeq, currentLen)
        return longestSeq
        



        