
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if s.count(ch) == 1:
                return s.index(ch)

        return -1


# Example
obj = Solution()
print(obj.firstUniqChar("leetcode"))
print(obj.firstUniqChar("loveleetcode"))
print(obj.firstUniqChar("aabb"))
