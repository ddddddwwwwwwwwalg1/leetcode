def func(nums,target):
    nums.sort()
    abs_err = 100000
    res = 0
    for i in range(len(nums)-1):
        j = i+1
        k = len(nums)-1
        if nums[i] == nums[i-1] and i >0:
            i += 1
            continue
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp > target:
                if abs(tmp-target) < abs_err:
                    abs_err = abs(tmp-target)
                    res = [nums[i],nums[j],nums[k]]
                k -= 1
            elif tmp < target:
                if abs(tmp-target) < abs_err:
                    abs_err = abs(tmp-target)
                    res = [nums[i],nums[j],nums[k]]
                j += 1
            else:
                res = [nums[i],nums[j],nums[k]]
                return res
    return res


print(func([-1,2,1,-4],1))
