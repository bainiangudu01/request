s = """
100
100
125
125
125
"""

l = s.split("\n")
result = []
for i in l:
    try:
        a = float(i)
        result.append(a)
    except:
        pass
result.sort()

print(sum(result[1:-1])/3)