from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the '#' separating the length from the string
            j = s.find("#", i)

            # Get the length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the string using its length
            result.append(s[j:j + length])

            # Move to the next encoded string
            i = j + length

        return result