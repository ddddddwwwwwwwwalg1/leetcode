## 几步能到达
class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance:
                ans += 1
                curDistance = nextDistance
                if nextDistance >= len(nums) - 1:
                    break
        return ans

## 是否可以到达
class Solution2:
    def canJump(self, nums) -> bool:
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1:
                    return True
        return False