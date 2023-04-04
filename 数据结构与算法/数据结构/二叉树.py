class BiTreeNode:  # 二叉树节点类
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e


# print(root.lchild.rchild.data)

# 二叉树的遍历
# 1、前序遍历
def pre_order(root):
    if root:  # 如果有root或者root不是空，递归的终止条件
        print(root.data, end=",")  # 先访问它的根节点
        pre_order(root.lchild)  # 然后访问它的左子树
        pre_order(root.rchild)  # 访问它的右子树


# pre_order(root)
# 2、中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


# in_order(root)
# 3、后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


# post_order(root)

# 4、层次遍历
from collections import deque


def level_order(root):
    q = deque()
    q.append(root)  # 首先root进队
    while len(q) > 0:  # 只要队不空，就一直循环
        node = q.popleft()  # 出队这个节点，然后访问这个节点，相当于已经走过的路径
        print(node.data, end=",")
        if node.lchild:  # 如果node有左孩子或者左孩子不为空，就进队
            q.append(node.lchild)
        if node.rchild:  # 如果node有右孩子或者右孩子不为空，也进队
            q.append(node.rchild)


level_order(root)
