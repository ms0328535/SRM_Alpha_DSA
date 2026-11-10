
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))
