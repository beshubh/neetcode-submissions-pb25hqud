class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        best = max(max_prod, min_prod)
        for i in range(1, len(nums)):
            old_max = max_prod
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(min_prod * nums[i], old_max * nums[i], nums[i])
            best = max(best, max_prod, min_prod)
        return best

            
