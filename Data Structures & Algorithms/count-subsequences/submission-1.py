class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def num_ds(i: int, subseq: list[chr]):
            if i >= len(s):
                if ''.join(subseq) == t:
                    return 1
                return 0
            return num_ds(i + 1, subseq + s[i]) + num_ds(i + 1, subseq)
        return num_ds(0, '')