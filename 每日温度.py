def func(nums):

    d = {}
    n = len(nums)
    ans = [0] * n
    for i in range(n-1,-1,-1):
        tmp = nums[i]
        index = -1
        for j in range(tmp+1,100):
            index = min(d.get(j),index)
        ans[i] = index-i
        d[tmp] = i
    return ans
