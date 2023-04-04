# 冒泡排序
import random  # 导入随机模块，下边的是算法，这个只是为了生成随机的列表进行验证

def bubble_sort(l):
    for i in range(len(l) - 1):  # i是趟的运行，总共会运行n-1趟
        for j in range(len(l) - i - 1):  # j是箭头的运行，箭头会从索引0开始，运行到n-i-1的位置
            if l[j] > l[j + 1]:  # 如果箭头指向的数大于后边的数（将>换成<会变成降序）
                l[j], l[j + 1] = l[j + 1], l[j]  # 将两个数进行交换

# 使用random模块的randint生成0-10000的随机整数，用列表生成式生成列表长度为1000的列表
l = [random.randint(0, 10000) for i in range(1000)]
print(l)  # 打印开始生成的列表
bubble_sort(l)
print(l)  # 打印排序之后的列表

# 优化后冒泡排序
def bubble_sort(l):
    for i in range(len(l) - 1):
        exchange = False  # 在第i趟时加一个标志位，刚开始为False
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                exchange = True  # 如果交换了，就将它置为True
        print(l)  # 打印每趟交换之后的列表
        if not exchange:  # 如果一趟结束没有进行交换，此时exchange依旧为False，就结束这个代码
            return

l = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print(l)  # 打印开始生成的列表
bubble_sort(l)