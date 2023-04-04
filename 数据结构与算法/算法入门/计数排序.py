import random


def count_sort(l, max_count=10):  # 这个数范围最大是10，列表长度是11
    count = [0 for _ in range(max_count + 1)]  # 生成11个0的列表
    for val in l:
        count[val] = count[val] + 1
    l.clear()
    for ind, val in enumerate(count):  # count中有val个ind
        for i in range(val):
            l.append(ind)


l = [random.randint(0, 10) for _ in range(15)]
print(l)
count_sort(l)
print(l)
