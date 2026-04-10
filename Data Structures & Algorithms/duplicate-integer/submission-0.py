class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts: dict = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        return any(x > 1 for _, x in counts.items())
