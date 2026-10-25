class Solution:
    def inversionCount(self, arr):
        return self.mergeSort(arr)[1]

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, inv_left = self.mergeSort(arr[:mid])
        right, inv_right = self.mergeSort(arr[mid:])

        merged = []
        i = j = 0
        inv = inv_left + inv_right

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inv