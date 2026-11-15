
class Solution:
    def isPrefix(self, s: str, prefix: str) -> bool:
        if len(prefix) > len(s):
            return False

        for i in range(len(prefix)):
            if s[i] != prefix[i]:
                return False

        return True


obj = Solution()

print(obj.isPrefix("programming", "pro"))
print(obj.isPrefix("programming", "gram"))
