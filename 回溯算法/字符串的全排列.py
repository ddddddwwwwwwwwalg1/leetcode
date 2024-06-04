def func(s):
    res = []
    path = []
    use_list = [False] * len(s)
    def backtrack(s,used_list):
        if len(path)==len(s):
            res.append(''.join(path[:]))
            return
        for i in range(0,len(s)):
            if use_list[i] == True:
                continue
            use_list[i] = True
            path.append(s[i])
            backtrack(s,used_list)
            path.pop()
            use_list[i] = False
    backtrack(s,use_list)
    return res


