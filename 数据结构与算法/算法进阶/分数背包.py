goods = [(60, 10), (120, 30), (100, 20)]  # 定义成字典也可以
goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # 按照价格/重量降序排列
print(goods)


def fractional_backpack(goods, w):  # goods是商品
    m = [0 for i in range(len(goods))]  # m表示每个商品拿走几个，此时m是对照排序后的goods
    total_v = 0  # 拿走商品的总价值
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1  # 拿走全部
            total_v = total_v + price
            w = w - weight
        else:
            m[i] = w / weight  # 拿走一部分，此时背包就满了
            total_v = total_v + m[i] * price
            w = 0
            break
    return m, total_v


print(fractional_backpack(goods, 50))
