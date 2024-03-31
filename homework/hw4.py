class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def potato_game(n, k):
    """
    Simulate a circular counting-out game with n players.

    Each round of the game, we count off k players and eliminate the kth.
    We then start the next round from the player after the one eliminated.

    Returns the number of the last remaining player. Players are numbered
    starting from zero.
    """

    if n < 1:
        return -1  # invalid input
    if n == 1:
        return 0  # game is over before it started

    # Create a circularly linked list with n nodes
    head = LinkedListNode(0)
    cur = head
    for i in range(1, n):
        cur.next = LinkedListNode(i)
        cur = cur.next

    cur.next = head  # finish the circle

    # Play the game
    cur = head
    while cur.next != cur:  # will be True as long as the list has >1 nodes
        for _ in range(k-2):
            cur = cur.next

        print(f"{cur.next.value} is eliminated")
        # we've taken k-1 steps, so delete the NEXT node
        cur.next = cur.next.next
        # start the next round from the node after the removed one
        cur = cur.next

    return cur.value


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_info(root):
    def height(root):
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 0
        return 1 + max(height(root.right), height(root.left))

    def num_leaves(root):
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        return num_leaves(root.left) + num_leaves(root.right)

    def is_full(root):
        if root is None:
            return True
        if root.right is None and root.left is not None:
            return False
        if root.left is None and root.right is not None:
            return True
        return is_full(root.left) and is_full(root.right)

    def is_balanced(root):
        if root is None:
            return True
        if is_balanced(root.right) and is_balanced(root.left):
            return abs(height(root.right) - height(root.left)) <= 1
        return False

    print(
        f"Height: {height(root)}\nNumber of leaf nodes: {num_leaves(root)}\n"
        f"Is Full: {is_full(root)}\nIs Balanced: {is_balanced(root)}"
    )

print(potato_game(12,8))
print(potato_game(11,6))
print(potato_game(7,13))

n3 = TreeNode(3)
n4 = TreeNode(4)
n2 = TreeNode(2, left=n3, right=n4)
n5 = TreeNode(5)
root = TreeNode(1, left=n2, right=n5)
tree_info(root)

n5 = TreeNode(5)
n4 = TreeNode(4)
n3 = TreeNode(3, left=n4, right=n5)
n2 = TreeNode(2, left=n3)
root = TreeNode(1, left=n2)

tree_info(root)