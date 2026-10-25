
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_length = len(nums) + 1

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                length = right - left + 1

                if length < min_length:
                    min_length = length

                window_sum -= nums[left]
                left += 1

        if min_length == len(nums) + 1:
            return 0

        return min_length
