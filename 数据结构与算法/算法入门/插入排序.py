def insert_sort(l):
    for i in range(1, len(l)):  # 刚开始手里有一张牌，索引为0，所以开始摸牌时从1开始，到索引为n-1的位置，此时i表示摸到的牌的下标
        tmp = l[i]  # 用一个变量存储我摸到的牌
        j = i - 1  # j指的是手里的牌的下标
        while j >= 0 and l[j] > tmp:  # 如果我手里的牌比摸到的牌大
            l[j + 1] = l[j]  # 把j手里的牌往右移
            j = j - 1  # 再把j手里的牌指向的箭头往左移动一个
        l[j + 1] = tmp  # 不满足循环时，将摸到的牌放到j的牌的右侧
    return l  # 返回排好序的牌


l = [3, 2, 4, 1, 5, 7, 9, 6, 8]
print(insert_sort(l))
