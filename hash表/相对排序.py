def func(nums1,nums2):
    rank = {}
    for x,y in enumerate(nums2):
        rank[y] = x

    def custom_sort(i):
        if i in rank:
            return (0,rank[i])
        else:
            return (1,i)

    nums1.sort(key=custom_sort)
    return nums1


def func(root):

    paths = []
    nodes = []

    paths.append([root.val])
    nodes.append(root)

    res = []

    while nodes:
        node = nodes.pop()
        path = paths.pop()

        if node.left is None and node.right is None:
            res.append(path)

        if node.right:
            nodes.append(node.right)
            paths.append(path+[node.right.val])
        if node.left:
            nodes.append(node.left)
            paths.append(path+[node.left.val])

    return res