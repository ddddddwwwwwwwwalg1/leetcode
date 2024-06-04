## 判断是否对称二叉树
def func(root):
    if root is None:
        return True
    que = [root.left, root.right]
    while que:
        left = que.pop(0)
        right = que.pop(0)
        if not left and not right:
            continue
        if left is None or right is None or left.val!=right.val:
            return False
        que.append(left.left)
        que.append(right.right)
        que.append(left.right)
        que.append(right.left)
    return True
