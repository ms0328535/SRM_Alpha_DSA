
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


# Example
obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))
print(obj.isAnagram("rat", "car"))
