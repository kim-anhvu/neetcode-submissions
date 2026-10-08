class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        current = 0
        result = []
        while(current < len(s)):
            delimiterIndex = s.find("#", current)
            strlength = int(s[current : delimiterIndex])
            current = delimiterIndex + 1 + strlength
            result.append(s[delimiterIndex+1:current])

        return result