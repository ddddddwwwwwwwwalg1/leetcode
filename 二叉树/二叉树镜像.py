def func(root):
    if not root:
        return None
    queue = [root]
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
    return root
