import random

def insert_sort_gap(l, gap):  # gap参数是分的组，d是4时，gap就是4，把插入排序所有1改成gap
    for i in range(gap, len(l)):
        tmp = l[i]
        j = i - gap
        while j >= 0 and l[j] > tmp:
            l[j + gap] = l[j]
            j = j - gap
        l[j + gap] = tmp


def shell_sort(l):
    d = len(l) // 2
    while d >= 1:
        insert_sort_gap(l, d)
        d = d // 2


l = list(range(1000))
random.shuffle(l)
shell_sort(l)
print(l)
