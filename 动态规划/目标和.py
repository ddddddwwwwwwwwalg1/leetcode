## left - (sum - left) = target 推导出 left = (target + sum)/2

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        sumValue = sum(nums)
        #注意边界条件为 target>sumValue or target<-sumValue or  (sumValue + target) % 2 == 1
        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]


def func(nums):
    cover = 0
    for i in range(len(nums)):
        cover = max(cover,i+nums[i])
        if cover >= len(nums):
            return True
    return False

def func2(nums):

    cur = 0
    next = 0
    step = 0

    for i in range(len(nums)):

        next = max(next,nums[i]+i)

        if i == cur:
            step += 1
            cur = next
            if next > len(nums)-1:
                return step
    return step


