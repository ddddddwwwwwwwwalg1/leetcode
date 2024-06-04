## 迭代 组合 [1,2,3] --> [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
def subsets(nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


print(subsets([1,2,3]))

## 回溯
def func(nums):

    res = []
    path = []

    def dfs(nums, start_index, size):
        res.append(path[:])
        if start_index == size+1:
            return
        for i in range(start_index, size):
            path.append(nums[i])
            dfs(nums, i+1, size)
            path.pop()

    dfs(nums, 0, len(nums))
    return res


print(func([1,2,3]))
