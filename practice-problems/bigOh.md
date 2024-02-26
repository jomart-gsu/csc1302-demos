# SECTION 1: Intro Big-Oh
Find the big-Oh time and space complexity of the below functions

## 1
```
def print_stuff():
    print("Woohoo!")
    print("Moo!")
    print("Kangaroo!")
```
## 2
```
def add_stuff(n, m):
    s = n + m
    return s
```
## 3
```
def divide_stuff(n, m, z):
    s = n / m
    z = m / s
    return z
```
## 4
```
def count_vowels(s):
    vowels = 0
    for char in s:
        if char in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return vowels
```
## 5
```
def print_everything_10_times(l):
    for item in l:
        for i in range(10):
            print(item)
```

## 6
```
def range_but_slow_and_bad(n):
    i = 0
    res = []
    while i < n:
        res.append(i)
        i += 1
    return res
```

## 7
```
def pairs(l):
    res = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            res.append((l[i], l[j]))
    return res
```
# SECTION 2: Advanced Big-Oh
Find the big-Oh time and space complexity of the below functions
## 1
```
def blah(l):
    result = []
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                result.append(l[i] + l[j] - l[k])
    return result                
```

## 2
```
def blah(l):
    for i in range(len(l)):
        result = []
        for j in range(len(l)):
            for k in range(len(l)):
                result.append(l[i] + l[j] - l[k])
    return result                
```

## 3
```
def print_distinct_pairs(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] != l[j]:
                print(f"{l[i]} {l[j]}")              
```

## 4
```
def a_strange_loop(l):
    res = []
    i = 1
    while i < len(l):
        i *= 2
        res.append(l[i])
    return res              
```

## 5
```
def a_stranger_loop(l):
    res = []
    i = 0
    while i < len(l):
        i = i * 8 // 7
        res.append(l[i])
    return res              
```

## 6
```
def triangles(l):
    for i in range(100):
        for j in range(i):
            print("*" * j)       
```

# SECTION 3: Best/Worst/Average Case
For each algorithm below, describe the best and worst case, and the big-Oh time complexity for both.

## 1
```
def iterate_until_even(l):
    for num in l:
        if num % 2 == 0:
            return num
    return None  
```

## 2
```
def double_search(l, num1, num2):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == num1 and l[j] == num2:
                return True
    return False  
```

## 3
```
def smart_selection_sort(l):
    i = 0
    need_swap = True
    while i < l and need_swap:
        need_swap = False
        ith_min = l[i]
        ith_min_idx = i
        last = l[i]
        for j in range(i, len(l)):
            if l[j] < ith_min:
                ith_min = l[j]
                ith_min_idx = j
            if l[j] < last:
                need_swap = True
            last = l[j]
        
        l[ith_min_idx], l[i] = l[i], l[ith_min_idx]
        i += 1
    return l
             
```

## 4
```
def weird_sort(l):
    for j in range(len(l)):
        i = 0
        while i < j:
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
            else:
                return l
            i += 1
    return l   
```
# SECTION 4: Challenge Problems
These problems are just here if you REALLY want to push yourself -- none of the exam questions will be at this level.

## 1
Consider the following code:
```
def has_two_elements_that_sum_to_zero(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
```
 - What is the big-Oh time and space complexity of this algorithm?
 - Can you rewrite the algorithm so that it has O(n) time and O(n) space?
 - Can you rewrite the algorithm so that it has better than O(n^2) time and O(1) space?

## 2
Consider the following un-memoized recursive function:
```
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```
- What is the big-Oh time and space complexity of this algorithm?
- What would the big-Oh time and space complexity of this algorithm be if we added memoization? What does this tell you about how time and space complexity interact?