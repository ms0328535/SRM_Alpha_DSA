
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n // 2 + 1):

            if n % length == 0:
                count = n // length
                pattern = s[:length]
                result = ""

                for i in range(count):
                    result += pattern

                if result == s:
                    return True

        return False
