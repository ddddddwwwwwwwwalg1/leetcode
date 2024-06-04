def func(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
        

# def func(graph):
#
#     m = len(graph)
#     n = len(graph[0])
#
#     def dfs(i,j):
#         res = 1
#         if i>=m or j>=n or graph[i][j]==0:
#             return 0
#         res += dfs(i-1,j)+dfs(i+1,j)+dfs(i,j+1)+dfs(i,j-1)
#         return res
#
#     ans =
#
# def func():
#     isVisited = set()
#
#     def dfs(i):
#         for j in cities:
#             if graph[i,j]==1 and j is not in isVisited:
#                 isVisited.add(j)
#                 dfs(j)



