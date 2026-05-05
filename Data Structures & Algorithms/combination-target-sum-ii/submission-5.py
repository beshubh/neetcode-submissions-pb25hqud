class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        candidates.sort()
        running_combination = []
        def dfs(i: int):
            if sum(running_combination) == target:
                output.append(running_combination.copy())
                return
            if i >= len(candidates):
                return
            
            if sum(running_combination) + candidates[i] <= target:
                running_combination.append(candidates[i])
                dfs(i + 1)
                running_combination.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return output