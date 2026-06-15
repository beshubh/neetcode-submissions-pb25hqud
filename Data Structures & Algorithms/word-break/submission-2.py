class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def canBreak(target: str):
            if target in cache:
                return cache[target]
            if target == '' or not target:
                return True
            for word in wordDict:
                if target.startswith(word):
                    rest = target[len(word):]
                    if canBreak(rest):
                        cache[target] = True
                        return True
            cache[target] = False
            return cache[target]
        return canBreak(s)
