## hello world --> world hello

def func(strings):
    strings = strings.strip()
    i = len(strings)-1
    j = len(strings)-1
    res = []
    while i >= 0:
        while i>=0 and strings[i] != ' ':
            i -= 1
        res.append(strings[i+1:j+1])
        while strings[i]==' ':
            i -= 1
        j = i
    print(res)
    return ' '.join(res)


print(func("hello world"))


