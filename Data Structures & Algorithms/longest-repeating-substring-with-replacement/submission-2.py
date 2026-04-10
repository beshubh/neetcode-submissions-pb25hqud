class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for ch in set(s):
            l, r = 0, 0
            rleft = k
            while r < len(s):
                if s[r] == ch:
                    r += 1
                elif rleft > 0:
                    rleft -= 1
                    r += 1
                else:
                    if s[l] != ch:
                        rleft += 1
                    l += 1
                best = max(best, r - l)
        return best