## 爬楼梯
# def climb_stairs(n):
#
#     dp = [0,1,2]
#
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#
#     for i in range(3,n):
#         dp.append(dp[i-1]+dp[i-2])
#
#     return dp[-1]
# print(climb_stairs(5))

## 快排
def func(nums):

    def quick_sort(nums,start,end):

        left = start
        right = end
        p = nums[left]

        while left < right:

            while left < right and nums[right] >= p:
                right-=1
                print(right)
            while left < right and nums[left] <= p:
                left += 1
            nums[left],nums[right] = nums[right],nums[left]

        nums[left] = p

        quick_sort(nums,start,left-1)
        quick_sort(nums,left+1,end)

    quick_sort(nums,0,len(nums)-1)

print(func([3,4,2,5]))