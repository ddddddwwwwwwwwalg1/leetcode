# 输入: g = [2,3,4], s = [1,2,3,4] s饼干 g人需求

def func(g,s):
    g.sort()
    s.sort()
    res = 0
    for i in range(len(s)):
        if res<len(g) and s[i] >= g[res]:
            res += 1
    return res