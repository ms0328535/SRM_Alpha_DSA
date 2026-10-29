class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        self.mergeSort(intervals, 0, len(intervals) - 1)

        count = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]

        return count

    def mergeSort(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.mergeArray(arr, left, mid, right)

    def mergeArray(self, arr, left, mid, right):
        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i][0] <= arr[j][0]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]