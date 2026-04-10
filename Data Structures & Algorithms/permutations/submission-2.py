class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = [0] * len(nums)
        availability = [True for _ in nums]
        def backtrack(depth: int = 0):
            if all([not a for a in availability]):
                result.append(current.copy())
                return
            if depth >= len(nums):
                return 

            for i, available in enumerate(availability):
                if available:
                    current[depth] = nums[i]
                    availability[i] = False
                    backtrack(depth + 1)
                    availability[i] = True
                    current[depth] = 0
        backtrack(0)
        return result
