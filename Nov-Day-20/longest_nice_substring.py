
class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        for i in range(len(s)):
            char = s[i]

            if (char.lower() not in s or
                char.upper() not in s):

                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s
