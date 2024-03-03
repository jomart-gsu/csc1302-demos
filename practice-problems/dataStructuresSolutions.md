# SECTION 1: Sets
1. Write a function `dedupe(l)` that takes a list of numbers `l` and returns a list of unique elements in `l` (i.e. numbers that only appear once) (yes we did this in class).

```
def dedupe(l):
    return list(set(l))

# BTW, these are O(n) time and space complexity:
    - We have to iterate over all of l to put its elements in a set. We have to then iterate over all elements in the set to get it in list form.
    - We are allocating O(n) space for the set we're storing the elements of l in in the worst case.
```
2. Write a function `overlap(l1, l2)` that takes two lists of numbers `l1` and `l2` and returns a list of all the numbers that appear in both `l1` and `l2`. Your function should run in `O(n)` time.

```
def overlap(l1, l2):
    s1 = set(l1)  # O(n), where n is the size of l1
    s2 = set(l2)  # O(m), where m is the size of l2
    return list(s1.intersection(s2))  # O(n), since we have to look at all elements in s1 and see if they're in s2.
```
3. Describe the big-Oh time and space complexity of the following function:

```
def are_all_letters_unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        s.add(char)
    return True
```
*This loop will terminate early if we encounter a duplicate letter in `s`. Therefore, in the worst case, all letters in `s` are unique, and we iterate over all of `s` and store each letter in `seen`, which brings both our time and space complexity to `O(n)`, where `n` is the length of `string`.*
4. Describe the big-Oh time and space complexity of the following function:
``` 
def pair_intersection(l1, l2, l3, l4):
    result = []
    s = set()
    for num1 in l1:
        for num2 in l2:
            s.add((l1, l2))  # tuples are hashable so this is okay!
    for num3 in l3:
        for num4 in l4:
            if (l3, l4) in s:
                result.append(l3, l4)
    return result
```
*This function creates a set of pairs of elements from l1 and l2 (the cross-product, in technical terms), then looks through pairs of elements from l3 and l4, finding all shared items, and storing them in the list. The largest `result` can get is if l3 and l4 are the same as l1 and l2 -- in that case, all pairs of elements will get added to `result`. Moreover, the set could contain all pairs of elements from `l1` and `l2`. We don't know if `l1` and `l2` are bigger than `l3` and `l4`, or vice versa, so the space complexity ends up being `O(ab+cd)`, where `a, b, c, d` are the sizes of `l1, l2, l3, l4`, respectively. The time complexity is the same, as it's determined by the two pairs of `for` loops.* 
5. Describe the bug in the following snippet of code:
```
s1 = {1,2,3}
s2 = {4,5,6}
set_of_sets = {s1, s2}
```
* This code tries to create a set of sets, which is not allowed in Python because sets are not hashable due to their immutability.*

# SECTION 2: Stacks
1. Describe the bug in the following snippet of code:
```
stack = []
stack.push(1)
stack.pop()
stack.pop()
```
*This code attempts multiple pops from a stack with only one element in it. If you call `stack.pop()` when `stack` is empty, you get an `IndexError`. 

2. Write a function `is_balanced(s)` that takes a string `s` and returns `True` if its parentheses are balanced and `False` otherwise. For example, `is_balanced("(abc)()((a)b)")` would return `True` because all open parens have a subsequent closing paren, and vice versa.
```
def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.push(char)
        if char == ")":
            # trying to pop from an empty stack means we have a closing paren
            # with no opening paren preceding it
            if len(stack) == 0:
                return False
            stack.pop()
    # if stack is empty, all opening parens got cancelled out. If not, the string is imbalanced.
    return len(stack) == 0
```
*Note: the astute reader will notice that you don't technically need a stack here. You could accomplish the same using simple counters:*
```
def is_balanced(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        if char == ")":
            if count == 0:
                return False
            count -=1
    return count == 0
```
3. *CHALLENGE:* Write a function `balance(s)` that takes a string and makes its parentheses balanced by removing as few parentheses as possible. For example, `balance("a(abc(())") might return `"a(abc())"`.
*Now we do need a stack, because the position of the parentheses matters:*
```
def balance(s):
    extra_opening_parens = []  # this will contain indices of parentheses we want to remove
    extra_closing_parens = set()
    for i in range(len(s)):
        if s[i] == "(":
            extra_opening_parens.append(i)
        if s[i] == ")":
            if len(extra_opening_parens) == 0:
                extra_closing_parens.add(i)
            else:
                extra_opening_parens.pop()
    
    extra_opening_parens = set(extra_opening_parens)  # need O(1) lookup to make the overall algorithm O(n)
    result = []
    for char in s:
        if char not in extra_opening_parens and char not in extra_closing_parens:
            result.append(char)
    return "".join(result)  # This is an operation that takes a string and turns it into a list. We use it because appending to a string is an O(n) operation in the length of the string (so O(n^2) if we do it n times), but building the string all at once with join() is O(n) total.
```
# SECTION 3: Linked Lists
For the below, assume linked lists are defined by the following class:
```
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```
That is, we're working with plain old singly-linked lists.

1. Write a function `is_sorted(head)` that takes a linked list and returns `True` if the items in the list are sorted, and `False` otherwise.
```
def is_sorted(head):
    if head is None:
        return True 
    prev = head.value
    
    # at each element, check if it's at least as large as the previous element
    # if we make it through the loop without returning, the list was sorted, so return True
    while head.next is not None:
        head = head.next
        if head.value < prev:
            return False
        prev = head.value
    return True
```
2. Identify the big-Oh time complexity of the following code:
```
def append_to_linked_list(head, value):
    if head is None:
        return Node(value)
    while head.next is not None:
        head = head.next
    head.next = Node(value)
```
*The `while` loop will iterate as many times as there are nodes in the linked list with head `head`. Therefore, the time complexity is O(n), where n is the length of the list. Note that having a `tail` reference would make this operation O(1), because we could just start there instead.*
3. Describe the bug in the following code:
```
def remove_last_element_of_linked_list(head):
    if head is None:
        return
    while head.next is not None:
        head = head.next
    head.next = None
```
*This code doesn't really do anything. It traverses the list until it reaches the last element, but then it just sets its `next` to `None`, which should already be the case because it's the last element anyway. Remember, when removing from a singly-linked list, you need to update the `next` pointer so the node you'er removing doesn't point to anything (which this code does, although it's only necessary if you're not on the last item in the list), AND, crucially, you have to make the item before the one you're removing point to its new neighbor (since you're removing its old neighbor). Otherwise, you're just chopping off a whole section of the list!*
4. Write a function `insert_at_position(head, value, i)` that inserts a node with value `value` at the `i`th position in a linked list `head`. You can assume the list starting at `head` has at least `i` values.

```
def insert_at_position(head, value, i):
    if i == 0:
        return Node(value, head)  # probably makes sense to return the new head here
    
    # travel to the node BEFORE the one we're inserting
    cur = head
    for _ in range(i-1):
        cur = cur.next
    
    # Now we want to make this node point to the new node, and the new node to point to this one's old neighbor
    new_node = Node(value, cur.next)
    cur.next = new_node
```
5. Now assume you have a doubly linked list:
```
class Node:
    def __init__self(value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
```
That is, each node has a pointer to both of its neighbors! 

Write the same function as in question 4 so that it works on such a linked list!

*Insertion is a little more complicated with doubly-linked lists -- now we have to manage the `previous` pointers of the neighbor node as well.*
```
def insert_at_position(head, value, i):
    if i == 0:
        return Node(value, None, head)  # same as last time, but no prev node if it's the first
    
    # travel to the node BEFORE the one we're inserting
    cur = head
    for _ in range(i-1):
        cur = cur.next
    
    # Now we want to
    # - make current node's next the new node
    # - make new node's prev the current node
    # - make new node's next the current node's (old) next
    # - make sure the node after the new node points back to the new node, not to the current node
    
    # Note that we'd have even more to think about if we didn't get to assume the list has i nodes in it already.
    # If the node we're inserting is at the end of the list, we need to be careful about grabbing the thing after it, because it doesn't exist!
    
    next = cur.next
    new_node = Node(value, cur, next)
    next.prev = new_node
    cur.next = new_node
```