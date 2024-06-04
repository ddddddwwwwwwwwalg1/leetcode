def func(a,b):
    i = len(a)-1
    j = len(b)-1
    res = []
    carry = 0
    while i>=0 or j>=0:
        if i>=0:
            carry += ord(a[i]) - ord("0")
        if j>=0:
            carry += ord(b[j]) - ord("0")
        res.append(carry%2)
        carry = carry // 2
        i -= 1
        j -= 1
    if carry == 1:
        res.append(1)
    return "".join(res[::-1])
