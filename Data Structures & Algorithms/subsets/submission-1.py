class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        def dfs(idx: int = 0):
            if idx == len(nums):
                result.append(stack.copy())
                return
            
            stack.append(nums[idx]) 
            dfs(idx + 1)
            stack.pop()
            dfs(idx + 1)
        
        dfs()
        return result