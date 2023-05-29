s = input()
s1 = ''
for i in s:
    if i.isalpha():
        s1 += i
s1 = sorted(s1, key=str.upper)

ind = 0
res = ''
for i in s:
    if i.isalpha():
        res += s1[ind]
        ind += 1
    else:
        res += i
print(res)