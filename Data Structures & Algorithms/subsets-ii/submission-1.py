class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        nums.sort()
        def backtrack(i: int = 0):
            if i >= len(nums):
                result.append(current.copy())
                return

            current.append(nums[i]) 
            backtrack(i + 1)
            current.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack()
        return result
            