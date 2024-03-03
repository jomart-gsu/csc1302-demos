# SECTION 1: Sets
1. Write a function `dedupe(l)` that takes a list of numbers `l` and returns a list of unique elements in `l` (i.e. numbers that only appear once) (yes we did this in class).
2. Write a function `overlap(l1, l2)` that takes two lists of numbers `l1` and `l2` and returns a list of all the numbers that appear in both `l1` and `l2`. Your function should run in `O(n)` time.
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
5. Describe the bug in the following snippet of code:
```
s1 = {1,2,3}
s2 = {4,5,6}
set_of_sets = {s1, s2}
```

# SECTION 2: Stacks
1. Describe the bug in the following snippet of code:
```
stack = []
stack.push(1)
stack.pop()
stack.pop()
```

2. Write a function `is_balanced(s)` that takes a string `s` and returns `True` if its parentheses are balanced and `False` otherwise. For example, `is_balanced("(abc)()((a)b)")` would return `True` because all open parens have a subsequent closing paren, and vice versa.
3. *CHALLENGE:* Write a function `balance(s)` that takes a string and makes its parentheses balanced by removing as few parentheses as possible. For example, `balance("a(abc(())") might return `"a(abc())"`.

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
2. Identify the big-Oh time complexity of the following code:
```
def append_to_linked_list(head, value):
    if head is None:
        return Node(value)
    while head.next is not None:
        head = head.next
    head.next = Node(value)
```
3. Describe the bug in the following code:
```
def remove_last_element_of_linked_list(head):
    if head is None:
        return
    while head.next is not None:
        head = head.next
    head.next = None
```
4. Write a function `insert_at_position(head, value, i)` that inserts a node with value `value` at the `i`th position in a linked list `head`. You can assume the list starting at `head` has at least `i` values.
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