## s = "adcbbcd" hash表

def func(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] = 0
        else:
            d[s[i]] = 1
    for i in range(len(s)):
        if d[s[i]]==1:
            return s[i]


print(func("adcbbcd"))