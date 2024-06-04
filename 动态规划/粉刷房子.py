## costs = [[17,2,17],[16,16,5],[14,3,19]]
def func(costs):

    dp = [[0 for _ in range(len(costs))] for _ in range(3)]

    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]

    for i in range(1, len(costs)):

        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    return min(dp[-1][0], dp[-1][1], dp[-1][2])