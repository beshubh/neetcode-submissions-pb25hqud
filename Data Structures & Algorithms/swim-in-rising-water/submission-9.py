from heapq import heappop, heappush

NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        seen = set()
        pq = [(grid[0][0], (0, 0))]
        dist = collections.defaultdict(lambda: 0)
        dist[(0, 0)] = grid[0][0]
        while pq:
            w, u = heappop(pq) 
            r, c = u
            if u in seen:
                continue
            seen.add(u)
            for dr, dc in NEIGHBORS:
                vr, vc = dr + r, dc + c
                if (vr, vc) in seen:
                    continue
                if vr < 0 or vc < 0 or vr >= len(grid) or vc >= len(grid[vr]):
                    continue
                nw = grid[vr][vc]
                dist[(vr, vc)] = max(nw, dist[u])
                heappush(pq, (nw, (vr, vc)))
                
        n = len(grid)
        return dist[(n - 1, n - 1)]

                


        
