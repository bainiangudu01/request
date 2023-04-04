from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def print_r(path):
    curNode = path[-1]  # 当前节点就是列表的最后一个位置
    realpath = []  # 创建一个空列表，用来保存真正的路径，path不是真正的路径
    while curNode[2] != -1:  # nextNode节点进来的时候是三维的，curNode节点出去的时候也是三维的
        realpath.append((curNode[0:2]))  # 此时不需要三维了，只取前两位即可
        curNode = path[curNode[2]]  # 找到path列表中这个节点对应的上个节点
    realpath.append(curNode[0:2])  # 此时curNode[2] == -1，把起点放进去
    realpath.reverse()  # 对realpath原列表进行倒序
    print(realpath)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()  # 实例化创建队列
    queue.append((x1, y1, -1))  # 进来的是一个节点，但是节点是三维的，包含节点的位置和谁让它进来的
    path = []  # 为了保存路径创建一个空列表，一旦有节点出队，就将出队的节点放到这个空列表里
    while len(queue) > 0:  # 如果队空表示有出队，但无进队，即几条路都是死路
        curNode = queue.popleft()  # 当前节点是队首节点，让它出队，先进先出，并将值保存在curNode中
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:  # 到了终点，此时终点位置已经出队，在列表中
            print_r(path)  # 打印路径
            return True

        for dir in dirs:  # 搜索4个方向的可走节点，存到队里
            nextNode = dir(curNode[0], curNode[1])  # dir是一个函数，根据当前节点，返回下一个节点
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下个节点能走
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # 就将下个节点进队，len(path)-1)是curNode在path中的位置
                maze[nextNode[0]][nextNode[1]] = 2  # 然后将这个节点标记为走过
    else:  # 队空的时候没有路
        print("没有路")
        return False


maze_path_queue(1, 1, 8, 8)
