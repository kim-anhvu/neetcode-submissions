import re
import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        formattedS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(formattedS) == 1:
            return True

        lenFormattedS = len(formattedS)
        # print(lenFormattedS)

        for i in range(lenFormattedS - 1, lenFormattedS - math.floor(lenFormattedS/2) - 1, -1):
            # print(lenFormattedS - 1)
            # print(lenFormattedS - math.ceil(lenFormattedS/2))
            if(formattedS[i] != formattedS[lenFormattedS - 1 - i]):
                return False
        return True
