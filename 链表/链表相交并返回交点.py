def getIntersectionNode(headA, headB):
    lenA, lenB = 0, 0
    curA = headA
    curB = headB
    while curA:
        curA = curA.next
        lenA += 1
    while curB:
        curB = curB.next
        lenB += 1
    curA = headA
    curB = headB
    if lenA > lenB:
        curA, curB = curB, curA
        lenA, lenB = lenB, lenA
    for i in range(lenB-lenA):
        curB = curB.next
    while curA:
        if curA == curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None
