import time

# 时间戳
a = time.localtime(1680147595794 / 1000)
b = time.strftime("%Y-%m-%d %H:%M:%S", a)
print(a)

# # 追加文件内容
# path = "C:/Users/13792/Desktop/下载内容/mlm.bin"
# with open(path, mode="wb") as f:
#     f.write(b"abcd")
