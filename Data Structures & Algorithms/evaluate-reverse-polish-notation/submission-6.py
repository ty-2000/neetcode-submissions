
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        p = 0
        while p < len(tokens):
            print(stack)
            token = tokens[p]
            try:
                v = int(token)
                stack.append(v)
            except:
                v2 = stack.pop()
                v1 = stack.pop()
                if token == '+':
                    v = v1 + v2
                elif token == '-':
                    v = v1 - v2
                elif token == '*':
                    v = v1 * v2
                elif token == '/':
                    v = int(v1 / v2)
                stack.append(v)
            p += 1
        return int(stack[-1])