def func(x):
    res = 0
    while x!=0:
        tmp = x%10
        res = res*10 + tmp
        x = x // 10
        print(x)
    return res


print(func(123))
