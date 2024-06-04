def func(root1,root2):

    def helper(A,B):

        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return helper(A.left,B.left) and helper(A.right,B.right)

    return helper(root1,root2) or func(root1.left, root2) or func(root1.right, root2)