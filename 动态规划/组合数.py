## nums = [1, 2, 3] target = 4 所有可能的组合为： (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 3) (2, 1, 1) (2, 2) (3, 1)

def combinationSum4(nums, target: int) -> int:
    if not nums:
        return 0
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i-num]
    return dp[target]


print(combinationSum4([1, 2, 3], 4))