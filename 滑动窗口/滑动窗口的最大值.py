class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = []
        n = len(nums)
        res=[]
        for i,j in zip(range(1-k,n-k-1),range(0,n)):
            if i > 0 and nums[i-1] == queue[0]:
                queue.pop(0)
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            if i >= 0:
                res.append(queue[0])
        return res