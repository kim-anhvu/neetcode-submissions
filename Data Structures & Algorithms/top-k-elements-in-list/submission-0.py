class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}

        for n in nums:
            numsCount[n] = numsCount.get(n, 0) + 1

        sorted_keys = sorted(numsCount, key=lambda k: numsCount[k], reverse=True)

        return sorted_keys[:k]
        
    