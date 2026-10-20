
def kth_largest(arr, k):
    target = len(arr) - k
    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]

        if i == target:
            return arr[i]
        elif i < target:
            low = i + 1
        else:
            high = i - 1

    return None


arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k))
