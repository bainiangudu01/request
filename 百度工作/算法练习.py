while True:
    try:
        s = input()
        if len(s) <= 8:
            print("NG")
        else:
            upp, low, dig, sym = 0, 0, 0, 0
            for i in s:
                if i.upper():
                    upp = 1
                elif i.lower():
                    low = 1
                elif i.isdigit():
                    dig = 1
                elif i.isascii():
                    sym = 1
            if upp + low + dig + sym < 3:
                print("NG")
            else:
                for i in range(len(s) - 3):
                    if len(s.split(s[i:i + 3])) >= 3:
                        print("NG")
                        print("NG")
                        break
                else:
                    print("OK")




    except:
        break
