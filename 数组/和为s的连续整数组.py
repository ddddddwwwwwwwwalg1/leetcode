## target = 9, [2,3,4],[4,5]

def func(target):
    l = 1
    r = 2
    res = []
    while l < r:
        sum_ = (l+r) * (r-l+1)/2
        if sum_ == target:
            res.append([m for m in range(l,r+1)])
            l += 1
        elif sum_ < target:
            r += 1
        else:
            l += 1
    return res


def func1(target):

    i = 0
    j = 0
    sum_ = 0
    res = []
    while i <= target //2:
        if sum_ < target:
            sum_ += j
            j += 1
        elif sum_ > target:
            sum_ -= i
            i += 1
        else:
            res.append(list(range(i,j)))
            sum_ -= i
            i += 1
    return res


print(func(9))

