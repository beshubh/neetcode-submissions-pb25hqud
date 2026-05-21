
NEIGHBORS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        
        # this solution reverse the condition of water flow
        # we check from which cells can water flow into the ocean
        # and we can check the same for both pacific and atlantic 
        # water can flow form any cell into pacific/atlantic if the neighboring
        # cells have height >= my current cell which is touching the ocean
        def dfs(r: int, c: int, visited: set):
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc

                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # pacific 
        for c in range(COLS):
            dfs(0, c, pacific)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
        
        # atlantic
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)
        
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        output = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    output.append([r, c])
        return output

        

             