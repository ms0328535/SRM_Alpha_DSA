def count_inversions(arr):
    def merge_count(left, right):
        result = []
        i = 0
        j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                count += len(left) - i

        result.extend(left[i:])
        result.extend(right[j:])

        return result, count

    def sort_count(values):
        if len(values) <= 1:
            return values, 0

        mid = len(values) // 2

        left, left_count = sort_count(values[:mid])
        right, right_count = sort_count(values[mid:])

        merged, split_count = merge_count(left, right)

        total = left_count + right_count + split_count
        return merged, total

    _, count = sort_count(arr)
    return count


arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))