import random


def bucket_sort(l, n=5, max_num=1000):  # n是分成多少个桶，max_num是这些数的最大值
    buckets = [[] for _ in range(n)]  # 创建桶，大桶是一个列表，大桶中包含小桶，小桶又是一个列表
    for var in l:
        # i表示var应该放到几号桶里，对var // (max_num // 5), n - 1取最小值，避免最大数字越界
        i = min(var // (max_num // 5), n - 1)
        buckets[i].append(var)  # 把var放到对应的桶里
        for j in range(len(buckets[i]) - 1, 0, -1):  # 保持桶内的顺序，对桶里的元素进行反向冒泡排序，j是指针
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]  # 交换
            else:
                break
    l_new = []  # 接收桶内的有顺序的元素
    for buc in buckets:
        l_new.extend(buc)  # 把小桶的列表加入到l_new中
    return l_new


l = [random.randint(0, 1000) for i in range(10)]
print(l)
print(bucket_sort(l))
