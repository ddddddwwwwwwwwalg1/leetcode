def func(weight,value,bag_size):
    dp = [[0 for _ in range(bag_size+1)] for _ in range(len(weight))]
    first_weight = weight[0]
    first_value = value[0]
    for j in range(bag_size+1):
        if j >= first_weight:
            dp[0][j] = first_value

    for i in range(1,len(weight)):
        cur_weight = weight[i]
        cur_value = value[i]
        for j in range(1,bag_size+1):
            if j >= cur_weight:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-cur_weight]+cur_value)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)


# 一维解法
def func2(weight, value, bag_size):
    dp = [0 for i in range(bag_size+1)]
    for i in range(len(weight)):
        w = weight[i]
        v = value[i]
        for j in range(bag_size,w-1,-1):
            dp[j] = max(dp[j],dp[j-w]+v)
    return dp[-1]


bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]
func(weight, value, bag_size)