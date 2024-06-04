def func(root):
    if not root:
        return 0
    queue = [root]
    res = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if node.left is None and node.right is None:
                return res
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        res += 1
    return res