class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def f(i: int, total_sum: int = 0) -> int:
            if i >= len(nums):
                if target == total_sum:
                    return 1
                return 0
            # add, sub
            result = f(i + 1, total_sum + nums[i]) + f(i + 1, total_sum - nums[i])
            return result
        return f(0, 0)
