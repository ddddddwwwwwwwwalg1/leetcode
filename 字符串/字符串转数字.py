print(ord('2')-ord('0'))

def func(s):
    s = s.strip()
    i = 0
    sign = 1
    if s[0] == '-':
        i = 1
        sign = -1
    res = 0
    for j in range(i,len(s)):
        res = res * 10 + ord(s[j]) - ord('0')
    return res * sign


print(func('-42'))