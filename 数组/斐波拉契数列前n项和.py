#
def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    dp = [0,1]
    res = 0
    for i in range(2,n):
        tmp = dp[i-1] + dp[i-2]
        res += tmp
        dp.append(tmp)
    return res

def func2(n):
    def func1(n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        return func1(n-1)+func1(n-1)-func1(n-2) + func1(n-2)-func1(n-3)
    return func1(n)

print(func2(5))


