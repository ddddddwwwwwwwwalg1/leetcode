## [[1,3,1],
#   [1,5,1],
#   [4,2,1]]
#   路线：1->3->5->2->1 

def func(nums):
    m = len(nums)
    n = len(nums[0])
    dp = nums.copy()
    for i in range(1,m):
        dp[0][i] = dp[0][i-1]+nums[0][i]
    for j in range(1,n):
        dp[j][0] = dp[j-1][0]+nums[j][0]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])+nums[i][j]
    return dp[-1][-1]


print(func([[1,3,1],[1,5,1],[4,2,1]]))