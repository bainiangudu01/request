while True:
    try:
        m, n = map(int, input().split())
        # 初始化表格
        if m <= 9 and n <= 9:
            print(0)
            l = [[0 for i in range(n)] for i in range(m)]
        else:
            print(-1)

        # 交换
        x1, y1, x2, y2 = map(int, input().split())
        if (x1 in range(m) and x2 in range(m)) and (y1 in range(n) and y2 in range(n)):
            l[x1][y1], l[x2][y2] = l[x2][y2], l[x1][y1]
            print(0)
        else:
            print(-1)
        # 插入行
        x = int(input())
        l.insert(x, [0 for i in range(n)])
        if len(l) > 9:
            print(-1)
        else:
            print(0)
            l.pop()
        # 插入列
        y = int(input())
        if n==9 or y>=n:
            print(-1)
        else:
            for i in range(m):
                l[i].insert(y, 0)
            for i in range(m):
                if len(l[i]) > 9 or len(l[i]) > n + 1:
                    print(-1)
                    break
                else:
                    print(0)
                    for i in range(m):
                        l[i].pop()
                    break
        # 查询
        x, y = map(int, input().split())
        if x <= m - 1 and y <= n - 1:
            print(0)
        else:
            print(-1)
    except:
        break
# 7 3
# 2 2 4 0
# 4
# 4
# 6 2
