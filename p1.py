class CQueue:
# 两个栈 一个控制出 一个控制进
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        elif len(self.stack_in) > 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
