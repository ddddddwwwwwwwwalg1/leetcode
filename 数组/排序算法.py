# 冒泡排序 [3,2,4,1,6]
def func1(nums):
    for j in range(1,len(nums)-1):
        for i in range(len(nums)-j):
            if nums[i+1] < nums[i]:
                nums[i+1],nums[i] = nums[i],nums[i+1]
    return nums
# 归并排序
def func2(nums):
    def part(nums,left,right):
        if left >= right:
            return
        mid = (left+right)//2
        part(nums,left,mid)
        part(nums,mid+1,right)
        merge(nums,left,mid,right)

    def merge(arrays,left,mid,right):
        res = []
        i,j = left,mid
        m,n = mid+1,right
        while i<=j and m<=n:
            if arrays[i] <= arrays[m]:
                res.append(arrays[i])
                i+=1
            else:
                res.append(arrays[m])
                m+=1
        while i<=j:
            res.append(arrays[i])
            i+=1
        while m<=n:
            res.append(arrays[m])
            m+=1
        arrays[left:left+len(res)] = res

    part(nums,0,len(nums)-1)

# 快速排序,[3,2,4,1,6]

def func4(nums):
    def quick_sort(left,right,nums):
        if left >= right:
            return
        i = left 
        j = right
        p = nums[left]
        while i<j:
            while i<j and nums[j]>=p:
                j -= 1
            while i<j and nums[i]<=p:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        quick_sort(left, i-1, nums)
        quick_sort(i+1, right, nums)
    quick_sort(0, len(nums)-1, nums)
    return nums

print(func1([3,2,4,1,6]))

a = [3,2,4,1,6]
func2(a)
print(a)

b = [3,2,4,1,6]
func3(b)
print(b)
