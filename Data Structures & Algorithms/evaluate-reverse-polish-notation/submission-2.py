class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        # ops = {
        #     "+": operator.add,
        #     "-": operator.sub,
        #     "*": operator.mul,
        #     "/": operator.truediv
        # }
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The right operand is popped first, then the left
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int(a / b) naturally truncates toward zero in Python
                    stack.append(int(a / b))
            else:
                # Token is a number
                stack.append(int(token))

        while len(stack)>1:
            b=stack.pop()
            a=stack.pop()
            new_char=f"{a} {char} {b}"
            stack.append(eval(new_char))

        return int(stack[0])

        