class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = (min(val, self.min_stack[-1]) if self.min_stack else val)
        self.min_stack.append(curr_min)    

    def pop(self) -> None:
        self.stack.pop() # problem -- there is a possibility of poping a min value
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]