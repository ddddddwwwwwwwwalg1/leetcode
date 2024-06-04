## nums = [1,2,3], S = 2, 输出 2（[1,2],[3]）

def func(nums,s):

    count = 0

    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum_ = sum(nums[i:j+1])
            if sum_ == s:
                count+=1
    return count

print(func([1,2,3],3))