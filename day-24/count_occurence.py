class Solution:
    def countFreq(self, arr, target):
        def first():
            left = 0
            right = len(arr) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == target:
                    ans = mid
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def last():
            left = 0
            right = len(arr) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == target:
                    ans = mid
                    left = mid + 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        firstIndex = first()

        if firstIndex == -1:
            return 0

        lastIndex = last()

        return lastIndex - firstIndex + 1