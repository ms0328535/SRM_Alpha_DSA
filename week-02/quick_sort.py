
def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_lomuto(arr, low, high):
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)

        quick_sort_lomuto(arr, low, pivot_index - 1)
        quick_sort_lomuto(arr, pivot_index + 1, high)


arr = [4, 2, 7, 1, 3]
quick_sort_lomuto(arr, 0, len(arr) - 1)
print(arr)
