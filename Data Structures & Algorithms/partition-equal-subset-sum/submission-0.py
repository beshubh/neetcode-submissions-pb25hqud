class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def can_sum_to_target(nums, i, target: int) -> bool:
            if i >= len(nums):
                return False
            if target == 0:
                return True
            # take 
            if nums[i] <= target:
                if can_sum_to_target(nums, i + 1, target - nums[i]):
                    return True
            # don't take
            if can_sum_to_target(nums, i + 1, target):
                return True
            return False
        
        tsum = sum(nums)
        if tsum % 2 != 0:
            return False
        return can_sum_to_target(nums, 0, tsum // 2)


