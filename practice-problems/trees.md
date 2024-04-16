# Tree Practice Problems
In the below, assume a `TreeNode` is defined as follows:
```
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```
1. Write a function `is_binary_search_tree()` that takes a binary tree and returns True if it is a binary search tree and False otherwise.
2. Write a function `number_of_nodes()` that takes a binary tree and returns the number of nodes in the tree.
3. Write a function `number_of_left_children()` that takes a binary tree and returns the number of nodes that are left children of other nodes.
4. Consider the paths from root to leaf in a binary tree. Let's call the sum of values in such a path the "path sum" of that path. Write a function `largest_path_sum()` that takes a binary tree and returns the largest path sum across all paths from root to leaf.

For example, the tree
```
    4
   / \ 
  2   3 
 /   / \
5   1   0
```

would have largest path sum (4+2+5) = 11.
5. Do the same, but return a list of nodes in that path.
6. Do the same, but allow for paths that do not start at the root and paths that do not end at a leaf (remember that node values can be negative!)
7. **(Challenge)** Write a function `lowest_common_ancestor()` that takes the root of a binary tree and two nodes A and B, and finds the node N with the largest distance from the root such that A and B are both descendants of N.