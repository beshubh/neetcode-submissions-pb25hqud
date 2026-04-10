class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.Counter()
        result = None
        need_count, have, l = len(need), 0, 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1
            while need_count == have:
                # update the best answer
                if result is None or r - l + 1 <= len(result):
                    result = s[l: r + 1]
                char = s[l]
                window[char] -= 1
                if char in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return result if result else ""
