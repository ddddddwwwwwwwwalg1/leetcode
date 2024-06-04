yfrom collections import deque


class Solution:
    """二叉树的所有路径 迭代法"""

    def binaryTreePaths(self, root):
        # 题目中节点数至少为1
        stack, path_st, result = deque([root]), deque(), []
        path_st.append(str(root.val))

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result