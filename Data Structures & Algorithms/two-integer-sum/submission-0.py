class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        store: dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                return sorted([i, store[diff]])
            else:
                store[nums[i]] = i
