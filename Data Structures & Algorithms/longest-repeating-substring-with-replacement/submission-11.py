class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        best = 0
        for c in char_set:
            l = 0
            count = 0
            for r in range(len(s)):
                if c == s[r]:
                    count += 1
                while (r - l + 1) - count > k and l < len(s):
                    if s[l] == c:
                        count -= 1
                    l += 1
                best = max(best, r - l + 1)
        return best
