#01背包
def func(weights,values,bagsize):
    dp = [0 for _ in range(len(bagsize))]
    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        for j in range(bagsize,w-1,-1):
            dp[j] = max(dp[j],dp[j-w]+v)
    return dp[-1]

#完全背包
def func1(weights,values,bagsize):
    dp = [0 for _ in range(len(bagsize))]
    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        for j in range(w,bagsize+1):
            dp[j] = max(dp[j],dp[j-w]+v)
    return dp[-1]

# 兑换零钱, 可重复的组合数
def func2(coins,target):
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(len(coins)):
        coin = coins[i]
        for j in range(coin, target+1):
            dp[j] = dp[j] + dp[j-coin]
    return dp[-1]

# 子集
def func3(nums):
    res = [[]]
    for i in nums:
        res = res + [[i]+j for j in res]
    return res

#二叉树所有路径
def func4(root):
    stack = [root]
    path_st = [root.val]
    res = []
    while stack:
        node = stack.pop()
        path = path_st.pop()
        if node.left is None and node.right is None:
            res.append(path)
        if node.right:
            stack.append(node.right)
            path_st.append(path+'->'+node.right.val)
        if node.left:
            stack.append(node.left)
            path_st.append(path+'->'+node.left.val)
    return res

#字符串转整数
def func5(s):
    if '1' <= s[0] <= '9':
        flag = 1
        i = 1
    else:
        flag = -1
        i = 0
    res = 0
    for j in range(i,len(s)):
        res = res * 10 + ord(s[j])-ord('0')
    return res * flag

# hello world --> world hello
def func6(s):
    s = s.strip()
    i = len(s)-1
    j = len(s)-1
    res = []
    while i >= 0:
        while i>0 and s[i] != ' ':
            i -= 1
        res.append(s[i+1:j+1])
        while s[i] == ' ':
            i -= 1
        j = i
    return ''.join(res)

# 逆序对
def func7(nums):
    res = 0
    def partition(nums,left,right):
        global res
        if left >= right:
            return
        mid = (left + right)//2
        partition(nums,left,mid)
        partition(nums,mid+1,right)
        merge(nums,left,mid,right)

    def merge(nums,left,mid,right):
        global res
        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            v1 = nums[i]
            v2 = nums[j]
            if v1 <= v2:
                tmp.append(v1)
                i += 1
            else:
                res += mid-i+1
                tmp.append(v2)
                j += 1
    partition(nums,0,len(nums)-1)
    return res

# 全排列
def func8(nums):
    res = []
    def backtrack(nums,tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
    backtrack(nums,[])
    return res

# power(x,n)
def func9(x,n):

    def f(n):
        if n==0:
            return 1
        y = f(n//2)
        if n%2==1:
            return y*y*x
        else:
            return y*y
    return f(n)

# 跳跃游戏
def func10(nums):
    cover = 0
    for i in range(len(nums)):
        if i <= cover:
            cover = max(cover,nums[i]+i)
            if cover >= len(nums)-1:
                return True
    return False

def func11(nums):
    step = 0
    curD, nextD = 0,0
    for i in range(len(nums)):
        nextD = max(nums[i]+i,nextD)
        if i==curD:
            step += 1
            curD = nextD
            if nextD >= len(nums)-1:
                return step
    return step

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

# 两两交换链表节点
def func12(head):
    dummy_head = ListNode(next = head)
    pre = dummy_head
    while pre.next and pre.next.next:
        cur = pre.next
        post = pre.next.next

        cur.next = post.next
        post.next = cur
        pre .next = post

        pre = pre.next.next
    return dummy_head.next





