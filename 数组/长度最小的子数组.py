# s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。 滑动窗口解法
def func(nums, s):
    i = 0
    res = 10000
    Sum = 0
    for j in range(len(nums)):
        Sum += nums[j]
        while Sum >= s:
            res = min(res, j-i+1)
            Sum -= nums[i]
            i += 1
    return 0 if res > 100 else res


print(func([2,3,1,2,4,3], 7))
