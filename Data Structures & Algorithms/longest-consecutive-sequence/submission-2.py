class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        result = 0
        for i in range(len(nums)):
            n = nums[i]
            if n - 1 not in numset:
                sz = 0
                while n in numset:
                    n += 1
                    sz += 1
                result = max(result, sz)
        return result