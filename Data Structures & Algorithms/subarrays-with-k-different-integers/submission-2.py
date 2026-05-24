import collections

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k - 1)

    def at_most(self, nums: list[int], k: int) -> int:
        freq = collections.defaultdict(int)
        left = 0
        ans = 0
        # 1, 2, 3, 4, 5 | k = 2
        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                k -= 1
            freq[nums[right]] += 1
            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1
            ans += right - left + 1
        return ans
