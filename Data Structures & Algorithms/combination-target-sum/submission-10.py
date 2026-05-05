class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []
        running_combination = []
        def dfs(i: int):
            if sum(running_combination) == target:
                output.append(running_combination.copy())
                return
            if i >= len(nums):
                return
            # include ith
            if sum(running_combination) + nums[i] <= target:
                # choose same
                running_combination.append(nums[i])
                dfs(i)
                running_combination.pop()
            # exclude ith
            dfs(i + 1)
        dfs(0)
        return output
        