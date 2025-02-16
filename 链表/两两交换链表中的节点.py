class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def swap(head):
    res = ListNode(next = head)
    pre = res
    while pre.next and pre.next.next:
        cur = pre.next
        post = pre.next.next

        cur.next = post.next
        post.next = cur
        pre.next = post

        pre = pre.next.next
    return res.next

