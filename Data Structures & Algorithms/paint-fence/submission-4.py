class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {} 
        def paint(post, streak):
            if post >= n:
                return 1
            key = (post, streak)
            if key in memo:
                return memo[key]

            # make this same as previous color
            # only possible if streak < 2
            ways = 0
            if streak < 2:
                ways += paint(post + 1, streak + 1)

            # make this post different that previous ones
            # there are k - 1 [exclude this color] choice
            ways += (k - 1) * paint(post + 1, 1) 
            memo[key] = ways 
            return ways
        
        # Paint the first post with K choice
        return k * paint(1, 1)
