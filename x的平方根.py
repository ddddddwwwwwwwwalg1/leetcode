## 牛顿法

def func(n):
    x = n
    while abs(x * x - n) > 0.01:
        print(x)
        x = (n+x*x)/(2*x)
    return int(x)

print(func(8))