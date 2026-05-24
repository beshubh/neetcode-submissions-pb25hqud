class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        min_prod = nums[0]
        max_prod = nums[0]
        best = max(min_prod, max_prod)
        for i in range(1, len(nums)):
            tmp_max = max_prod
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i]) 
            min_prod = min(min_prod * nums[i], tmp_max * nums[i], nums[i])
            best = max(best, max_prod, min_prod)
        return best
