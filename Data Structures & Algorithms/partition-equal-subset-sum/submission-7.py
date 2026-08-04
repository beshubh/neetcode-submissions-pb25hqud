class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        total_sum = sum(nums)
        # two partitions subset means
        # let two subsets sums be a and b
        # return true on a == b
        # for two sums to be equal: a and b have to include all the elements of the nums
        # a + b = total_sum
        # a = total_sum - a
        # to prove a = b 
        # a = total_sum - a
        # 2a = total_sum
        # a = total_sum / 2
        # if we can prove a == total_sum / 2 we can prove that there are two subsets with equal sum
        if total_sum % 2 != 0:
            return False
        def go(i: int, current_sum: int):
            key = (i, current_sum)
            if i >= len(nums):
                return current_sum == (total_sum + 1) // 2
            if key in cache:
                return cache[key]
            c1 = go(i + 1, current_sum + nums[i])
            c2 = go(i + 1, current_sum) 
            cache[key] = c1 or c2
            return c1 or c2
        
        # dp = [[False] * (len(nums) + 1) for _ in range(total_sum // 2)]
        # for i in range(len(nums))
        return go(0, 0)
