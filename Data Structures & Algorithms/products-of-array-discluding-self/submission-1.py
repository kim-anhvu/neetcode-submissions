import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeros = [i for i,val in enumerate(nums) if val==0]
        productNums = 0;

        if(len(zeros) > 1):
            print([0 for num in nums])
            return [0 for num in nums]

        if(len(zeros) == 1):
            return [math.prod(nums[:i] + nums[i+1:]) if num == 0 else 0
 for i, num in enumerate(nums)]

        if(len(zeros) == 0):
            productNums = math.prod(nums)
            
        output = []

        for i in range(0, len(nums)):
            output.append(int(productNums / nums[i]))
        
        return output