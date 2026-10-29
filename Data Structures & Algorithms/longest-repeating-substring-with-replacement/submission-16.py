class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.Counter()
        best = max_f = l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_f = max(max_f, counts[s[r]])
            if (r - l + 1) - max_f > k:
                counts[s[l]] -= 1
                l += 1
            best = max(r - l + 1, best)
        return best
