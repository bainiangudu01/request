import time

# 时间戳
a = time.localtime(1680147595794 / 1000)
b = time.strftime("%Y-%m-%d %H:%M:%S", a)
print(a)

