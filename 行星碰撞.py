def func(nums):

    stk = []

    for i in nums:
        flag = 1
        while flag and stk and i<0 and stk[-1] > 0:
            if stk[-1] >= -i:
                flag = 0
            if stk[-1] <= -i:
                stk.pop()
        if flag == 1:
            stk.append(i)
    return stk
