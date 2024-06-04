## abcabcbb -> abc
# 滑动窗口
def func(s):
    lst = []
    res = 0
    for j in range(len(s)):
        while s[j] in lst:
            del lst[0]
        lst.append(s[j])
        res = max(res, len(lst))
    return res
