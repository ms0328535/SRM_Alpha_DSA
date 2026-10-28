class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1

        def possible(limit):
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= limit:
                    pages += book
                else:
                    students += 1
                    pages = book

            return students <= k

        left = max(arr)
        right = sum(arr)

        while left < right:
            mid = left + (right - left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left