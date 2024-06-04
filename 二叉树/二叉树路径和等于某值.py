def func(root,target):

    stack = []
    path_stack = []

    stack.append(root)
    path_stack.append([root.val])

    res = []
    while stack:
        node = stack.pop()
        path = path_stack.pop()

        if node.left is None and node.right is None and sum(path)==target:
            res.append(path)

        if node.right:
            stack.append(node.right)
            path_stack.append(path+[node.right.val])
        if node.left:
            stack.append(node.left)
            path_stack.append(path+[node.left.val])

    return res

