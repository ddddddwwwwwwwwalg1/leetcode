def func(nums):
    if nums[-1] == len(nums) - 1:
        return nums[-1] + 1
    res = -1
    i = 0
    j = len(nums)-1
    while i<=j:
        mid = (i+j)//2
        if nums[mid] == mid:
            i = mid + 1
        else:
            res = mid
            j = mid - 1
    return res