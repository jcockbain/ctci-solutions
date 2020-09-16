def get_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def print_list(head):
    values = get_list(head)
    string_values = " -> ".join([str(v) for v in values])
    print(string_values)
