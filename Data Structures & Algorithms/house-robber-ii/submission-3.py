class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        nums1 = nums[:N - 1]
        nums2 = nums[1:N]

        def dp(i: int, nums: list[int], memo: dict) -> int:
            if i < 0 or i >= len(nums):
                return 0

            if i in memo: 
                return memo[i]
            memo[i] = max(nums[i] + dp(i + 2, nums, memo), dp(i + 1, nums, memo))
            return memo[i]
        
        first_house_included = dp(0, nums1, {})
        first_house_excluded = dp(0, nums2, {})
        return max(first_house_included, first_house_excluded)