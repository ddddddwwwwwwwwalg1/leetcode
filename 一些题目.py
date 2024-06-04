## 整数反转
def reverse_int(m):

    res = 0
    while m > 0 :
        digit = m%10
        res = res*10+digit
        m = m//10

    return res

## 最小路径和
def find_shortest_road(graph):
    m = len(graph[0])
    n = len(graph)

    dp = graph.copy()

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            elif i == 0:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += min(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

## 买卖股票的最佳时机1
def find_best_chance1(l):
    min_ = l[0]
    res = 0
    for i in l:
        res = max(res,i-min_)
        min_ = min(min_,i)
    return res

## 买卖股票的最佳时机2
def find_best_chance2(l):
    dp = [[0,0] for _ in range(len(l))]
    dp[0][0] = 0
    dp[0][1] = -l[0]
    for i in range(1,len(l)):

        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+l[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-l[i])

    return dp[-1][0]

## x的平方根

def func(m):
    x1 = m
    while abs(x1*x1 - m) > 0.00001:
        x1 = 0.5*(x1+m/x1)

    return x1

## 接雨水
def func2(l):
    res = 0
    for i in range(1,len(l)-1):
        max_l = l[0]
        for j in range(i):
            max_l = max(l,l[j])
        max_r = l[-1]
        for j in range(i+1,len(l)):
            max_r = max(max_r,l[j])
        res += min(max_l,max_r)-l[i]
    return res

## 含有k个元素的组合
def func3(nums,k):

    res = []
    path = []

    def dfs(start_index):

        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start_index,len(nums)):
            path.append(nums[i])
            dfs(i+1)
            path.pop(nums[i])
    dfs(0)
    return res

## 删除有序数组的重复项 1222334
def func4(nums):
    m = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != nums[i+1]:
            nums[m] = nums[i]
            m += 1
    return nums[:m]

## 移除元素
def func5(nums,k):
    m = 0
    n = len(nums)
    for i in range(n):
        if nums[i]!=k:
            nums[m] = nums[i]
            m+=1
    return m

## 搜索旋转数组
def func6(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        if nums[mid]>=nums[0]:
            if target <= nums[mid] and target >= nums[0]:
                right = mid-1
            else:
                left = mid+1
        else:
            if target<= nums[len(nums)-1] and target>=nums[mid]:
                left = mid+1
            else:
                right = mid-1
    return -1

## 长度最小的子数组,总和大于等于target
def func7(nums,target):
    left = 0
    right = len(nums)-1
    min_len = len(nums)

    for i in range(len(nums)):
        s = 0
        for j in range(i,0,-1):
            s += nums[j]
            len_ = j-i+1
            if s>=target and min_len>len_:
                left = i
                right = j
                min_len = len_
    return nums[left:right+1]

## 搜索二维数组
def func8(nums,target):
    m = len(nums[0])
    n = len(nums)

    i = 0
    j = n-1
    while i < m and j > 0:

        if nums[i][j] == target:
            return [i,j]
        elif nums[i][j] > target:
            j-=1
        else:
            i+=1
    return -1

## 层序遍历
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def func9(root):
    res = []
    queue = [root]
    while queue:
        tmp = []
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            res.append(tmp)
    return res

## power(x,n)
def func10(x,n):
    def func_(n):
        if n==0:
            return 1
        if n%2==1:
            return func_(n//2)*func_(n//2)*x
        else:
            return func_(n//2)*func_(n//2)
    return func_(n)

## 两个整数相除
def func11(m,n):

    res = 0
    while m-n >= 0:
        m -= n
        res += 1
    return res

## 回文数121
def func12(n):

    l = []
    while n > 0:
        digit = n%10
        l.append(digit)
        n = n//10
    return l==l[::-1]

# 旋转数组最小值 [3,4,5,1,2]
def func13(nums):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid
        else:
            r -= 1
    return nums[l]

## 丑数
def func14(n):
    a,b,c=0,0,0
    res = [1]
    for i in range(n-1):
        tmp1 = res[a] * 2
        tmp2 = res[b] * 3
        tmp3 = res[c] * 5
        min_ = min(tmp1,tmp2,tmp3)
        res.append(min_)
        if tmp1==min_:
            a+=1
        elif tmp2==min_:
            b+=1
        else:
            c+=1
    return res

## 最长公共子数组
def func15(s1,s2):
    m = len(s1)
    n = len(s2)
    res = 0
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i]==s2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 0
            res = max(res,dp[i][j])
    return res

## 最长公共子序列
def func16(s1,s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i]==s2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

## 反转链表



## 合并两个有序链表

## 移除链表元素

## 删除倒数第n个节点

