class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def canBreak(target): 
            if target in memo:
                return memo[target]
            if target == '':
                return True
            for word in wordDict:
                try:
                    idx = target.index(word)
                except ValueError:
                    idx = -1
                if idx == 0:
                    suffix = target[len(word): ]
                    if canBreak(suffix):
                        memo[target] = True
                        return True
            memo[target] = False
            return False
        return canBreak(s)
