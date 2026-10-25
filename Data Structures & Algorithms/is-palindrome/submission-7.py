import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        formattedS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(formattedS) == 1:
            return True

        lenFormattedS = len(formattedS)

        for i in range(len(formattedS) // 2):
            if formattedS[i] != formattedS[len(formattedS) - 1 - i]:
                return False

        return True
