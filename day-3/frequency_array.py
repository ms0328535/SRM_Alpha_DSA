class Solution:
    def frequencyCount(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for i in range(len(arr)):
            arr[i] = freq.get(i + 1, 0)

        return arr