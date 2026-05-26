class Solution:
    
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS, COLS = len(picture), len(picture[0])
        brows = collections.defaultdict(list)
        bcols = collections.defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B':
                    brows[r].append((r, c))
                    bcols[c].append((c, r))
        ans = 0
        for row in brows.values():
            if len(row) == 1:
                r, c = row[0]
                if len(bcols.get(c, [])) <= 1:
                    ans += 1
        return ans
