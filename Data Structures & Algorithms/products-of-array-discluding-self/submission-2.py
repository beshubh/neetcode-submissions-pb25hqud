class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_mul = 1
        zero_indexes = 0
        zero_idx = -1
        outputs = [0] * len(nums)
        for i, x in enumerate(nums):
            zero_indexes += 1 if x == 0 else 0
            zero_idx = i if x == 0 else zero_idx
            nums_mul *= 1 if x == 0 else x

        if zero_indexes > 1:
            return outputs
        
        if zero_idx != -1:
            outputs[zero_idx] = nums_mul
            return outputs

        for i in range(len(nums)):
            outputs[i] = nums_mul // nums[i]
        return outputs
