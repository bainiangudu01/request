import random


# 比如最大是19，先根据个位决定放进哪个桶里，然后将桶放进列表里，再根据十位决定放进哪个桶里，然后将桶放进列表里
# 此时已完成排序
def radix_sort(l):
    max_num = max(l)  # 如果最大数是99，需要放到桶里2次；是10000，需要放到桶里5次
    it = 0  # it=0时表示先取个位放到桶里
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 个位、十位都有10个数，固定分10个桶
        for var in l:  # 将l中元素取出，放到哪个桶中
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)  # 循环结束后，分桶完成
        l.clear()  # 清空原来的列表
        for buc in buckets:
            l.extend(buc)  # 然后把分好类的桶放回l中
        it = it + 1


l = list(range(19))
random.shuffle(l)
print(l)
radix_sort(l)
print(l)
