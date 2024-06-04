def func(x):
    res = []
    while x != 0:
        tmp = x % 10
        res.append(tmp)
        x = x//10
    return res == res[::-1]


print(func(121))