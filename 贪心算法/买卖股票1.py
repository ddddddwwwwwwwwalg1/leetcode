def func(nums):
    res = 0
    min_ = 10000
    for i in nums:
        min_ = min(min_, i)
        res = max(res, i-min_)
    return res


print(func([1,2,0,10,8,9]))