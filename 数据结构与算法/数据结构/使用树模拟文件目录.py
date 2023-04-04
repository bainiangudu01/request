class Node:  # 树是由一堆节点组成的
    def __init__(self, name, type='dir'):
        self.name = name  # 节点的名字，就是文件/文件夹的名字
        self.type = type  # 文件的类型，是文件夹dir还是文件file，可以设置默认是文件夹
        self.children = []  # 文件夹下边是否还有文件夹，这里不是next，因为文件夹下边可以有好多文件夹，可以用列表表示
        self.parent = None  # 文件/文件夹的父目录，只能有一个，有些像双链表，链式存储

    def __repr__(self):  # 直接查看对象的时候调用repr方法，不然会返回object对象
        return self.name  # 只返回节点的名字


# n = Node('hello')
# n2 = Node('world')
# n.children.append(n2)  # 将n文件夹和n2文件夹连起来
# n2.parent = n  # 文件夹下子文件夹可以有很多，但父文件夹只能有一个

class FileSystemTree:
    def __init__(self):
        self.root = Node('/')  # 刚开始需要维护树/目录根节点，type默认是dir
        self.now = self.root  # 刚开始未创建新文件夹时就在根目录里

    def mkdir(self, name):  # 在当前目录创建一个目录，name是一个文件夹的名字
        if name[-1] != '/':  # 如果目录名字的最后一个字符不是'/'，即不是文件夹的形式
            name = name + '/'  # 就将name加上一个'/'，变成文件夹的形式
        node = Node(name)  # 创建这个文件夹节点，然后和现在的文件夹连起来
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):  # 展示当前目录下的所有子目录
        return self.now.children

    def cd(self, name):  # 切换目录，有相对路径和绝对路径，先写一个只支持相对路径的
        if name[-1] != '/':
            name = name + '/'
        if name == '../':
            self.now = self.now.parent
            return
        for child in self.now.children:  # 遍历当前目录的子目录
            if child.name == name:  # 如果子目录中有cd传进的目录
                self.now = child  # 就切换当前目录
                return  # 搜到之后结束一下，不要再往下搜了，不然会报错
        raise ValueError('invalid dir')  # for循环没有搜到才执行，搜到了return中断循环就不会执行
    # else子语句是在循环体正常结束时才执行的语句，当循环被中断时不执行，当遇到break、return和有异常发生时都会中断循环


tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('user/')
tree.cd('bin/')
tree.mkdir('python/')  # 此时会在bin目录下创建python目录
tree.cd('../')  # 此时又切换会bin目录上一个目录，即根目录
print(tree.root.children)
print(tree.ls())
