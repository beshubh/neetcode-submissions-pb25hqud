class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = [0] * len(nums)
        lr_pass = [1] * len(nums)
        rl_pass = [1] * len(nums)

        for i in range(1, len(nums)):
            lr_pass[i] = nums[i - 1] * lr_pass[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rl_pass[i] = nums[i + 1] * rl_pass[i + 1]
        
        print('lrpass', lr_pass)
        print('rl_pass', rl_pass)
        for i in range(len(nums)):
            outputs[i] = lr_pass[i] * rl_pass[i]
        return outputs
