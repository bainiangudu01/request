def fibnacci(n):  # 递归版本
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


print(fibnacci(100))


def fibnacci_no_recurision(n):  # 非递归版本
    f = [0, 1, 1]  # 首先建个列表，第一项是1，第二项是1，为了保持下标一致，加个第0项是0，接下来要求第n项
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    print(f[n])


fibnacci_no_recurision(100)
# 1、递归会使子问题进行重复计算，如斐波那契5=斐波那契4+斐波那契3，斐波那契4=斐波那契3+斐波那契2，递归每一次都要求斐波那契3
# 2、所以递归执行效率低，所以递归版本运行很慢
