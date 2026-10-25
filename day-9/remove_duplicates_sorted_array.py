class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        position = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[position - 1]:
                nums[position] = nums[i]
                position += 1

        return position