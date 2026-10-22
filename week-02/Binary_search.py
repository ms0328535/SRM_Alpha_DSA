def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
print(binary_search(nums, 9))
