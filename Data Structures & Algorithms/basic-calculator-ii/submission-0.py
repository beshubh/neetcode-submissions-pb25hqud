class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        previous_op = "+"
        num = 0
        s = s.replace(" ", "").strip()
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if previous_op == "+":
                    stack.append(num)
                elif previous_op == "-":
                    stack.append(-num)
                elif previous_op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                previous_op = ch
        return sum(stack)
 