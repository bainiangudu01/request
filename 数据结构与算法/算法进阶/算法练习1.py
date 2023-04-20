while True:
    try:
        m, n = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())
        x, y = int(input()), int(input())
        x3, y3 = map(int, input().split())
        print(0 if m <= 9 and n <= 9 else -1)
        print(0 if x1 < m and x2 < m and y1 < n and y2 < n else -1)
        print(0 if 9 > m > x else -1)
        print(0 if 9 > n > y else -1)
        print(0 if x3 < m and y3 < n else -1)
    except:
        break
