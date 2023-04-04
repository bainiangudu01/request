class Linklist:  # 先定义一个链表类
    class Node:  # 链表里的节点，class里套一个class和函数里套一个函数一样，就像列表里可以装字典
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:  # 这个类是一个迭代器，因为它有__next__
        def __init__(self, node):
            self.node = node

        def __next__(self):  # 每执行next的时候
            if self.node:  # 如果node不是空，，
                cur_node = self.node  # 就把这个node存一下
                self.node = cur_node.next  # 然后更新node成下一个
                return cur_node.item  # 然后把前边保存的node输出出来
            else:  # 如果node是空
                raise StopIteration  # 抛出该异常，停止迭代

        def __iter__(self):  # __next__方法它的iter是返回它自己
            return self

    def __init__(self, iterable=None):  # 构造函数，允许传一个列表进来
        self.head = None  # 刚开始链表的头结点为空
        self.tail = None  # 刚开始链表的尾结点为空
        if iterable:  # 如果有这个iterable，且不是None
            self.extend(iterable)  # 就调用下边的extend函数

    def append(self, obj):  # 尾插插入一个元素，obj就是要插入的对象，
        s = Linklist.Node(obj)  # 先创建一个节点，然后把尾巴链起来
        if not self.head:  # 如果head是空的话，将新建的s设置为头结点，就一个节点，尾节点也是s
            self.head = s
            self.tail = s
        else:  # 如果不是空的话，就将s插到尾巴上
            self.tail.next = s  # 先将它跟尾巴接起来
            self.tail = s  # 然后更新尾巴

    def extend(self, iterable):
        for obj in iterable:  # 循环调append就有extend了
            self.append(obj)

    def find(self, obj):  # 哈希表要在链表里查找，就在链表里写了个查找函数，self就是lk这个对象
        for n in self:  # 此时已经支持迭代
            if n == obj:  # 如果找到，返回True
                return True
        else:  # 如果循环完没有找到，返回False
            return False

    def __iter__(self):  # iter这个函数用来写迭代器的，要让这个链表支持迭代循环，列表支持，但链表现在不支持
        return self.LinkListIterator(self.head)  # 在创建迭代器的时候又创建了迭代器类，对应嵌套的第二个类，刚开始传进了头结点

    def __repr__(self):  # 是转换为字符串的
        return "<<" + ",".join(map(str, self)) + ">>"
        # 两边套额两个尖括号，然后逗号隔开，map函数对于self可迭代对象的每一个元素都转换成字符串


lk = Linklist([1, 2, 3, 4, 5])  # 经过上边的操作，此时lk这个链表已经支持迭代循环，可以用for循环打印出来
for element in lk:
    print(element)
print(lk)


class HashTable:  # 在上边基础上创建哈希表，做一个类似于集合的数据结构
    def __init__(self, size=101):  # 哈希表的构造函数需要传一个哈希表的长度
        self.size = size  # 存一下它的大小
        self.T = [Linklist() for i in range(self.size)]  # 然后开出来T，T中包含101个位置，刚开始每个位置都是一个空链表

    def h(self, k):  # 哈希函数
        return k % self.size  # 假设目前只支持整数

    def find(self, k):  # 哈希表的查找函数
        i = self.h(k)  # 先找到查找k元素的哈希值，是在i位置所在的链表
        return self.T[i].find(k)  # 返回哈希表i位置查找到的k元素

    def insert(self, k):  # 哈希表的插入函数
        i = self.h(k)  # 先计算插入k元素的哈希值，然后会插入到i位置
        if self.find(k):  # 如果找到了k，即哈希表中存在k，不插入
            print("Duplicated Insert")
        else:  # 如果没找到，可以插入
            self.T[i].append(k)  # 插入到i位置所在的链表


ht = HashTable()  # 创建一个HashTable对象
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)
print(ht.T)  # 打印这个哈希表
print(ht.find(3))
print(ht.find(102))
print(ht.find(508))
