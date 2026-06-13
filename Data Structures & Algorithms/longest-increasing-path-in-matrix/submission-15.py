NEIGHBORS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        indegree = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                indegree[(r, c)] = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                for (dr, dc) in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    nei = matrix[nr][nc]
                    if nei > matrix[r][c]:
                        indegree[(nr, nc)] += 1
        starts = [s for s in indegree.keys() if indegree[s] == 0]
        q = collections.deque(starts)
        result = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                for dr, dc in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if matrix[nr][nc] > matrix[r][c]:
                        indegree[(nr, nc)] -= 1
                        if indegree[(nr, nc)] == 0:
                            q.append((nr, nc))
            result += 1    
        return result
