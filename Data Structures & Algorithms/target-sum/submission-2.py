class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def ways(i: int, s: int):
            if i >= len(nums):
                return 1 if s == target else 0
            
            result = ways(i + 1, s + nums[i]) + ways(i + 1, s - nums[i])
            return  result
        return ways(0, 0)