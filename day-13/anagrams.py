
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []

        if len(p) > len(s):
            return result

        p_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        if p_count == window_count:
            result.append(0)

        for right in range(len(p), len(s)):
            window_count[ord(s[right]) - ord('a')] += 1

            left_char = s[right - len(p)]
            window_count[ord(left_char) - ord('a')] -= 1

            if p_count == window_count:
                result.append(right - len(p) + 1)

        return result
