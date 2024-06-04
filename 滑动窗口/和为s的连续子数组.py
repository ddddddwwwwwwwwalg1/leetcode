#枚举
def func(nums,k):
    count = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i, 0, -1):
            sum_ += nums[j]
            if sum_ == k:
                count += 1
    return count

