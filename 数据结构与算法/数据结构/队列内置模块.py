# import queue  # 也是队列，用来保证线程安全的，做算法时不用这个
from collections import deque  # collections中有一些数据结构，deque是双向结构队列

# 创建队列，可以理解为对deque类实例化，参数可以是列表，表示创建的非空队列，第二个参数可以设置最大长度，超过长度前边的会自动出队
q = deque([1, 2, 3, 4, 5], 5)
q.append(6)  # 队尾进队，默认在右边加
print(q.popleft())  # 队首出队，在左边出，和上一个加起来是单向队列，单向队列用的比较多
# 下边用于双向队列
q.appendleft(1)  # 队首进队，在左边加
q.pop()  # 队尾出队，默认在右边出


# 由于超过长度前边的会自动出队，可以实现类似于linux的tail命令，打印文件最后几行内容
def tail(n):
    with open("tail.txt", "r") as f:
        q = deque(f, n)  # f相当于列表，文件是一行一行读的，最后是个列表
        return q


print(tail(5))

for line in tail(5):  # 使用for循环打印后5行内容
    print(line, end="")

with open("tail.txt", "r") as f:  # 打印文件前5行内容
    for ind, line in enumerate(f):
        print(line, end="")
        if ind == 4:
            break
