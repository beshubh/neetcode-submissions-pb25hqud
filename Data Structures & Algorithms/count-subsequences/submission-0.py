class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def num_ds(s: str, subseq: str):
            if not s:
                if subseq == t:
                    return 1
                return 0
            
            return num_ds(s[1:], subseq + s[0]) + num_ds(s[1:], subseq)
        return num_ds(s, "")