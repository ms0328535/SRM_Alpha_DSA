class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()

        n = len(arr)
        remove_count = n // 20

        total = 0

        for i in range(remove_count, n - remove_count):
            total += arr[i]

        remaining_count = n - 2 * remove_count

        return total / remaining_count