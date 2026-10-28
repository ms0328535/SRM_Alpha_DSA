class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        position = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[position] = nums[i]
                position += 1

        return position