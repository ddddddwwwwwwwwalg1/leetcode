def func(graph):
    cities = len(graph)
    isVisited = set()

    def dfs(i):
        for j in range(cities):
            if graph[i][j] == 1 and j not in isVisited:
                isVisited.add(j)
                dfs(j)
    p = 0
    for i in range(cities):
        if i not in isVisited:
            dfs(i)
            p += 1
    return p


