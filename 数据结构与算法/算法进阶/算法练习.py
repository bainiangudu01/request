ip=list(map(int,input().split('.')))
ip_10=int(input())
s=""
for i in ip:
    a=bin(i)[2:]
    if len(a)<=8:
        a='0'*(8-len(a))+a
        s+=a
print(int(s,2))

ip_2=bin(ip_10)[2:]
# print(ip_2)
if len(ip_2)<=32:
    ip_2='0'*(32-len(ip_2))+ip_2
l=[]
for i in range(0,len(ip_2),8):
    l.append(str(int(ip_2[i:i+8],2)))
print(".".join(l))

