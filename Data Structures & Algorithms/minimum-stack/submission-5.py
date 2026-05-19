class MinStack:

    def __init__(self):
        # In addition to the stack that store the value, keep min_stack that always keeps the minimum value up to that point
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
        

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

