class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first positive integer missing can only be
        # from 1 to N + 1 (N+1 because there can be 0 in the nums as well)
        numset = set(nums) 
        for i in range(1, len(nums) + 1):
            if i not in numset:
                return i
        return len(nums) + 1
