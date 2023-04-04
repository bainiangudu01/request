from 时间计算装饰器 import cal_time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod_recurision_1(p, n):  # 左右都切割，递归写法
    if n == 0:  # 如果钢条长度是0，返回0
        return 0
    else:
        # 公式：r_n=max(p_n，r_1+r_n-1，r_2 +r_n-2，......，r_n-1+r_1)
        res = p[n]
        for i in range(1, n):  # i取值为1到n-1
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n - i))
        return res


@cal_time
def c1(p, n):
    return cut_rod_recurision_1(p, n)


def cut_rod_recurision_2(p, n):  # 左边不切割，右边切割递归写法，函数就是求rn的
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max((res, p[i] + cut_rod_recurision_2(p, n - i)))
        return res


@cal_time
def c2(p, n):
    return cut_rod_recurision_2(p, n)


# print(c1(p, 15))
# print(c2(p, 15))

@cal_time
def cut_rod_dp(p, n):  # 自底向上实现，使用左侧不切割，右侧切割公式
    r = [0]  # 每个子问题只求解一次，保存求解结果，需要开个列表，刚开始长度为0时，表里只有一个元素0
    for i in range(1, n + 1):  # 要求rn的话需要循环n次，每一个r1,r2都要算出来保存到列表上，循环的i就是公式里的n
        res = 0  # res初始为0，即j为0时res为0，所以下边从1开始循环
        for j in range(1, i + 1):  # 循环的j就是公式里的i
            res = max(res, p[j] + r[i - j])  # p[j]+r[i-j]就是原来的p[i]+r[n-i]，这里不用递归，直接从表里取
        r.append(res)
    return r[n]


# print(c2(p, 20))
# print(cut_rod_dp(p, 20))


def cut_rod_extend(p, n):  # 重构解，输出最优切割方案
    r = [0]
    s = [0]  # s是切割一次时保存的左边切下的长度，刚开始是0
    for i in range(1, n + 1):
        res_r = 0  # 用来记录价格的最大值
        res_s = 0  # 价格最大值对应方案的左边不切割的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:  # 如果这个值要大于res_r的值
                res_r = p[j] + r[i - j]  # res_r的值更新为这个值
                res_s = j  # res_s更新为j
        r.append(res_r)  # 循环结束后更新两个列表
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []  # 最后的方案
    while n > 0:  # 切割的最后一段会变成0
        ans.append(s[n])
        n = n - s[n]  # 左边切割后，去掉，剩下右边再对应s表里左边切割的，直到n=0
    return r, ans

print(cut_rod_solution(p, 20))
