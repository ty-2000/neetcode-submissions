class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(val, self.minimum) if self.minimum != None else val
        

    def pop(self) -> None:
        ret = self.stack.pop()
        self.minimum = min(self.stack) if self.stack else None
        return ret
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum

