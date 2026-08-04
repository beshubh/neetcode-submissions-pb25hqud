class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        total_sum = sum(nums)
        def go(i: int, current_sum: int):
            key = (i, current_sum)
            if i >= len(nums):
                return current_sum == total_sum / 2
            if key in cache:
                return cache[key]
            c1 = go(i + 1, current_sum + nums[i])
            c2 = go(i + 1, current_sum) 
            cache[key] = c1 or c2
            return c1 or c2
        return go(0, 0)
