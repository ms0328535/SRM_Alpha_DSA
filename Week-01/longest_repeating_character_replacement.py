
def character_replacement(s, k):
    left = 0
    max_freq = 0
    max_length = 0
    freq = {}

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        max_freq = max(max_freq, freq[char])

        while (right - left + 1) - max_freq > k:
            left_char = s[left]
            freq[left_char] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


s = "AABABBA"
k = 1

print("Longest repeating substring:", character_replacement(s, k))
