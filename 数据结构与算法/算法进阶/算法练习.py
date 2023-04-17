s = input()
d = ''  # 把s中的字符挑出来放到d中排序

for i in s:
    if i.isalpha():
        d = d + i
d = sorted(d, key=str.upper)  # 可以实现1）字符由A到Z的排序2）同字母（A与a算同字母），由输入先后顺序排列

ind = 0
f = ''  # 最终要输出的字符串

for i in s:
    if i.isalpha():  # 如果i是字符
        f = f + d[ind]
        ind += 1
    else:
        f = f + i
print(f)
