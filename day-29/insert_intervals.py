class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)

        self.mergeSort(intervals, 0, len(intervals) - 1)

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

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