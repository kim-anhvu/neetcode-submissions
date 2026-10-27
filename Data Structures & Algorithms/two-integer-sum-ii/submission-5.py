class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in list(set(numbers)):
            diff = target - n
            indices = [index for index,x in enumerate(numbers) if x == diff]

            if len(indices) > 0:
                if diff == n and len(indices) > 1:
                    return [indices[0]+1, indices[1]+1]
                elif(diff == n and len(indices) < 2):
                    continue
                else:
                    indicesN = [index for index,x in enumerate(numbers) if x == n]
                    if indicesN[0]+1 > indices[0] + 1:
                        return [indices[0] + 1, indicesN[0]+1]
                    return [indicesN[0]+1, indices[0] + 1]
            continue
            
