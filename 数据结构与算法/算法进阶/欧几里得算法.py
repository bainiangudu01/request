def gcd(a, b):  # 伪递归写法，只有递，没有归
    if b == 0:  # 终止条件是b=0时
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 16))


def gcd_2(a, b):
    while b > 0:
        r = a % b  # 记录一下a%b的值
        a = b  # 然后a的位置变成b
        b = r  # b的位置变成r的值
    return a  # 最后返回a位置的值


print(gcd_2(12, 16))
