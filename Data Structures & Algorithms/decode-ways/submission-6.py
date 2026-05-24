class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def num_ways(i: int):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            res = num_ways(i + 1)
            if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
                res += num_ways(i + 2)
            memo[i] = res
            return memo[i]
        return num_ways(0)