def func(m,n,k):
    visited = set()

    def dfs(i,j):
        if i>=m:
            return 0
        if j>=n:
            return 0
        if (i,j) in visited:
            return 0
        sum_ = i%10 + i//10 + j%10 + j//10
        if sum_ >k:
            return 0
        visited.add((i,j))
        return 1+dfs(i+1,j)+dfs(i,j+1)

    return dfs(0,0)

