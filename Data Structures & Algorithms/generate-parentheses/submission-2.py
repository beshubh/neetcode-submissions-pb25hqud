class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []
        def backtrack(open: int = 0, close: int = 0):
            if close > open or open > n:
                return
            
            if open == close  and close == n:
                print('open: ', open, 'n: ', n)
                result.append(''.join(current))
                return
            
            current.append('(')
            backtrack(open + 1, close)
            current.pop()
            if open > close:
                current.append(')')
                backtrack(open, close + 1)
                current.pop()
        backtrack()
        return result
