class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def func(head, n):
    dummy_head = ListNode(next=head)
    fast = dummy_head
    slow = dummy_head
    while n>0:
        fast = fast.next
        n -= 1
    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy_head.next