import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s: dict = collections.defaultdict(int)
        freq_t: dict = collections.defaultdict(int)
        for i, j in zip(s, t):
            freq_s[i] += 1
            freq_t[j] += 1
        
        for i in s:
            if freq_s[i] != freq_t[i]:
                return False
        return True
