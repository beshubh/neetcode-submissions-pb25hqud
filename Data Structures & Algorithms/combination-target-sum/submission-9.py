class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        current = []
        def dfs(i: int = 0, curr_sum: int = 0):
            if i >= len(nums):
                if curr_sum == target:
                    result.append(current.copy())
                return
            
            if curr_sum == target:
                result.append(current.copy())
                return
            
            if curr_sum + nums[i] <= target:
                current.append(nums[i])
                dfs(i, curr_sum + nums[i])
                current.pop()
            
            dfs(i + 1, curr_sum)
        dfs()
        return result
