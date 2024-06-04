def func(root,k):
    res = []
    def dfs(root):
        if not root:
            return
        dfs(root.right)
        res.append(root.val)
        dfs(root.left)
    dfs(root)
    return res[k]
