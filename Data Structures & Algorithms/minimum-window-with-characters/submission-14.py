class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.Counter()
        formed = 0
        l = 0
        ans = (0, float('inf'))
        for r in range(len(s)):
            window[s[r]] += 1
            ch = s[r]
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == len(need):
                if ans[1] - ans[0] > r - l:
                    ans = (l, r)
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        if ans[1] == float('inf'):
            return ""
        return s[ans[0]: ans[1] + 1]
                
