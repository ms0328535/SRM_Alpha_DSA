
from collections import Counter


def check_inclusion(s1, s2):
    window_size = len(s1)

    if window_size > len(s2):
        return False

    target = Counter(s1)
    window = Counter(s2[:window_size])

    if window == target:
        return True

    for right in range(window_size, len(s2)):
        left_char = s2[right - window_size]
        right_char = s2[right]

        window[left_char] -= 1

        if window[left_char] == 0:
            del window[left_char]

        window[right_char] += 1

        if window == target:
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"

print(check_inclusion(s1, s2))
