def func(s1,s2):
    cnt1 = [0 for _ in range(26)]
    cnt2 = [0 for _ in range(26)]
    m = len(s1)
    n = len(s2)
    for i in range(m):
        tmp1 = s1[i] - 'a'
        tmp2 = s2[i] - 'a'
        cnt1[tmp1] += 1
        cnt2[tmp2] += 1
    if cnt1 == cnt2:
        return True
    for j in range(m,n):
        tmp1 = s2[j-m]-'a'
        tmp2 = s2[j]-'a'
        cnt2[tmp1]-=1
        cnt2[tmp2]+=1
        if cnt1==cnt2:
            return True
    return False