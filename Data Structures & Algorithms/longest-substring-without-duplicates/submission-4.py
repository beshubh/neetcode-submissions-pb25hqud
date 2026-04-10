class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        seen = {}
        longest_seq, start, ptr = 0, 0, 0
        while ptr < len(s):
            ch = s[ptr]
            if ch not in seen or seen[ch] < start:
                longest_seq = max(longest_seq, ptr - start + 1)
                seen[ch] = ptr
                ptr += 1
            else:
                start = seen[ch] + 1
                seen[ch] = ptr
                ptr += 1
        return longest_seq
