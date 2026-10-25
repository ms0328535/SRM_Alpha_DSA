# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation.
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:
# """

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        n = mountain_arr.length()

        # Find Peak
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # Binary Search (Ascending)
        left = 0
        right = peak

        while left <= right:
            mid = left + (right - left) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # Binary Search (Descending)
        left = peak + 1
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1