def func(n):
    startx, starty = 0, 0
    loop = n//2
    count = 1
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,loop+1):
        for j in range(starty,n-i):
            res[startx][j] = count
            count += 1
        for j in range(startx,n-i):
            res[j][n-i] = count
            count += 1
        for j in range(n-i,starty,-1):
            res[n-i][j] = count
            count += 1
        for j in range(n-i,startx,-1):
            res[j][starty] = count
            count += 1
        startx += 1
        starty += 1
    mid = n//2
    if n % 2 != 0:
        res[mid][mid] = count
    return res

