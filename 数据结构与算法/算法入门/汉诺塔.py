def hanoi(n, a, b, c):  # 定义ｎ个盘子，ａ、b、c三个柱子，
    if n > 0:  # 递归终止条件是n=0时，没有盘子，此时我们一步都不用移动

        hanoi(n - 1, a, c, b)  # 将n-1个盘子从a经过c移动到b
        print("moving from %s to %s" % (a, c))  # 把第n个盘子从a移动到c
        hanoi(n - 1, b, a, c)  # 把n-1个盘子从b经过a移动到c


hanoi(3, "A", "B", "C")
