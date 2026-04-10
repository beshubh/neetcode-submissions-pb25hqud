class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} 
        def num_ds(i: int, subseq: list[chr]):
            if (i, subseq) in memo:
                return memo[(i, subseq)]
            if i >= len(s):
                if ''.join(subseq) == t:
                    return 1
                return 0
            result = num_ds(i + 1, subseq + s[i]) + num_ds(i + 1, subseq)
            memo[(i, subseq)] = result
            return result
        return num_ds(0, '')