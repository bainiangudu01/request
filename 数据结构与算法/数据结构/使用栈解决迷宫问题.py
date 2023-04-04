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


def maze_path_stack(x1, y1, x2, y2):  # x1,y1代表起点位置，x2,y2代表终点位置，x代表行
    stack = []  # 创建空栈
    stack.append((x1, y1))  # 栈中增加起点，以元组表示起点（元素是二维的）
    while len(stack) > 0:  # 栈长度为0时表示没有通路
        curNode = stack[-1]  # 当前的位置
        if curNode[0] == x2 and curNode[1] == y2:  # 判断当前节点是否是终点，是否走到终点了
            for p in stack:
                print(p)  # 打印出来走的路径
            return True  # 如果走到终点就证明有路返回True

            # x,y的四个方向：上：x-1,y 下：x+1,y 左：x,y-1 右：x,y+1
        for dir in dirs:  # 搜索4个方向，dir是一个函数
            nextNode = dir(curNode[0], curNode[1])  # 下一个位置
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下个节点能走
                stack.append(nextNode)  # 就将下个节点加到栈里
                maze[nextNode[0]][nextNode[1]] = 2  # 然后将走过的这个位置标记为2，避免走回头路
                break  # 找到一个能走的点就不需要找其它点了
        else:  # 如果循环结束一个能走的点都找不到
            maze[nextNode[0]][nextNode[1]] = 2  # 也将这个位置标记成2，这个点尝试过了
            stack.pop()  # 然后出栈回退，找前一个节点看还有没有能走的，因为走过的都标记2了，所以回退前一个节点走过的就不会再走了
    else:  # 栈空的时候表示没路返回False
        print("没有路")
        return False


maze_path_stack(1, 1, 8, 8)
