class Solution:
    def findMin(self, nums: List[int]) -> int: # [3, 4, 5, 6, 1, 2]
        left, right = 0, len(nums) - 1 # 0, 5
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2 # 2
            pivot = nums[mid] # 2
            if pivot > nums[right]: # 2 > 5, false
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans
