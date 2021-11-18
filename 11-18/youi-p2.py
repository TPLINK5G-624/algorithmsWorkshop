class MinStack:

# 一个主栈负责存储数据，另一个辅助栈负责记录最小值
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack =[]
        self.m = [math.inf]


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.m or self.m[-1] > x:
            self.m.append(x)

    def pop(self) -> None:
        t = self.stack.pop()
        if t == self.m[-1] and t not in self.stack:
            self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.m[-1]
