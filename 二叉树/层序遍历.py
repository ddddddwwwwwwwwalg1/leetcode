def func(root):
    if root is None:
        return []
    que = []
    que.append(root)
    res = []
    while que:
        tmp = []
        size = len(que)
        for i in range(size):
            node = que[i]
            tmp.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        res.append(tmp)
    return res
