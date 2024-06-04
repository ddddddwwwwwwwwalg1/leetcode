# 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].

def func(nums):
    sum_ = sum(nums)
    if sum_ % 2 != 0:
        return False
    target = sum_ // 2
    dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]
    for j in range(nums[0], target+1):
        dp[0][j] = nums[0]
    for m in range(1,len(nums)):
        for n in range(1,target+1):
            if n >= nums[m]:
                dp[m][n] = max(dp[m-1][n],dp[m-1][n-nums[m]]+nums[m])
            else:
                dp[m][n] = dp[m-1][n]
    print(dp)
    return dp[-1][-1] == target


print(func([1,5,11,5]))