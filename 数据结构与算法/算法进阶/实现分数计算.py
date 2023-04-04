class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)  # x是最大公约数
        self.a = self.a / x  # 对a约分
        self.b = self.b / x  # 对b约分

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):  # 最小公倍数=最大公约数*（a/最大公约数）*（b/最大公约数）
        x = self.gcd(a, b)
        return a * b / x  # 最小公倍数简化了

    def __add__(self, other):  # 加法
        a = self.a  # 要算a/b+c/d
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)


f = Fraction(30, 16)
print(f)
a = Fraction(1, 3)  # 1/3
b = Fraction(1, 2)  # 1/2
print(a + b)
