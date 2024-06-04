def func(nums1,nums2):
    dict = {}
    for num in nums1:
        dict[num] = 1
    res = []
    for num in nums2:
        if num in dict.keys() and dict[num]==1:
            res.append(num)
            dict[num] = 0
    return res
