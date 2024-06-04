def func(s,t):

    need = dict()
    for i in t:
        if i not in need:
            need[i] = 1
        else:
            need[i] += 1

    needCount = len(t)
    i = 0
    res = (0,10000)
    for j in range(len(s)):
        if need[s[j]] > 0:
            needCount -= 1
        need[s[j]] -= 1
        if needCount == 0:
            while True:
                c = s[i]
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            if res[1]-res[0] > j-i:
                res = (j,i)
            need[s[i]] += 1
            needCount += 1
            i+=1
    return s[res[0]:res[1]+1]
