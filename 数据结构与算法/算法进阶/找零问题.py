t = [100, 50, 20, 5, 1]  # 有的钱币的面额,是排好序的，没排好先排一下


def change(t, n):
    m = [0 for _ in range(len(t))]  # 找零的张数，对应钱币的面额，每个面额找几张，刚开始都是0
    for i, money in enumerate(t):
        m[i] = n // money  # 对应面额的张数
        n = n % money
    return m, n  # 返回m列表和剩余的钱数


print(change(t, 376))
