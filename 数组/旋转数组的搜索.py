class Solution:
    def search(self, nums, target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[0]:
                if nums[0] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1