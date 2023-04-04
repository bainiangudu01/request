# 顺序查找
def liner_serch(l, a):  # l是输入的一个列表，a是待查找的元素
    for ind, i in enumerate(l):  # ind是下标index，i是这个下标的值
        if i == a:  # 如果i等于我们要找的值a
            return ind  # 那就返回它的下标
    return  # 如果找完列表l，没有找到，返回的是None


# 二分查找
def binary_serch(l, a):
    left = 0  # 初始索引
    right = len(l) - 1  # 结束索引
    while left <= right:  # 如果left<=right,说明候选区有值
        mid = (left + right) // 2  # 如果left<=right,中间位置的索引mid=(left+right)//2
        if l[mid] == a:  # 如果mid索引位置的值等于a，说明找到了
            return mid  # 返回此时的索引
        elif l[mid] > a:  # 如果mid索引位置的值大于a，说明待查找的值在mid左侧
            right = mid - 1  # 将right移动到mid-1的位置（因为mid也不是，所以移动到mid左侧一位）
        else:  # 此时也就是l[mid]<a，说明待查找的值在mid的右侧
            left = mid + 1
    else:
        return None  # 如果循环完没有找到，返回None


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liner_serch(l, 3))
print(binary_serch(l, 3))
