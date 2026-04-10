class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        result = float('-inf')
        for i in range(len(nums)):
            subprod = 1
            for j in range(i, len(nums)):
                subprod *= nums[j]
                result = max(subprod, result)
                print('i, j', i, j, 'subprod', subprod)
        return result
