# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

def func(nums):
    dp = [1 for _ in range(len(nums))]
    ret = 0
    for i in range(1, len(nums)):
        for j in range(1, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
        ret = max(dp[i], ret)
    return ret


print(func([10,9,2,5,3,7,101,18]))
