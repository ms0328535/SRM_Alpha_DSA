
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try deleting the left character
                s1 = s[left + 1:right + 1]

                # Try deleting the right character
                s2 = s[left:right]

                return s1 == s1[::-1] or s2 == s2[::-1]

            left += 1
            right -= 1

        return True


# Example
obj = Solution()
print(obj.validPalindrome("aba"))
print(obj.validPalindrome("abca"))
print(obj.validPalindrome("abc"))
