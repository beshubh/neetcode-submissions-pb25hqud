class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # bfs, process layer by layer, diagonals are also possible
        NEIGHBORS = [
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 0),
            (-1, 0)
        ]
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1

        q = deque([(0, 0)])
        seen = set()
        length = 1
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for dr, dc in NEIGHBORS:
                    row, col = r + dr, c + dc
                    if (
                        row >= 0 and row < N and col >= 0 and col < N and
                        (row, col) not in seen
                    ):  
                        if row == N - 1 and col == N - 1:
                            return length + 1
                        if grid[row][col] == 0:
                            q.append((row, col))
                        seen.add((row, col))
            length += 1
        return -1
