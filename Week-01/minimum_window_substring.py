def min_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""
 
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
 
    missing = len(t)
    left = 0
    best_start, best_len = 0, float("inf")
 
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
 
        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
 
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
 
    return "" if best_len == float("inf") else s[best_start:best_start + best_len]
 
 
if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # Expected: BANC
    print(min_window("a", "a"))                # Expected: a
    print(min_window("a", "aa"))               # Expected: (empty string)
 
