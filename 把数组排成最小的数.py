## 快排思路
def func(l, r):
    i, j = l, r
    if l >= r:
        return
    while i < j:
        while nums[l] + nums[j] <= nums[j] + nums[l] and i < j:
            j -= 1
        while nums[i] + nums[l] <= nums[l] + nums[i] and i < j:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[l] = nums[l], nums[i]
    func(l, i-1)
    func(i+1, r)


nums = [3, 30, 34, 5, 9]
nums = [str(i) for i in nums]
func(0, len(nums)-1)
print(''.join(nums))
