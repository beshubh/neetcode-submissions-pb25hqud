class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        prefixes_so_far = {0: 1}
        for n in nums:
            prefix += n
            diff = prefix - k
            result += prefixes_so_far.get(diff, 0)
            prefixes_so_far[prefix] = 1 + prefixes_so_far.get(prefix, 0)
        return result