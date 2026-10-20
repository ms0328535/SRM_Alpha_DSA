
def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoare(arr, low, high):
    if low < high:
        partition_index = hoare_partition(arr, low, high)

        quick_sort_hoare(arr, low, partition_index)
        quick_sort_hoare(arr, partition_index + 1, high)


arr = [4, 2, 7, 1, 3]
quick_sort_hoare(arr, 0, len(arr) - 1)
print(arr)
