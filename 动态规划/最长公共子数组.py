def func(nums1,nums2):
    m = len(nums1)+1
    n = len(nums2)+1
    dp = [[0 for i in range(m)] for j in range(n)]
    result = 0
    for i in range(1, m):
        for j in range(1, n):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 0

            result = max(result, dp[i][j])
    return result