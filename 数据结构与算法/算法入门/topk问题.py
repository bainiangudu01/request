import random


def sift(l, low, high):
    i = low
    j = 2 * i + 1
    tmp = l[low]
    while j <= high:
        if j + 1 <= high and l[j + 1] < l[j]:  # 后边>改成<，取两个孩子里更小的那一个
            j = j + 1
        if l[j] < tmp:  # 后边>改成<，此时建立的会是小根堆，孩子小于父亲，将孩子和父亲对调
            l[i] = l[j]
            i = j
            j = 2 * i + 1
        else:
            l[i] = tmp
            break
    l[i] = tmp


def topk(l, k):
    heap = l[0:k]  # 取出k个元素，然后建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)  # 建堆完成
    for i in range(k, len(l)):  # 把剩下的元素和堆顶对比
        if l[i] > heap[0]:
            heap[0] = l[i]  # 把数值heap[0]覆盖为l[i]，然后做一次调整
            sift(heap, 0, k - 1)
    for i in range(k - 1, -1, -1):  # 挨个出数
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


l = list(range(1000))
random.shuffle(l)
print(topk(l, 10))
