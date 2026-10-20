
def sort_zeros_ones(arr):
    left = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr


arr = [1, 0, 1, 1, 0, 0, 1]
print(sort_zeros_ones(arr))
