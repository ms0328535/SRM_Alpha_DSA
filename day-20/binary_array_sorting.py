class Solution:
    def binSort(self, arr):
        count0 = 0

        for num in arr:
            if num == 0:
                count0 += 1

        for i in range(len(arr)):
            if i < count0:
                arr[i] = 0
            else:
                arr[i] = 1

        return arr