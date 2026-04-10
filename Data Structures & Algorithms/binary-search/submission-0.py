class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            if target < mid_val:
                right = mid - 1
            else:
                left = mid + 1
        return  -1