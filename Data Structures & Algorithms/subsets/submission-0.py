class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def inner(idx = 0, cur = []):
            if idx == len(nums):
                res.append(cur)
                return
            inner(idx + 1, cur)
            inner(idx + 1, cur + [nums[idx]])
        inner()
        return res 
