class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        result = max(nums)
        max_ps = 1
        min_ps = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                max_ps, min_ps = 1, 1
                continue
            tmp = max_ps
            max_ps = max(nums[i] * max_ps, nums[i] * min_ps, nums[i])
            min_ps = min(nums[i] * tmp, nums[i] * min_ps, nums[i])
            result = max(max_ps, min_ps, result)
        return result
