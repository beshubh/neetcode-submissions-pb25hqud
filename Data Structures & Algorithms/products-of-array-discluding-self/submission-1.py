class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_mul = 1
        zero_indexes = 0
        zero_idx = -1
        for i, n in enumerate(nums):
            if n == 0:
                zero_indexes += 1
                zero_idx = i
                if zero_indexes > 1:
                    return [0]*len(nums)
                continue
            nums_mul *= n
        outputs = [0] * len(nums)
        if zero_idx != -1:
            outputs[zero_idx] = nums_mul
            return outputs
        for i in range(len(nums)):
            outputs[i] = nums_mul // nums[i]
        return outputs
