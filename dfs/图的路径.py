def func(graph):
    res = []
    stack = []
    def dfs(i):
        if i == len(graph)-1:
            res.append(stack[:])
            return
        for j in graph[i]:
            stack.append(j)
            dfs(j)
            stack.pop()
    stack.append(0)
    dfs(0)
    return res



