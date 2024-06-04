def func(n, k):
    res = []
    path = []
    def backtrack(start):
        if len(path)==k:
            res.append(path[:])
            return
        for i in range(start,n+1):
            path.append(i)
            backtrack(i+1)
            path.pop()
    backtrack(0)
    return res


print(func(4,2))