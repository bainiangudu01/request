while True:
    try:
        ip = input()  # ip地址
        num = input()  # 10进制ip地址
    except:
        break
    else:
        # ip to num
        ip_list = ip.split('.')  # 列表
        ip2num = str()
        for i in ip_list:
            a = bin(int(i, 10))[2:]
            a = '0' * (8 - len(a)) + a if len(a) < 8 else a
            ip2num += a
        print(int(ip2num, 2))

        # num to ip
        num2ip = []
        num2 = bin(int(num, 10))[2:]
        num2 = '0' * (32 - len(num2)) + num2 if len(num2) < 32 else num2
        for i in range(4):
            b = num2[8 * i:8 * i + 8]
            b = str(int(b, 2))
            num2ip.append(b)
        print('.'.join(num2ip))
