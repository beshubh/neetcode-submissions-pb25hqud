class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i = 0, cur_sum = 0, cur=[]):
            if cur_sum > target:
                cur.pop()
                return
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i >= len(candidates):
                if cur_sum == target:
                    res.append(cur.copy())
                return 
            # include 
            dfs(i + 1, cur_sum + candidates[i], cur + [candidates[i]])
            # exclude
            while i  + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur_sum, cur)
        
        candidates = sorted(candidates)
        dfs()
        return [list(x) for x in res]
