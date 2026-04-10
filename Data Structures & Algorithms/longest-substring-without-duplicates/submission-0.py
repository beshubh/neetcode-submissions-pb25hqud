class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest_seq = 0
        longest_curr = 0
        
        ptr = 0
        while ptr < len(s):
            c = s[ptr]
            if c not in seen or seen[c] >= ptr:
                longest_curr += 1
                longest_seq = max(longest_seq, longest_curr)
                seen[c] = ptr
                ptr += 1
            else:
                t_ptr = ptr
                ptr = seen[c] + 1
                seen[c] = t_ptr
                longest_curr = 0
        return longest_seq
