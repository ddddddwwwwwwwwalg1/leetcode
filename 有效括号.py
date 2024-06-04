def func(s):
    l1 = ['{', '(', '[']
    l2 = ['}', ')', ']']
    stack = []
    for i in s:
        if i in l1:
            stack.append(l2[l1.index(i)])
        else:
            if not stack:
                return False
            else:
                tmp = stack.pop()
                if tmp != i:
                    return False
    if stack:
        return False
    return True

