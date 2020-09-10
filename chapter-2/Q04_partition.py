def partition(head, partition):
    lowerHead = None
    lowerEnd = None
    upperHead = None
    upperEnd = None

    while head:
        if head.value < partition:
            if not lowerHead:
                lowerHead = head
                lowerEnd = head
            else:
                lowerEnd.next = head
                lowerEnd = head
        else:
            if not upperHead:
                upperHead = head
                upperEnd = head
            else:
                upperEnd.next = head

        head = head.next

    lowerEnd.next = upperHead
    return lowerHead
