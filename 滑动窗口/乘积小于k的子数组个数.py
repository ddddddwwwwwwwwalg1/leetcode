def func(nums,k):
    total = 1
    i = 0
    res = 0
    for j in range(len(nums)):

        total = total * nums[j]
        while total >= k:
            total = total // nums[i]
            i += 1
        res += j-i+1
    return res
