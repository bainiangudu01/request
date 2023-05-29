import time


# 时间戳
a = time.localtime( 1684563067372 / 1000)
b = time.strftime("%Y-%m-%d %H:%M:%S", a)
print(a)

# 1684638217610
# 1684724690325
# 1684551659248