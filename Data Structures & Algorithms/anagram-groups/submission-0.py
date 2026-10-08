class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict= {}

        if len(strs) == 1:
            return [strs]

        for s in strs:
            sSorted = ''.join(sorted(s))
            anagramDict[sSorted] = anagramDict.get(sSorted, []) + [s]

        return list(anagramDict.values())

        
        