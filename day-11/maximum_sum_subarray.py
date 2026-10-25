
class Solution:
    def maxSubarraySum(self, arr, k):
        window_sum = 0

        for i in range(k):
            window_sum += arr[i]

        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum
