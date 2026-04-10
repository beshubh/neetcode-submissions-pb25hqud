class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1

        if zeroes > 1:
            return [0]*len(nums) 
        
        if zeroes == 1:
            total_product = 0
            total_product_except_0 = 1
            zeroth_idx = -1
            for i, n in enumerate(nums):
                if n == 0:
                    zeroth_idx = i
                    continue
                total_product_except_0 *= n

            output = [0]*len(nums) 
            output[zeroth_idx] = total_product_except_0
            return output
        
        total_product = 1
        for n in nums:
            total_product *= n
        
        output = [0]*len(nums)
        for i, n in enumerate(nums):
            output[i] = total_product//nums[i]
        return output