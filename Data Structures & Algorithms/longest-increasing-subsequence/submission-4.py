class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        memo = {}
        def lis(i: int = 0, j: int = -1, res: int = 0) -> int:
            if i >= len(nums):
                return res
            # take
            a = -1
            if j == -1 or nums[i] > nums[j]:
                a = lis(i + 1, i, res + 1)
            # skip
            b = lis(i + 1, j, res)
            return max(a, b)
        return lis()
