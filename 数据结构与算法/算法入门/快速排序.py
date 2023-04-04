def parition(l, left, right):  # partition接收3个参数，列表和要操作的列表的范围
    tmp = l[left]  # 将第一个数存起来，好让右边的数可以填过来，要写left不能写0，0写固定了后续不好移动
    while left < right:
        while left < right and l[right] >= tmp:  # 从右边开始循环找比tmp小的数，只要l[right]>=tmp，就继续往左找
            right = right - 1  # right往左走一位
        l[left] = l[right]  # 如果循环不成立，将右边的值放到左边空位上
        while left < right and l[left] <= tmp:  # 放完之后，右侧有空位，再从左侧找
            left = left + 1
        l[right] = l[left]  # 如果循环不成立，将左边的值放到右边空位上
    l[left] = tmp  # 循环结束后，left和right位置相等了，把tmp归位，这里写left和right都可以，和tmp = l[left]对照，一个拿出，一个归位
    return left  # 返回mid的值，此时left和right碰上了，返回谁都可以


def quick_sort(l, left, right):
    if left < right:  # 递归终止条件
        mid = parition(l, left, right)
        quick_sort(l, left, mid - 1)
        quick_sort(l, mid + 1, right)


l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(l)
quick_sort(l, 0, len(l) - 1)
print(l)

