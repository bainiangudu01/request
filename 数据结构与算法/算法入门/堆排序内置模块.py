import heapq
import random

l = list(range(100))
random.shuffle(l)
print(l)
heapq.heapify(l)  # 相当于建堆的过程，建的是小根堆
for i in range(len(l)):
    heapq.heappop(l)  # 相当于每次弹出顶端的最小元素，如果排序，每次把弹出的存到一个新列表里就行
