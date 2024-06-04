##请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.stack = []

    def max_value(self):
        return self.stack[0]


    def push_back(self, value: int):
        self.queue.append(value)
        while self.stack and value > self.stack[0]:
            self.stack.pop()
        self.stack.append(value)


    def pop_front(self):
        res = self.queue.pop(0)
        if res == self.stack[0]:
            self.stack.pop(0)
        return res