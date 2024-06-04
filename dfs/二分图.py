##[[1,3],[0,2],[1,3],[0,2]] true

def func(graph):

    colors = [-1 for i in range(len(graph))]

    def dfs(i, cur_color):

        colors[i] = cur_color

        for j in graph[i]:
            if colors[j] == cur_color:
                return False
            elif colors[j] == 1-cur_color:
                continue
            else:
                dfs(j, 1-cur_color)
        return True

    n = len(graph)

    for i in range(n):
        if colors[i] == -1:
            dfs(i,0)
    return True