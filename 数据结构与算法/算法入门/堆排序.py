import random


def sift(l, low, high):  # 堆的向下调整函数，此时左右都已经是堆，high是堆的最后一个元素位置，low最开始是根节点位置
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = l[low]  # 拿出堆顶存起来
    while j <= high:  # j的位置不能超过high，避免下标越界
        if j + 1 <= high and l[j + 1] > l[j]:  # 如果有有右孩子，且右孩子大于左孩子
            j = j + 1  # 把j指向右孩子，此时j指向的是两个孩子里更大的数
        if l[j] > tmp:  # 如果j更大，j要上去，和i调换位置
            l[i] = l[j]  # 把j放到i的位置上
            i = j  # i等于原来的j
            j = 2 * i + 1  # j往下挪一层
        else:  # tmp更大，把存起来的堆顶放回去
            l[i] = tmp
            break
    l[i] = tmp  # 循环跳出，如果j>high，下标越界了，此时没有实际的j和i比，依旧把存起来的堆顶放回去


def heap_sort(l):  # 堆排序，先建堆
    n = len(l)
    # n-1是最后一个元素下标，(n-1-1）//2是它的父节点，从它到0是所有的父节点，右不包所以为-1，倒序步长为-1
    for i in range((n - 2) // 2, -1, -1):  # i表示建堆的时候调整的部分的根的下标
        sift(l, i, n - 1)  # 让这个high一直指向最后一个元素，这个不是递归，调用的不是自身
    # 上边循环结束后建堆完成，接着挨个出数，拿掉堆顶
    for i in range(n - 1, -1, -1):  # 此时i一直指的是当前堆的最后一个位置
        l[0], l[i] = l[i], l[0]  # 交换堆顶和最后一个位置
        sift(l, 0, i - 1)  # 再将堆进行调整，i-1是新的high


l = [i for i in range(100)]
random.shuffle(l)  # 打乱这个列表
print(l)
heap_sort(l)
print(l)
