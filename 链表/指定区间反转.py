class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def func(head, m, n):
    pre = head
    for i in range(m-1):
        pre = pre.next
    left = pre.next

    right = pre
    for i in range(n-m+1):
        right = right.next
    cur = right.next

    pre.next = None
    right.next = None

    reverse(left)

    pre.next = right
    left.next = cur 

def reverse(head):
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        left_pre = head
        for i in range(m - 1):
            left_pre = left_pre.next
        right = left_pre
        for i in range(n - m + 1):
            right = right.next
        left = left_pre.next
        right_next = right.next

        left_pre.next = None
        right.next = None

        reverse(left)
        left_pre.next = right
        left.next = right_next

        return head


def reverse(head1):
    cur = head1
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

