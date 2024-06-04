## 22/3 = 7， 用减法代替除法

def func(a,b):
    sign = 1
    if (a>0 and b<0) or (a<0 and b>0):
        sign = -1
    if a<0:
        a = -a
    if b<0:
        b = -b
    res = 0
    while b <= a:
        a -= b
        res += 1
    if sign == 1:
        return res
    else:
        return -res


print(func(22,3))