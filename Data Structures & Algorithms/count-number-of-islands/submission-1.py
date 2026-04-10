import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            if row >= len(grid) or col >= len(grid[row]) or row < 0 or col < 0:
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'
                # visist all its neighbour
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    ans += 1
        return ans
         