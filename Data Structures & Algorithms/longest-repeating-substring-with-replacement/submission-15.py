class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = max_f = 0
        l = 0
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_f = max(max_f, counts[s[r]])
            if (r - l + 1) - max_f > k:
                counts[s[l]] -= 1
                l += 1
            best = max(r - l + 1, best)
        return best