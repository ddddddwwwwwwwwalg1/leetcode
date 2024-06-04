
def func(nums):

    p = 0
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            nums[i],nums[p] = nums[p],nums[i]
            p += 1
    for j in range(p,n):
        if nums[j] == 1:
            nums[j],nums[p] = nums[p],nums[j]
            p += 1
    return nums

