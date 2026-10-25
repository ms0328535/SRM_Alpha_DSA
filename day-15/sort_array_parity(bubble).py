
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums
