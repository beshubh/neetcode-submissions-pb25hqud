class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        total_sum = sum(nums)
        def go(i: int, a: int, b: int):
            key = (i, a, b)
            if i >= len(nums):
                return a == b
            if key in cache:
                return cache[key]
            c1 = go(i + 1, a + nums[i], b)
            c2 = go(i + 1, a, b + nums[i]) 
            cache[key] = c1 or c2
            return c1 or c2
        return go(0, 0, 0)
