class Solution:
    def calculate(self, s: str) -> int:


        def apply_op(stack: list, op: str, num):
            match op:
                case '+':
                    stack.append(num)
                case '-':
                    stack.append(-num)
                case '*':
                    stack.append(stack.pop() * num)
                case '/':
                    stack.append(int(stack.pop()/num))

        def parse(i):
            stack = []
            previous_op = '+'
            num = 0
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num, i = parse(i + 1)
                else: # + - * / )
                    apply_op(stack, previous_op, num)
                    previous_op = ch
                    num = 0
                    if ch == ')':
                        return sum(stack), i
                i += 1
            apply_op(stack, previous_op, num)
            return sum(stack), i
        return parse(0)[0]
                    

                    