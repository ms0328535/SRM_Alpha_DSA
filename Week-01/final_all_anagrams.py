
from collections import Counter


def find_anagrams(s, p):
    result = []
    window_size = len(p)

    if window_size > len(s):
        return result

    target = Counter(p)
    window = Counter(s[:window_size])

    if window == target:
        result.append(0)

    for right in range(window_size, len(s)):
        left_char = s[right - window_size]
        right_char = s[right]

        window[left_char] -= 1

        if window[left_char] == 0:
            del window[left_char]

        window[right_char] += 1

        if window == target:
            result.append(right - window_size + 1)

    return result


s = "cbaebabacd"
p = "abc"

print(find_anagrams(s, p))
