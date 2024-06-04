
class Solution:
    def permute(self, nums):
        if len(nums)==1:
            return [nums]
        res = []
        path = []
        usage_list = [False] * len(nums)
        def dfs(nums, usage_list):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0,len(nums)):
                if usage_list[i] == True:
                    continue
                usage_list[i] = True
                path.append(nums[i])
                dfs(nums,usage_list)
                path.pop()
                usage_list[i] = False

        dfs(nums, usage_list)
        return res