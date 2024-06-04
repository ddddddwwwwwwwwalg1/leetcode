# def func(x, n):
#     def func1(n):
#         if n == 0:
#             return 1
#         y = func1(n//2)
#         if n % 2 == 1:
#             return y * y * x
#         else:
#             return y * y
#     return func1(n)
#
#
# print(func(2, 5))


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0, 1]
    for i in range(2, n + 1):
        tmp = dp[-1] + dp[-2]
        dp.append(tmp)
    return dp[-1]

def numWays(n: int) -> int:
    def f(n):
        if n==0:
            return 1
        if n==1:
            return 1
        return f(n-1) % 1000000007 + f(n-2) % 1000000007
    return f(n)


print(numWays(7))