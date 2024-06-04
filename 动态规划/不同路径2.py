# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

def func(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1:
        return 0
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(cols):
        if obstacleGrid[0][i] == 1:
            break
        dp[0][i] = 1
    for j in range(rows):
        if obstacleGrid[j][0] == 1:
            break
        dp[j][0] = 1
    for m in range(1,cols):
        for n in range(1,rows):
            if obstacleGrid[m][n] != 1:
                dp[m][n] = dp[m-1][n] + dp[m][n-1]
    return dp[-1][-1]

