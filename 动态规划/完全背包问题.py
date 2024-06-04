def func(weight, value, bag_size):
    dp = [[0 for _ in range(bag_size+1)] for _ in range(len(weight))]
    first_weight = weight[0]
    first_value = value[0]
    for j in range(bag_size+1):
        if j >= first_weight:
            dp[0][j] = dp[0][j-first_weight]+first_value

    for i in range(1,len(weight)):
        cur_weight = weight[i]
        cur_value = value[i]
        for j in range(1,bag_size+1):
            if j >= cur_weight:
                dp[i][j] = max(dp[i-1][j],dp[i][j-cur_weight]+cur_value)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)


# 先遍历物品，再遍历背包
def test_complete_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0] * (bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bag_weight])

bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]
func(weight, value, bag_size,)