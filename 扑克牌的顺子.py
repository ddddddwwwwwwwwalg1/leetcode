
def func(nums):
    repeat = set()
    min_,max_ = 0,14
    for i in nums:
        if i == 0:
            continue
        min_ = min(min_,i)
        max_ = max(max_,i)
        if i in repeat:
            return False
        repeat.add(i)
    return max_-min_ < 5
