## 全删 
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def func(head):
    dummy_head = ListNode(next=head)
    cur = dummy_head
    while cur.next is not None and cur.next.next is not None:
        if cur.next.val == cur.next.next.val:
            tmp = cur.next.val
            while cur.next.val == tmp and cur.next is not None:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next