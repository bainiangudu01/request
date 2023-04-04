p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
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