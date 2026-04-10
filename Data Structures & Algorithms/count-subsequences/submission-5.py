class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def num_ds(i: int, j: int):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            c1 = 0
            if s[i] == t[j]:
                c1 = num_ds(i + 1, j + 1)
            c2 = num_ds(i + 1, j)
            return c1 + c2
        return num_ds(0, 0)
    