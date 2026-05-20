class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        best = 0
        for c in char_set:
            l = 0
            window, rr = 0, k
            for r in range(len(s)):
                if c == s[r]:
                    window += 1
                elif rr > 0:
                    rr -= 1
                    window += 1
                else:
                    while rr == 0:
                        if s[l] != c:
                            rr += 1
                        l += 1
                    window = r - l + 1
                    rr -= 1
                best = max(best, window)
        return best

