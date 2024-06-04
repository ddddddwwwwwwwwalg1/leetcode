def func(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i += 1
    return nums[:i+1]


print(func([1,1,2]))