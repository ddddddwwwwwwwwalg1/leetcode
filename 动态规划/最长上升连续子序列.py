def func(nums):
    dp = [1 for i in range(len(nums))]
    res = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = 1
        res = max(dp[i], res)
    return res
