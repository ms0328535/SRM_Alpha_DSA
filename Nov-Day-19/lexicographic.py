
class Solution:
    def smallerString(self, s1: str, s2: str) -> str:
        n = min(len(s1), len(s2))

        for i in range(n):
            if s1[i] < s2[i]:
                return s1

            elif s1[i] > s2[i]:
                return s2

        if len(s1) < len(s2):
            return s1

        elif len(s2) < len(s1):
            return s2

        return "Both strings are equal"


obj = Solution()

print(obj.smallerString("apple", "banana"))
print(obj.smallerString("cat", "car"))
print(obj.smallerString("abc", "abcd"))
