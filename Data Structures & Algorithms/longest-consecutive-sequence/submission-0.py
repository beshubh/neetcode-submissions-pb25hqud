from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        candidates = set()
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                candidates.add(num)
        longest_res = -1 
        for num in candidates:
            longest_here = 1
            num_temp = num + 1
            while longest_here < len(nums):
                if num_temp in num_set:
                    longest_here += 1
                    num_temp += 1
                else:
                    break
            longest_res = max(longest_res, longest_here)
        return longest_res
            
