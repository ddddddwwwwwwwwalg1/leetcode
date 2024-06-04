def func(nums):
    nums = set(nums)
    longestLen = 0
    for i in nums:
        if i-1 not in nums:
            curNum = i
            len = 1
            while curNum + 1 in nums:
                curNum += 1
                len += 1
            longestLen = max(longestLen, len)
    return longestLen


print(func([100, 101, 1, 2, 4, 5, 3]))