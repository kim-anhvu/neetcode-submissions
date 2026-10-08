class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.countLetters(s) == self.countLetters(t)
        
    def countLetters(self, word: str) -> dict[str, int]:
        countDict = {}

        for char in word:
            countDict[char] = countDict.get(char, 0) + 1
        
        return countDict
