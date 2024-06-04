# 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
def func(nums):
    left = 0
    right = len(nums)-1
    res = []
    while left <= right:
        if nums[left] * nums[left] >= nums[right] * nums[right]:
            res.append(nums[left] * nums[left])
            left += 1
        else:
            res.append(nums[right] * nums[right])
            right -= 1
    res.reverse()
    return res


print(func( [-4,-1,0,3,10]))