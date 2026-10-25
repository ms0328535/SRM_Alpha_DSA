class Solution:
    def getFloorAndCeil(self, arr, x):
        floor = -1
        ceil = -1

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                return [arr[mid], arr[mid]]

            elif arr[mid] < x:
                floor = arr[mid]
                left = mid + 1

            else:
                ceil = arr[mid]
                right = mid - 1

        return [floor, ceil]