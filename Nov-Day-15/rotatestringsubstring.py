
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        doubled = s + s
        n = len(goal)

        for i in range(len(doubled) - n + 1):
            j = 0

            while (j < n and
                   doubled[i + j] == goal[j]):
                j += 1

            if j == n:
                return True

        return False
