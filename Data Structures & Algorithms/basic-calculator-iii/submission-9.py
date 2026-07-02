class Solution:
    def calculate(self, s: str) -> int:


        def apply_op(stack, op, num):
            match op:
                case '+':
                    stack.append(num)
                case '-':
                    stack.append(-num)
                case '*':
                    stack.append(stack.pop() * num)
                case '/':
                    stack.append(int(stack.pop() / num))

        def parse(i):
            num = 0
            stack = []
            op = '+'
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num, i = parse(i + 1)
                else:
                    apply_op(stack, op, num)
                    if ch == ')':
                        return sum(stack), i
                    op = ch
                    num = 0
                i += 1
            apply_op(stack, op, num)
            return sum(stack), i
        return parse(0)[0]
 