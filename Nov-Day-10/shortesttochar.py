
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        result = []
        positions = []

        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)

        for i in range(len(s)):
            distance = float('inf')

            for j in positions:
                distance = min(distance, abs(i - j))

            result.append(distance)

        return result
