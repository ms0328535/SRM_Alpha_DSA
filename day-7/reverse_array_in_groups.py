class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)

        for start in range(0, n, k):
            left = start
            right = min(start + k - 1, n - 1)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return arr