class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 前序遍历 根左右
def func1(root):
    res = []
    def recur(root):
        if root is None:
            return
        res.append(root.val)
        recur(root.left)
        recur(root.right)
    recur(root)
    return res

# 中序遍历
def func2(root):
    res = []
    def recur(root):
        if root is None:
            return
        recur(root.left)
        res.append(root.val)
        recur(root.right)
    recur(root)
    return res

# 前序遍历，非递归
def func3(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return res



