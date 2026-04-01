class MinStack:

    def __init__(self):
        self.stackList = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stackList.append(val)
        if not self.minStack or val<=self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.stackList:
            return 
        val = self.stackList.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
