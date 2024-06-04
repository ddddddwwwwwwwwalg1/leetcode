def func(graph):
    m = len(graph)
    n = len(graph[0])

    def dfs(i,j):
        if graph[i][j] == 0 or i<0 or j<0 or i>=m or j>=n:
            return 0

        res = 1
        graph[i][j] = 0
        res = res+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
        return res
    ans = 0

    for x in range(m):
        for y in range(n):
            ans = max(dfs(x,y),ans)
    return ans


def func(nums):

    nums.sort()

    n = len(nums)

    for i in range(n-2):

        if nums[i]>0:
            break
        if nums[i]==nums[i+1]:
            continue

        j = i+1
        k = n-1

        while