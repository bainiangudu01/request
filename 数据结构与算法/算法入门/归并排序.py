import random


def merge(l, low, mid, high):  # 归并函数，假设此时左右两个列表是有序的，low是列表开始索引，mid是中间索引，high是结束索引
    i = low  # 先将i指向第一段第一个元素
    j = mid + 1  # 将j指向第二段的第一个元素
    l_tmp = []  # 临时列表，用来放拿出来的值
    while i <= mid and j <= high:  # i和j不能超过各自列表的末端，即左右两边都有数
        if l[i] < l[j]:
            l_tmp.append(l[i])
            i = i + 1
        else:
            l_tmp.append(l[j])
            j = j + 1
    # while执行完，左右列表肯定有一部分没数了
    while i <= mid:  # 如果左边有数，将左边剩下的数加到列表中
        l_tmp.append(l[i])
        i = i + 1
    while j <= high:  # 如果右边有数，将右边剩下的数加到列表中，两个while只会执行一个
        l_tmp.append(l[j])
        j = j + 1
    l[low:high + 1] = l_tmp  # 将新的l_tmp在写回l中
    return l


def merge_sort(l, low, high):
    if low < high:  # 列表中至少会有两个元素，递归
        mid = (low + high) // 2
        merge_sort(l, low, mid)  # 将左边合并，排好序
        merge_sort(l, mid + 1, high)  # 将右边合并，排好序
        merge(l, low, mid, high)  # 合并左右，排好序
        print(l[low:high+1])


l = list(range(30))
random.shuffle(l)
print(l)
merge_sort(l, 0, len(l) - 1)
print(l)
