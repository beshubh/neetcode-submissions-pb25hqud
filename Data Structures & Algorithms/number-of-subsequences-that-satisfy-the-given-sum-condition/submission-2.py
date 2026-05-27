class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        mod = (10**9 + 7)
        for i in range(len(nums)):
            # get all the subsequences with min and max value <= target
            left = nums[i]
            r = len(nums) - 1
            # if left + right are <= target that means all the subsequences in that 
            # window are valid which is 2^(size of window)
            while left + nums[r] > target and r >= i: # r = i is valid, because subseq can be of length one as well
                r -= 1
            
            if r >= i:
                result += 2**(r - i)
                result %= mod

        return result 
