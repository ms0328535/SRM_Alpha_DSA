class Solution:
    def firstNonRepeating(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in arr:
            if freq[num] == 1:
                return num

        return 0