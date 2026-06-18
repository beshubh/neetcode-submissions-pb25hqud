class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_servers = {x: [] for x in range(M)}
        col_servers = {x: [] for x in range(N)}

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    row_servers[i].append(j)
                    col_servers[j].append(i)

        result = 0 
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if len(row_servers[i]) > 1 or len(col_servers[j]) > 1:
                        result += 1
        return result

