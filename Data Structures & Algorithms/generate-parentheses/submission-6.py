class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current = []
        output = []
        def backtrack(open: int, close: int):
            if open == close == n:
                output.append(''.join(current))
                return
            if open > n or close > open:
                # invalid
                return
            current.append('(')
            backtrack(open + 1, close)
            current.pop()
            if open > close:
                current.append(')')
                backtrack(open, close + 1)
                current.pop()
        backtrack(0, 0)
        return output
