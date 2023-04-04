import random

from 二叉搜索树 import BSTNode, BST


class AVLNode(BSTNode):
    def __init__(self, data):
        BSTNode.__init__(self, data)  # 调用了BSTNode的构造方法
        self.bf = 0  # balance factor平衡因子初始定位0


class AVLTree(BST):
    def __init__(self, l=None):
        BST.__init__(self, l)

    def rotate_left(self, p, c):  # 左旋，对应p、c两个节点
        s2 = c.lchild  # 刚开始s2是c的左孩子节点，其它的都没有动，不用管
        p.rchild = s2  # 将s2给p的右孩子节点
        if s2:  # 如果s2不是空
            s2.parent = p  # 刚将p的右孩子定为s2，现在将s2的父亲定为p
        c.lchild = p  # 将c和p的关系变一下
        p.parent = c
        p.bf = 0  # 上边做完，更新平衡因子，等于0适用于插入，到删除时重新改
        c.bf = 0
        return c  # 返回旋转之后的根节点

    def rotate_right(self, p, c):  # 右旋
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        c.bf = 0
        p.bf = 0
        return c  # 返回旋转之后的根节点

    def rotate_right_left(self, p, c):  # 先右旋后左旋
        g = c.lchild
        s3 = g.rchild  # 先右旋，刚开始是s3变为c的左孩子
        c.lchild = s3
        if s3:  # 反着链回去都要判断是否为空
            s3.parent = c
        g.rchild = c
        c.parent = g
        s2 = g.lchild  # 再左旋
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g
        if g.bf > 0:  # 更新bf，g.bf > 0指插到s3上
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:  # 插到s3上
            p.bf = 0
            c.bf = 1
        else:  # s1、s2、s3、s4都是空，实际插入的是g
            p.bf = 0
            c.bf = 0
        return g  # 返回旋转之后的根节点

    def rotate_left_right(self, p, c):  # 先左旋，后右旋
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2

        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = 0
        return g  # 返回旋转之后的根节点

    def insert_no_rec(self, val):  # 从插入节点的父亲开始传递bf的变化，直到bf=0，不再往上传递
        # 第一步：和BST一样，先插入，代码直接复制过来
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 把原来的return去掉，改为这个，把这个node插入结点保存一下
                    break  # 然后break

            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild  # 把原来的return去掉，改为这个，把这个node插入结点保存一下
                    break  # 然后break
            else:
                return
            # 第二步：更新balance factor
        while node.parent:  # 需要保证node插入节点的父亲不是空，是空就不需要进行循环了
            if node.parent.lchild == node:  # 如果是从左节点插入的，传递是从左子树来的，左子树更沉了
                if node.parent.bf < 0:  # 更新node.parent的bf，如果原来是-1，更新为-2
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前子树的根
                    if node.bf > 0:  # 还要分情况，看node的哪边沉,如果是右边沉，先左旋再右旋
                        n = self.rotate_left_right(node.parent, node)
                    else:  # 如果是左边沉，只右旋
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:  # 原来node.parent.bf等于1，更新之后变为0，不需要旋转
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf等于0，更新之后变为-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 是从右节点插入的，传递是从右子树传来的，右子树更沉了
                if node.parent.bf > 0:
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前子树的根
                    if node.bf < 0:  # 如果node的左边沉
                        n = self.rotate_right_left(node.parent, node)
                    else:  # node.bf=-1，不会是0，如果是0就不会往上传
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1  # 上边不更新这个，是在旋转函数里更新了
                    node = node.parent
                    continue

            n.parent = g  # 链接旋转后的子树
            if g:  # 如果g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:  # 如果g是空，说明n是根节点
                self.root = n
                break


l = list(range(10))
random.shuffle(l)
print(l)
tree = AVLTree(l)
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
