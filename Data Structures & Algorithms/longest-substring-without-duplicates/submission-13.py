import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        window = set()
        ans = l = 0
        for r in range(len(s)):
            ch = s[r]
            while l < r and ch in window:
                window.remove(s[l])
                l += 1
            window.add(ch)
            ans = max(ans, len(window))
        return ans

