def lcs_length(x, y):  # 计算最长公共子序列长度函数
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 对应的二维列表，x、y洲都从0开始，空序列，x和y第一行列都是0已填充好
    for i in range(1, m + 1):  # 0行0列都已填充完，填充其他行列，故都从1开始
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # 如果x和y字符串最后一位相同
                c[i][j] = c[i - 1][j - 1] + 1  # 对应表上左上方+1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    # for _ in c:  # 可以让列表c逐行打印，非一行打印出来
    #     print(_)
    return c[m][n]


print(lcs_length('ABCDDAB', 'BDCABA'))


def lcs(x, y):  # 记录是来自左上、上、左方向的函数，是一个回溯
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # b和c是一样的，c记录的是数字，b记录的是箭头，1：左上方 2：上方 3：左方
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):  # 0行0列都已填充完，填充其他行列，故都从1开始
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # 如果x和y字符串最后一位相同，说明这个值对应表上左上方+1
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # 1代表左上方
            elif c[i - 1][j] > c[i][j - 1]:  # 来自于上方，x代表的是行，对照图来看,可以加个等号
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:  # 来自于左方
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    # for _ in b:
    #     print(_)
    return c[m][n], b

print(lcs('ABCDDAB', 'BDCABA'))


def lcs_traceback(x, y):  # 输出最长公共子序列函数
    c, b = lcs(x, y)
    i = len(x)  # 从最后一个位置往前走
    j = len(y)
    l = []
    while i > 0 and j > 0:  # 有一个等于0的就停止
        if b[i][j] == 1:  # 如果这个位置是来自左上方的，就说明这个位置两个字符串是匹配的
            l.append(x[i - 1])  # 把这个位置的值存到l列表里，y[j-1]也可以，两个值是一样的
            i = i - 1  # i，j同时减1表示往左上方走
            j = j - 1
        elif b[i][j] == 2:  # 来自上方，不匹配的，不append了
            i = i - 1  # 往上走
        else:  # 表示来自左方，不匹配的
            j = j - 1  # 往左走
    return "".join(reversed(l))  # 返回倒序的l，并将l合并为一个字符串


print(lcs_traceback('ABCDDAB', 'BDCABA'))
