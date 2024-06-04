def func(nums):
    l = 0
    r = len(nums)-1
    res = 0
    while l<r:
        if nums[l] < nums[r]:
            res = max(res, (l-r) * nums[l])
            l += 1
        else:
            res = max(res, (l-r) * nums[r])
            r -= 1
    return res