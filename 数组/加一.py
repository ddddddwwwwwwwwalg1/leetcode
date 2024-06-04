def func(nums):

    for i in range(len(nums)-1,-1,-1):
        if nums[i] != 9:
            nums[i] += 1
            for j in range(i+1,len(nums)):
                nums[j] = 0
            return nums
    return [1] + [0] * len(nums)