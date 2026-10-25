class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if (freq[nums[j]] > freq[nums[j + 1]]) or \
                   (freq[nums[j]] == freq[nums[j + 1]] and nums[j] < nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums