class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            if abs(left-right)<=1:
                return max(left,right)+1
            else:
                return -1
        if dfs(root)==-1:
            return False
        else:
            return True