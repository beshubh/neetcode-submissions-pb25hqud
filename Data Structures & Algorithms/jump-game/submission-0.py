class Solution:
    def canJump(self, nums: list[int]) -> bool:
        def can_jump(i: int) -> bool:
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for j in range(1, nums[i] + 1):
                if can_jump(i + j):
                    return True
            return False

        return can_jump(0)
