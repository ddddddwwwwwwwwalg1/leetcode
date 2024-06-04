# nums = [0,1,2,2,3,0,4,2], val = 2

def func(nums, val):
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return nums[:left]


print(func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))