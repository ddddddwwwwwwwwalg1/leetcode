class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def func(head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre