class ListNode:
    def __int__(self,val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val):
    dummy_head = ListNode(-1,head)
    cur = dummy_head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next()
