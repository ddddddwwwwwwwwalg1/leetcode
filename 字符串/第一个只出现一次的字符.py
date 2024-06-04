def func(s):
    d = {}

    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] = 0
    for i in s:
        if d[i]:
            return i
    return ''


print(func('abaccdeff'))