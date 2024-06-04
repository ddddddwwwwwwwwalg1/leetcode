def func(nums,k):
    i = 0
    total = 1
    res = 0
    for j in range(len(nums)):
        total = total * nums[j]
        while i <= j and total >= k:
            total = total//nums[i]
            i += 1
        if i <= j:
            res += j-i+1
    return res
