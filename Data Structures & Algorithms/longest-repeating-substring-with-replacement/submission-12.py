class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        best = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            replacements_needed = r - l + 1 - max(counts.values()) # max 26
            while replacements_needed > k:
                counts[s[l]] -= 1
                l += 1
                replacements_needed -= 1
            best = max(best, r - l + 1)
        return best