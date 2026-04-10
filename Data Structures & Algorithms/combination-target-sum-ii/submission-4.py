class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        visited = set()
        candidates.sort()
        def dfs(i: int = 0, curr_sum: int = 0):
            if i >= len(candidates):
                if curr_sum == target:
                    result.append(current.copy())
                return
            
            if curr_sum == target:
                result.append(current.copy())
                return
            
            if curr_sum + candidates[i] <= target:
                current.append(candidates[i])
                dfs(i + 1, curr_sum + candidates[i])
                current.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_sum)
        dfs()
        return result
