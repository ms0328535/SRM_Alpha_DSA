
def counting_sort(arr):
    if len(arr) == 0:
        return arr

    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    count = [0] * (maximum - minimum + 1)

    for num in arr:
        count[num - minimum] += 1

    index = 0

    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i + minimum
            index += 1
            count[i] -= 1

    return arr


arr = [4, 2, 2, 1, 4, 3, -1]
print(counting_sort(arr))
