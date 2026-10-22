def frequency_sort(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    arr = nums[:]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (freq[arr[i]], -arr[i]) > (freq[arr[j]], -arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr


nums = [1, 1, 2, 2, 2, 3]
print(frequency_sort(nums))
