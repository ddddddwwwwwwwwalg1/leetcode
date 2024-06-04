def func(nums,target):

    i = 0
    j = len(nums)-1
    right = -1
    while i<=j:
        mid = (i+j)//2
        if nums[mid] <= target:
            i = mid + 1
        else:
            right = mid
            j = mid - 1
    # right = i
    if nums[j] != target:
        return 0
    i = 0
    j = len(nums)-1
    left = -1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] >= target:
            j = mid-1
        else:
            left = mid
            i = mid+1
    return right-left-1,right,left


print(func([5,7,7,8,8,10],8))