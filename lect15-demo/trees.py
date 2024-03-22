class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

"""
        1
      / | \
     2  5  6
    / \ 
   3   4  
"""

root = Node(1,
    [
        Node(2,
            [
                Node(3, []), Node(4, [])
            ]),
        Node(5, []), Node(6, [])
    ]
)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

n3 = Node(3)
n4 = Node(4)
n2 = Node(2, left=n3, right=n4)
n5 = Node(5)
root = Node(1, left=n2, right=n5)

"""
        1
      /   \
     2     5
    / \ 
   3   4  
"""

def print_all_nodes(root):
    if root is None:
        return
    print_all_nodes(root.right)
    print_all_nodes(root.left)
    print(root.value)

# print_all_nodes(root)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

print(height(root))



def search_binary_tree(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    return search_binary_tree(root.left) or search_binary_tree(root.right)

def search_BST(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    if root.value < target:
        return search_BST(root.right)
    return search_BST(root.left)