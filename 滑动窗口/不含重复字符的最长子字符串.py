def func(s):

    res = []
    length = 1
    for j in range(len(s)):
        while s[j] in res:
            res.pop(0)
        res.append(s[j])
        length = max(length, len(res))
    return length
