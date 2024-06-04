# 递归

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def func(head,k):
    cur = head
    for i in range(k):
        if cur == None:
            return head
        cur = cur.next
    tail = cur

    pre = None
    cur = head
    while cur != tail:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
    head.next = func(tail,k)

    return pre
