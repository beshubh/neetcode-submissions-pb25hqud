class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        res = 0
        while l < len(s) and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(len(seen), res)
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return res