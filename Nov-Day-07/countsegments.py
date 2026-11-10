
class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split()
        return len(words)


# Example
obj = Solution()
print(obj.countSegments("Hello, my name is John"))
print(obj.countSegments("Hello"))
print(obj.countSegments("   "))
