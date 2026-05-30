class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def transform(x):
            return (a * x **2 + b * x + c)
        
        result = []

        if a < 0:
            left, right = 0, len(nums) - 1
            while left <= right:
                left_t = transform(nums[left])
                right_t = transform(nums[right])
                if left_t < right_t:
                    result.append(left_t)
                    left += 1
                else:
                    result.append(right_t)
                    right -= 1
        else:
            left, right = 0, len(nums) - 1 # 2, 2
            # [x1, y1, x2]
            while left <= right:
                left_t = transform(nums[left]) # x
                right_t = transform(nums[right]) # y

                if left_t > right_t: #
                    result.append(left_t)
                    left += 1
                else:
                    result.append(right_t)
                    right -= 1
            result.reverse()
        return result
        
