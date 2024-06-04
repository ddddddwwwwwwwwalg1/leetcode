# [2,3,4] 6
def func(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] not in d.keys():
            d[nums[i]] = i
        else:
            return [d[target-nums[i]],i]
    return None

print(func([2,3,4], 6))