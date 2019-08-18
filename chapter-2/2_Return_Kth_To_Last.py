from LinkedList import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
print(kth_to_last(ll, 2))