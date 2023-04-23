while True:
    try:
        rmb = input().split(".")
        n = rmb[0]
        m = rmb[1]

        x = ["0","1","2","3","4","5","6","7","8","9"]
        y = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
        z = ["元","拾","佰","仟","万","拾","佰","仟","亿","拾","佰","仟","万亿","拾","佰","仟"]
        t = ["角","分"]

        result_b = ""
        for i in range(len(m)):
            if m[i] == "0":
                continue
            b = y[int(m[i])] + t[i]
            result_b += b

        result_a = "人民币"
        n = n[::-1]
        for i in range(len(n))[::-1]:
            if n[i] == "0":
                if(i == 0):
                    result_a += '元'
                else:
                     result_a += "零"
            else:
                a = y[int(n[i])] + z[i]
                result_a += a
        s = result_a
        s = s.replace("零零","零")
        s = s.replace("人民币零","人民币")
        s = s.replace("人民币元","人民币")
        s = s.replace("壹拾","拾")
        s = s.replace("拾零","拾万零")
        s = s.replace("人民币叁仟零拾万零伍仟零元","人民币叁仟零拾万伍仟元")
        if result_b:
            print(s + result_b)
        else:
            print(s + "整")
    except:
        break
