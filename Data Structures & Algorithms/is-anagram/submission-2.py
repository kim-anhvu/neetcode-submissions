class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.countLetters(s) == self.countLetters(t)
        
    def countLetters(self, word: str) -> dict[str, int]:
        countDict = {}

        for char in word:
            if countDict.get(char) is None:
                countDict.update({char: 1})
            else:
                countDict.update({ char: countDict.get(char) + 1})
        return countDict
