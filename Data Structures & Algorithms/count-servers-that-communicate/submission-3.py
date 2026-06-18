class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_servers = {x: 0 for x in range(M)}
        col_servers = {x: 0 for x in range(N)}

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    row_servers[i] += 1
                    col_servers[j] += 1

        result = 0 
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if row_servers[i] > 1 or col_servers[j] > 1:
                        result += 1
        return result
        

