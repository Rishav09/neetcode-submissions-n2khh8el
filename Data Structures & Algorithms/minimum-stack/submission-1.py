class MinStack:

    def __init__(self):
        self.stackList = []

    def push(self, val: int) -> None:
        self.stackList.append(val)

    def pop(self) -> None:
        self.stackList.pop()

    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return min(self.stackList)
