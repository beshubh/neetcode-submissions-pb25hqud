class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = [] 
        def inner(opening, closing, cur=[]):
            if closing > opening or opening > n or closing > n:
                return
            
            if opening + closing == 2 * n:
                result.append(''.join(cur.copy()))
                return

            cur.append('(')
            inner(opening + 1, closing, cur)
            cur.pop()
            if closing < opening: 
                cur.append(')')
                inner(opening, closing + 1, cur)
                cur.pop()
            
        
        inner(0, 0) 
        return result
        
