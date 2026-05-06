class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        running_paren = [] 
        def backtrack(open: int, close: int):
            if close > open or open > n:
                return
            if open == close and close == n:
                output.append(''.join(running_paren.copy()))
                return
            # can add opening
            running_paren.append('(')
            backtrack(open + 1, close)

            running_paren.pop()
            # can add closing if open are more than close
            if open > close:
                running_paren.append(')')
                backtrack(open, close + 1)
                running_paren.pop()
        backtrack(0, 0)
        return output