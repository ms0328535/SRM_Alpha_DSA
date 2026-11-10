
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        odd_count = 0

        for value in count.values():
            if value % 2 == 1:
                odd_count += 1

        return odd_count <= 1


# Example
obj = Solution()
print(obj.canPermutePalindrome("code"))
print(obj.canPermutePalindrome("aab"))
print(obj.canPermutePalindrome("carerac"))
