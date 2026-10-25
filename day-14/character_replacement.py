
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            if count[char] > max_frequency:
                max_frequency = count[char]

            window_length = right - left + 1

            while window_length - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
                window_length = right - left + 1

            if window_length > max_length:
                max_length = window_length

        return max_length
