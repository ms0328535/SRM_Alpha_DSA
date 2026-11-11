
def rotateString(s, k):
    n = len(s)

    if n == 0:
        return s

    k = k % n

    return s[-k:] + s[:-k] if k != 0 else s


s = "abcdef"
k = 2

print(rotateString(s, k))
