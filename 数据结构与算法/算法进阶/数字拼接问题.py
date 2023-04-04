from functools import cmp_to_key  # 传一个老式的cmp函数，会转换成key函数


def xy_cmp(x, y):
    if x + y < y + x:
        return 1  # 此时进行交换
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(l):
    l = list(map(str, l))  # 将l中的每一个元素都转化为字符串，然后将这些字符串放在列表里
    l.sort(key=cmp_to_key(xy_cmp))  # cpm=是python2中可以传的参数，是可以传两个参数的一个函数，返回一个它们的比较结果
    return "".join(l)  # 将排好序的l中的元素组合成一个字符串


l = [32, 94, 128, 1286, 6, 71]
print(number_join(l))


# 也可以使用冒泡排序的方法

def bubble_sort(l):
    l = list(map(str, l))  # 将l中的每一个元素都转化为字符串，然后将这些字符串放在列表里
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] + l[j + 1] < l[j + 1] + l[j]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return "".join(l)  # 将排好序的l中的元素组合成一个字符串


l = [32, 94, 128, 1286, 6, 71]
print(bubble_sort(l))
