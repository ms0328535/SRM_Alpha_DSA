class Solution:
    def rowWithMax1s(self, arr):
        max_row = -1
        max_count = 0

        for i in range(len(arr)):
            count = 0
            for j in range(len(arr[0])):
                if arr[i][j] == 1:
                    count += 1

            if count > max_count:
                max_count = count
                max_row = i

        return max_row