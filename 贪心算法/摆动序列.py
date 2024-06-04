def func(nums):
    curC, preC, res = 0,0,1
    for i in range(len(nums)-1):
        curC = nums[i+1]-nums[i]
        if curC * preC <= 0 and curC !=0:
            res += 1
            preC = curC
    return res


print(func([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))