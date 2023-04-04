class Queue:
    def __init__(self, size=100):
        self.queue = [0 for i in range(size)]  # 不能建空列表了，长度刚开始就需要定下来
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):  # 进队列，进队时有可能是队满
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):  # 出队列，出队时是有可能队空
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]  # 指针已经指到下一个位置，不需要删除出队的元素，之后进队时会自动覆盖
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):  # 判断队空
        return self.rear == self.front

    def is_filled(self):  # 判定队满
        return (self.rear + 1) % self.size == self.front


q = Queue(5)  # 实例化可以传参，对应构造方法中的参数
for i in range(4):  # 队列长度5时只能存4个数，此时已经队满，再存第5个数时会报队满错误
    q.push(i)
print(q.pop())
q.push(4)
