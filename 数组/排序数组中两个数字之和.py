def func(nums,target):

    i = 0
    j = len(nums)-1

    while i < j:
        sum_ = nums[i] + nums[j]
        if sum_==target:
            return [i,j]
        elif sum_<target:
            i += 1
        else:
            j -= 1
    return -1 