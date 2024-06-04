class Queue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self,val):
        self.stack_1.append(val)

    def deleteHead(self):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        if self.stack_2:
            return self.stack_2.pop()
        return -1