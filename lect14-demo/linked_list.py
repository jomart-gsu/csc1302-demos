class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

head = Node(5, None)
head.next = Node(12, None)
head.next.next = Node(23, None)
head.next.next.next = Node(6, None)


# 5 -> 12 -> 6

def remove(head, val):
    """
    Remove a node with value val from a linked list given the head
    """
    current = head
    while current is not None and current.value != val:
        current = current.next
    if current is None:
        return

    prev = head
    while prev.next != current:
        prev = prev.next

    # current holds the node we want
    # prev holds the node before it

    prev.next = current.next
    current.next = None




remove(head, 23)



