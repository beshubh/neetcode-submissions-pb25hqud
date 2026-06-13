class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        subsequences = []
        memo = {}
        def inner(i: int, j: int):
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            a = 0
            if s[i] == t[j]:
                a = inner(i + 1, j + 1)
            memo[(i, j)] = inner(i + 1, j) + a
            return memo[(i, j)]

        return inner(0, 0)
