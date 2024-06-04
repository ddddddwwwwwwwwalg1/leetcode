def func(nums):

    def helper(i,j):
        if i>=j:
            return True
        p = i
        while nums[p] < nums[j]:
            p += 1
        m = p
        while nums[p] > nums[j]:
            p += 1
        return p==j and helper(i,m-1) and helper(m,j-1)

    return helper(0,len(nums)-1)