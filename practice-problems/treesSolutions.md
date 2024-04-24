1. **This is a HARD problem!** 

A tree is a binary search tree is for each node:
   - All elements in the left subtree are smaller than the current node's value
   - All elements in the right subtree are smaller than the current node's value

With that in mind, we actually have a tricky coding challenge ahead of us, because we can't just write something like
```
def is_BST(root):
    if root is None:
        return True
    
    if root.left is not None and root.left.value > root.value:
        return False
    
    if root.right is not None and root.right.value < root.value:
        return False
    
    return is_BST(root.left) and is_BST(root.right)
```
This doesn't work because everything in the whole left subtree has to be smaller than `root.value`, and this code gives us no way of verifying that.

Instead, we have to write a helper that keeps track of a lower and upper bound.
```
def is_BST(root):
    return helper(root, -float('inf'), float('inf'))  # that's negative infinity and infinity in Python
   
   
def helper(root, lower_bound, upper_bound):
    if root is None:
        return True
    if root.value < lower_bound or root.value > upper_bound:
        return False
    
    # This is the really tricky line! As we recurse and get deeper in the tree, the bounds on what a node's values
    # can be start to change. Imagine the first node we see is 5 and we want to check the left subtree. Then every 
    # node we see in that whole recursive chain must have a value less than 5. But if the next value we see is 3, and we 
    # are then investigating its right child, that child now must have a value that's less than 5 but ALSO greater than 3.
    # Hence the updating bounds!
    return helper(root.left, lower_bound, root.value) and helper(root.right, root.value, upper_bound)
```
Classic recursion: super tricky and rewarding to think through, but also like 5 lines of code :D 
2. This is more straightforward. The number of nodes in a tree is 1 + the number of nodes in the left subtree + the number of nodes in the right subtree. The number of nodes in an empty tree is zero. Therefore:
```
def number_of_nodes(root):
    if root is None:
        return 0
    return 1 + number_of_nodes(root.left) + number_of_nodes(root.right)
```
3. Same template, slightly different code:
```
def number_of_left_children(root):
    if root is None:
        return 0
    # add one if there's a left child, then recurse!
    has_left = 0
    if root.left is not None:
        has_left = 1 
    return has_left + number_of_left_children(root.left) + number_of_left_children(root.right)
```
4. This is a bit like computing the height - the largest path sum is whatever the largest path sum in any subtree is, plus the current node value.
```
def largest_path_sum(root):
    if root is None:
        return 0
    return max(largest_path_sum(root.left), largest_path_sum(root.right)) + root.value
```
5. Now we need to make the function return a list, and build up that list into a larger list as we go:
```
def largest_path_sum(root):
    if root is None:
        return []

    # we have to fetch the paths from recursive calls separately, since 
    # we can't just directly take the max() of two lists
    right_path = largest_path_sum(root.right)
    left_path = largest_path_sum(root.left)
    
    # the sum() builtin is really handy here!
    # if the right recursive call found a path with a larger sum, let's hold onto that and 
    # just append the current node's value.
    if sum(right_path) > sum(left_path):
        return right_path + [root.value]
    else:
        # otherwise, we use the left recursive result
        return left_path + [root.value]
```
6. This problem is also QUITE tricky and well beyond anything I'd ask you to write on an exam. It's hard because at each point in the tree, it's not clear whether you should take that node's value and use it in your "largest sum" or not. If the tree's values were all positive, it would be easy, but if they can be negative, we have a problem: if we see a negative-valued node, do we hold onto it because it connects two large-value nodes, or should we cut the path off then and there?

It's easy to fall down the recursive rabbit hole thinking about this, but it turns out that we just need to keep track of two pieces of information at every level:
- What is the best path we've found that does involve the current node?
- What is the best path we've found that doesn't involve the current node.

Then things fall into place:
```
def largest_path_sum(root):
    return max(helper(root)) # helper is going to return a tuple

def helper(root):
    if root is None:
        return (0, 0)
    left_sum_with, left_sum_without = helper(root.left)
    right_sum_with, right_sum_without = helper(root.right)
    
    # note that the first returned values had to have used root.left and root.right, respectively
    # however, left_sum_without and right_sum_without are sums of paths that don't contain root.left or
    # root.right, so we cannot add root.value to them -- that would be creating a path sum that skips some elements!
    best_without = max(left_sum_with, left_sum_without, right_sum_with, right_sum_without)
    best_with = root.value + max(left_sum_with, right_sum_with)
    
    return best_with, best_without
```
7. Left as an exercise due to lack of time and extensive discussion elsewhere on the internet.


