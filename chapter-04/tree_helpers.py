from collections import deque


def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)


def level_order_traversal(root):
    queue = deque([root])
    res = []
    while queue:
        res.append([])
        for _ in range(len(queue)):
            node = queue.pop()
            res[-1].append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
    return res
