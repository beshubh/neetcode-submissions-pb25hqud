class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def get_output(output_i: int, nums: list[int]):
            op = 1
            for i, n in enumerate(nums):
                if i == output_i:
                    continue
                op = op * n
            return op

        outputs = [0] * len(nums)
        for i in range(len(nums)):
            outputs[i] = get_output(i, nums)
        return outputs
