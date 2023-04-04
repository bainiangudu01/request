# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# a = Node(1)  # 创建节点，a节点等于Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b  # 将a和b连接起来
# b.next = c  # 将b和c连接起来，这时只需通过a节点就可以找到c
# print(a.next.item)
# print(a.next.next.item)
# print(a.next.next.next.item)


# 头插法
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None


# def creat_linklist_head(l):
#     head = Node(l[0])  # 实例化创建列表头结点
#     for element in l[1:]:
#         node = Node(element)  # 创建新节点，插到头这里
#         node.next = head  # 第一步：将node的下一个节点指向原来的head
#         head = node  # 第二步：将head重新赋值指向node节点
#     return head  # 返回头结点
#
#
# lk = creat_linklist_head([1, 2, 3])
# print(lk.item)  # 打印出的是头
# print(lk.next.item)
# print(lk.next.next.item)  # 一个个打印太麻烦，可以用循环打印
#
#
# def print_linklist(lk):  # 打印链表相当于链表的遍历
#     while lk:  # 只要lk不是None
#         print(lk.item, end=',')
#         lk = lk.next
#
#
# print_linklist(lk)


# 尾插法，不能只维护一个头结点，还要维护一个尾节点
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def creat_linklist_tail(l):
    head = Node(l[0])  # 根据第一个节点创建头结点
    tail = head  # 初始时头和尾指向的一样
    for element in l[1:]:
        node = Node(element)  # 创建新节点，插到尾这里，将新节点成为新的尾巴
        tail.next = node  # 第一步：将原来的尾节点下一个节点指向新节点
        tail = node  # 第二步：将tail重新赋值指向node节点
    return head  # 返回头结点，不管是头插法还是尾插法，都是返回头结点，从头结点一直往下找


def print_linklist(lk):  # 打印链表相当于链表的遍历
    while lk:  # 只要lk不是None
        print(lk.item, end=',')
        lk = lk.next


lk = creat_linklist_tail([1, 2, 3, 6, 8])

print_linklist(lk)
