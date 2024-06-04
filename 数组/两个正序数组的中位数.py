def func(nums1,nums2):

    def getKth(k):
        index1 = 0
        index2 = 0

        while True:
            if k==1:
                return min(nums1[index1],nums2[index2])
            newindex1 = min(index1 + k // 2 - 1, m-1)
            newindex2 = min(index2 + k // 2 - 1, n-1)
            p1,p2 = nums1[newindex1],nums2[newindex2]
            if p1<=p2:
                k -= newindex1 - index1+1
                index1 = newindex1 + 1
            else:
                k -= newindex2 - index2 + 1
                index2 = newindex2 + 1
    m, n = len(nums1), len(nums2)
    totallen = m + n
    if totallen % 2 == 1:
        return getKth((totallen+1)//2)
    else:
        return (getKth(totallen//2) + getKth(totallen//2+1))/2

