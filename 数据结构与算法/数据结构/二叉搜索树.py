import random


class BSTNode:  # 就是二叉树节点类
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None  # 删除操作需要用到parent


class BST:
    def __init__(self, l=None):
        self.root = None
        if l:  # 如果l不是none时，将l中元素都插入
            for val in l:
                self.insert_no_rec(val)

    def insert_no_rec(self, val):  # 非递归的插入
        p = self.root  # 刚开始设置p为根节点，然后val和这个比
        if not p:  # 如果刚开始p是空的，即刚开始是空树
            self.root = BSTNode(val)  # 直接就将val这个数放在root位置
            return  # 然后直接返回，什么也不用做就行
        while True:  # 如果不是空树，就开始循环，三种情况
            if val < p.data:  # 往左子树走，需要先判断左子树有没有，如果有就比一下，如果没有就插入到左子树位置
                if p.lchild:  # 如果p的左子树不是none，即p的左子树存在，p往左子树走一下
                    p = p.lchild
                else:  # 如果左子树是none，val插在这
                    p.lchild = BSTNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BSTNode(val)
                    p.rchild.parent = p
                    return
            else:
                return  # 如果相等的话，什么都不干，直接返回，中断循环

    def query_no_rec(self, val):  # 非递归的查询
        p = self.root  # p开始定义为根节点，从p开始找
        while p:  # 只要p不是空
            if p.data < val:  # 往右边找
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:  # 等于时返回True
                return p
        return None  # 循环结束没找到，即p是空的时候，返回None

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    # 删除情况1，要删除的节点是叶子节点：直接删除
    def __remove_node_1(self, node):
        if not node.parent:  # 如果node的父节点是空，即node是根节点
            self.root = None  # 让这棵树变成空树，即删除根节点
        if node == node.parent.lchild:  # 如果node是它父亲的左孩子
            node.parent.lchild = None  # 将它父亲的左孩子置为空，实现删除
            node.parent = None  # 这行写不写都行，断连接断一个就可以
        else:  # 如果node是它父亲的右孩子
            node.parent.rchild = None

    # 删除情况2，要删除的节点只有一个孩子：将此节点的父亲与孩子连接，爷爷连孙子，然后删除该节点；如果此时删除的是根，需要重新更新根
    def __remove_node_2_1(self, node):  # 只有一个左孩子的情况
        if not node.parent:  # 如果删除的这个是根节点，它的左孩子更新为新的根
            self.root = node.lchild
            node.lchild.parent = None  # 它现在是根了，它的父亲要置为空
        elif node == node.parent.lchild:  # 如果要删除的节点是它父亲的左孩子
            node.parent.lchild = node.lchild  # 那么将它父亲左边和它左孩子连接起来
            node.lchild.parent = node.parent  # 连回去
        else:  # 如果要删除的节点是它父亲的右孩子
            node.parent.rchild = node.lchild  # 那么将它父亲右边和它左孩子连接起来
            node.lchild.parent = node.parent  # 连回去

    def __remove_node_2_2(self, node):  # 只有一个右孩子的情况
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):  # 二叉搜索树删除操作，情况3用到情况1和2，放在delete里
        if self.root:  # 如果不是空树，再删，空树直接报错就行
            node = self.query_no_rec(val)  # 先找到这个节点，然后判断node满足哪种情况
            if not node:  # 如果node为none或不存在
                return False
            if not node.lchild and not node.rchild:  # 如果左右孩子都没有，第一种情况
                self.__remove_node_1(node)
            elif not node.rchild:  # 如果无右孩子，2-1情况；如果左孩子也没有，会执行上一个，不会到这
                self.__remove_node_2_1(node)
            elif not node.lchild:  # 如果无左孩子，2-2情况
                self.__remove_node_2_2(node)
            else:  # 情况3，两个孩子都有，先找其右子树里的最小节点，也就是找其右子树最左的点
                min_node = node.rchild
                while min_node.lchild:  # 如果右子树有左侧节点才找
                    min_node = min_node.lchild
                node.data = min_node.data  # 其右子树里的最小节点替换当前节点，然后删除右子树里的最小节点的位置
                if min_node.rchild:  # 此时min_node只有是叶子结点或只有右孩子节点两种情况
                    self.__remove_node_2_2(min_node)
                else:
                    self.__remove_node_1(min_node)


# tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
# # l = list(range(0, 40, 2))  # 偶数
# # random.shuffle(l)
# # tree = BST(l)  # 使用这个可以发现中序是排好序的
#
# # tree.pre_order(tree.root)
# # print("")  # 起个打印回车的作用
# tree.in_order(tree.root)
# print("")
# # tree.post_order(tree.root)
# # print("")
# # print(tree.query_no_rec(6))  # 查询
# tree.delete(4)
# tree.delete(1)
# print(tree.delete(0))
# tree.in_order(tree.root)
