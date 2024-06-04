# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]

def func(nums,):
    nums.sort()
    i = 0
    res = []
    while i < len(nums)-2:
        if nums[i]>0:
            break
        while i>=1 and nums[i] == nums[i-1]:
            i += 1
            continue
        j = i+1
        k = len(nums)-1
        while j<k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                k -= 1
                j += 1
        i += 1
    return res

print(func([-1, 0, 1, 2, -1, -4]))




























