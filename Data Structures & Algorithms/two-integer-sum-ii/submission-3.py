class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in list(set(numbers)):
            diff = target - n
            print ("n", n)
            print ("diff", diff)
            indices = [index for index,x in enumerate(numbers) if x == diff]
            print("indices", indices)

            if len(indices) > 0:
                if diff == n and len(indices) > 1:
                    print("here")
                    return [indices[0]+1, indices[1]+1]
                elif(diff == n and len(indices) < 2):
                    continue
                else:
                    indicesN = [index for index,x in enumerate(numbers) if x == n]
                    print("here2")
                    print(indicesN)
                    if indicesN[0]+1 > indices[0] + 1:
                        print("here3")
                        return [indices[0] + 1, indicesN[0]+1]
                    else:
                        print("here4")
                        return [indicesN[0]+1, indices[0] + 1]
            else:
                continue
            
