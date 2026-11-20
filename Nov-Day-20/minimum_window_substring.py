
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count = {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        left = 0
        required = len(t)
        min_length = float("inf")
        start = 0

        for right in range(len(s)):
            char = s[right]

            if char in count:
                if count[char] > 0:
                    required -= 1

                count[char] -= 1

            while required == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                left_char = s[left]

                if left_char in count:
                    count[left_char] += 1

                    if count[left_char] > 0:
                        required += 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]
