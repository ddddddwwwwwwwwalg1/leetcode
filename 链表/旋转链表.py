def func(head, k):
    cur = head
    length = 1
    while cur.next:
        cur = cur.next
        length += 1

    tail = cur
    tail.next = head

    cur = head
    for i in range(length-k):
        cur = cur.next
    newHead = cur.next
    cur.next = None

    return newHead


