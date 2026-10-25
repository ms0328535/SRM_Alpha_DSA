
class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        first_index = {}
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_length = i + 1

            needed = prefix_sum - k

            if needed in first_index:
                length = i - first_index[needed]

                if length > max_length:
                    max_length = length

            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

        return max_length
