
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            for num in row:
                arr.append(num)

        k = k % (m * n)

        arr = arr[-k:] + arr[:-k] if k != 0 else arr

        result = []

        for i in range(m):
            result.append(arr[i * n:(i + 1) * n])

        return result
