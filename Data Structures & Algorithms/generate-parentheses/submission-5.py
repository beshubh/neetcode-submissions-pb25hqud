class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate a valid open and close paranethes
        # parenthesis is invalid if closed or more than open, or open equals the n
        output = []
        running_paren = []
        def backtrack(open: int = 0, closed: int = 0):
            if closed > open or open > n:
                return
            
            if open == closed and closed == n:
                output.append(''.join(running_paren))
            
            # open 
            running_paren.append('(')
            backtrack(open + 1, closed)
            running_paren.pop()
            # close 
            if open > closed:
                running_paren.append(')')
                backtrack(open, closed + 1)
                running_paren.pop()
    
        backtrack()
        return output
