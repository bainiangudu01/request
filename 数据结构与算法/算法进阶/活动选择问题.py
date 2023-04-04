activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
activities.sort(key=lambda x: x[1])  # x是列表里的每一个元组，按照元组索引1结束时间进行排序


# 保证活动是按照结束时间排好序的
def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 如果a[i]中的开始时间大于等于res中最后一个活动的结束时间，就不冲突
            res.append(a[i])
    print(res)


activity_selection(activities)
