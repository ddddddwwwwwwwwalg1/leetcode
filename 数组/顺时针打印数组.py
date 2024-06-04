def func(nums):
    l,r,t,b = 0,len(nums)-1,0,len(nums[0])-1
    res = []
    while True:
        for i in range(l,r+1):
            res.append(nums[t][i])
        t += 1
        if t > b:
            break
        for i in range(t,b+1):
            res.append(nums[i][r])
        r -= 1
        if l>r:
            break
        for i in range(r,l-1,-1):
            res.append(nums[b][i])
        b -= 1
        if t>b:
            break
        for i in range(b,t-1,-1):
            res.append(nums[i][l])
        l += 1
        if l>r:
            break
    return res