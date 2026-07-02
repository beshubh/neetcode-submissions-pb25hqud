class Solution:
    def calculate(self, s: str) -> int:

        def apply_op(stack, op, num):
            match op:
                case "+":
                    stack.append(num)
                case "-":
                    stack.append(-num)
                case "*":
                    stack.append(stack.pop() * num)
                case "/":
                    stack.append(int(stack.pop() / num))

        def parse(i):
            stack = []
            num = 0
            op = "+"
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    print('ch: ', int(ch), ',num: ', num, ',num * 10 + int(ch)', num * 10 + int(ch))
                    num = num * 10 + int(ch)
                elif ch == "(":
                    num, i = parse(i + 1)
                elif ch in "+-*/)":
                    apply_op(stack, op, num)
                    if ch == ")":
                        return sum(stack), i
                    op = ch
                    num = 0
                i += 1
            apply_op(stack, op, num)
            print('stack: ', stack, 'num: ', num)
            return sum(stack), i

        ans, _ = parse(0)
        return ans

 