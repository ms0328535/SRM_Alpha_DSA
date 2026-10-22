def first_bad_version(n, bad):
    lo = 1
    hi = n

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if mid >= bad:
            hi = mid
        else:
            lo = mid + 1

    return lo


print(first_bad_version(5, 4))
