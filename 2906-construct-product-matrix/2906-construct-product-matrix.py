class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        arr = []
        for row in grid:
            arr.extend(row)

        size = len(arr)
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % 12345
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % 12345

        ans = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append((prefix[idx] * suffix[idx]) % 12345)
                idx += 1
            ans.append(row)
        return ans