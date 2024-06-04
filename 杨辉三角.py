def func(n):
    res = [[1]]

    for i in range(1,n):
        tmp1 = res[-1] + [0]
        tmp2 = [0] + res[-1]
        res.append([tmp1[j] + tmp2[j] for j in range(len(tmp1))])
    return res


print(func(3))