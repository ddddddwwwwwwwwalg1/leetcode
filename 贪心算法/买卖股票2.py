#  [7,1,5,3,6,4]

def func(nums):
    tmp = []
    for i in range(1,len(nums)):
        tmp.append(nums[i]-nums[i-1])
    res = 0
    for j in tmp:
        if j > 0:
            res+=j
    return res