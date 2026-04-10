import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = max(nums[:k])
        res = [mx]

        for i in range(k, len(nums)):
            left, right = i - k, i
            leaving = nums[left]
            coming = nums[right]
            if coming > mx:
                mx = coming
            elif mx == leaving:
                # calculate the new max
                window = nums[left + 1: right + 1]
                mx = max(window)
            res.append(mx)
        return res
        