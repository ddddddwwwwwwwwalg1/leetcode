# 归并排序思想
def partition(left, right, nums):

    if left == right:
        return nums[left]

    mid = (left + right)//2
    part1 = partition(left, mid, nums)
    part2 = partition(mid+1, right, nums)
    return merge(part1, part2)

def merge(list1, list2):
    p1 = 0
    p2 = 0
    m = len(list1)
    n = len(list2)
    res = []
    while p1 <= m-1 and p2 <= n-1:
        if list1[p1] <= list2[p2]:
            res.append(list1[p1])
            p1 += 1
        else:
            res.append(list2[p2])
            p2 += 1
    while p1 <= m-1:
        res.append(list1[p1])
        p1 += 1
    while p2 <= n-1:
        res.append(list2[p2])
        p2 += 1
    return res

