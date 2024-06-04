# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
#
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

def func(nums):
    sum_ = sum(nums)
    target = sum_ //2

    dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]

    for j in range(nums[0],target+1):
        dp[0][j] = nums[0]

    for i in range(1,len(nums)):
        for j in range(1,target+1):
            if j >= nums[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i]]+nums[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return sum_ - 2*dp[-1][-1]

print(func([2,7,4,1,8,1]))