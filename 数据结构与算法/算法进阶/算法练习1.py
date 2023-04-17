n = int(input())
weight = list(map(int, input().split()))
num = list(map(int, input().split()))

l = []
se = {0, }

for i in range(n):
    for j in range(num[i]):
        l.append(weight[i])

for i in l:
    for j in list(se):
        se.add(i + j)
print(len(se))
