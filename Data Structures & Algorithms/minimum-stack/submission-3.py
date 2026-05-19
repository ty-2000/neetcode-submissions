class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.stack)
        

    def pop(self) -> None:
        ret = self.stack.pop()
        if self.stack: self.minimum = min(self.stack)
        return ret
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum

