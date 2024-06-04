import collections

def func(nums, n):

    d1 = collections.defaultdict(list)
    d2 = {}

    res = []
    stk = []

    for v in nums:
        d1[v[1]].append(v[0])
        # 入度
        d2[v[0]] += 1

    for i in range(n):
        if d2[i] == 0:
            stk.append(i)

    while stk:
        for _ in stk:
            p = stk.pop()
            res.append(p)
            for j in d1[p]:
                d2[j] -= 1
                if d2[j] == 0:
                    stk.append(j)
    return res