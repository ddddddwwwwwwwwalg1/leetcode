## 不可以选重复元素
def func(nums, target):
    res = []
    path = []

    def dfs(nums, sum_, start_index, size):
        if sum_ == target:
            res.append(path[:])
            return

        if sum_ > target:
            return

        for i in range(start_index, size):
            tmp = nums[i]
            sum_ += tmp
            path.append(tmp)
            dfs(nums, sum_, i+1, size)
            sum_ -= tmp
            path.pop()
    dfs(nums, 0, 0, len(nums))
    return res


print(func([2,3,4,6],6))