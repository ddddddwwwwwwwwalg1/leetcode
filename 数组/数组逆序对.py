res = 0
def func(nums):
    def partition(nums, left, right):
        global res
        if left >= right:
            return
        mid = (left + right)//2
        partition(nums, left, mid)
        partition(nums, mid+1, right)
        return merge(nums, left, mid, right)

    def merge(nums, left, mid, right):
        global res
        i = left
        j = mid+1
        tmp = []
        while (i<=mid and j<=right):
            if nums[i] > nums[j]:
                res += mid - i +1
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        while i<=mid:
            tmp.append(nums[i])
            i+=1
        while j<=right:
            tmp.append(nums[j])
            j+=1
        nums[left:right+1] = tmp

    partition(nums, 0, len(nums) - 1)
    return res

print(func([6,7,5,8,9,1]))
