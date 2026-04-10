import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [max(nums[:k])]
        for i in range(k, len(nums)):
            l = i - k + 1
            r = i + 1
            window = nums[l:r]
            res.append(max(window))
        return res
        