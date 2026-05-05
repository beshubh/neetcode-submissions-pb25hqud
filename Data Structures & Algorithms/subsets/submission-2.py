class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        running_set = []
        def dfs(i: int):
            if i >= len(nums):
                output.append(running_set.copy())
                return
            # include ith
            running_set.append(nums[i])
            dfs(i + 1)
            # exclude ith
            running_set.pop()
            dfs(i + 1)
        dfs(0)
        return output