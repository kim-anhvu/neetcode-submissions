class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)

        if len(nums) == 0 or len(nums) == 1:
            return False
        elif len(numsSet) < len(nums):
            return True
        else:
            return False
        