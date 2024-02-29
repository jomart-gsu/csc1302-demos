# SECTION 1: Intro Big-Oh
Find the big-Oh time and space complexity of the below functions

## 1
```
def print_stuff():
    print("Woohoo!")
    print("Moo!")
    print("Kangaroo!")
```

*Print statements execute in constant (O(1)) time, and there's a constant number of them, so the time complexity is O(1).*

*No additional space is allocated, so the space complexity is also O(1).*
## 2
```
def add_stuff(n, m):
    s = n + m
    return s
```
*Arithmetic operations also take constant time, so the time complexity is O(1).*

*We allocate space for one additional variable, which is a constant number, so the space complexity is O(1).*
## 3
```
def divide_stuff(n, m, z):
    s = n / m
    z = m / s
    return z
```
*This problem is the same as the previous one -- division and other arithmetic operations are O(1) time, and a constant number of variables are declared.*
## 4
```
def count_vowels(s):
    vowels = 0
    for char in s:
        if char in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return vowels
```
*Here things get a little interesting. All lines of code take constant time, but the `for` loop executes once for every character in `s`. So the time complexity is O(n), where n is the number of characters in `s`.*

*The space complexity remains O(1). We allocate some amount of space for `vowels` and the list of vowels, but none of it depends on the input.*
## 5
```
def print_everything_10_times(l):
    for item in l:
        for i in range(10):
            print(item)
```
*We execute the inner for loop once for every item in `l`, so the number of steps is on the order of `10n`, where `n` is the length of `l`. However, we know that we simplify out constants, and 10n is O(n), so the time complexity is O(n)*

*Print statements and the range() operator take constant space as of Python 3, so the space complexity is O(1).*

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
*Here we have a while loop that iterates until `i` catches up to `n`, and `i` increments by 1 every time. Appending to the list and incrementing `i` are constant time operations, so the time complexity is `O(n)`, where `n` is, well, `n`.*

*In addition, we are creating a list of length `n`, and constant other variables, so the space complexity is `O(n)` as well.*

## 7
```
def pairs(l):
    res = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            res.append((l[i], l[j]))
    return res
```
*Here we have the dreaded nested `for` loop. The inner loop starts at `i`, so it won't span the entire list every time (once `i` is on the last item in `l`, the inner loop won't run at all!), but that just means the inner loop will run `n + (n-1) + (n-2) + ... + 1` times, where `n` is the length of `l`. As we saw in class, that works out to O(n^2) time complexity.*

*We append to `res` every iteration of the inner loop, so the space complexity is the same as the time complexity: O(n^2).*

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
*This is almost identical to an example we did in class. The triply-nested `for` loop means the list gets appended to `n^3` times, where `n` is the length of `l`, so the time complexity is O(n^3).*

*By a similar argument, the space complexity is O(n^3) as well, because `result` grows by 1 every time the inner for loop executes, and that happens n^3 times.*

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
*This is the same example as the previous one, but `result` is instantiated on a different line. The time complexity is unaffected and remains O(n^3).*

*However, `result` now gets overwritten every time `i` increments, so it only ever gets as large as one pass through the two inner loops will allow. In typical nested `for` loop fashion, the `j` and `k` loops result in n^2 operations before `i` increments, so the space complexity is only O(n^2) this time. Thanks garbage collection!*

## 3
```
def print_distinct_pairs(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] != l[j]:
                print(f"{l[i]} {l[j]}")              
```
*This example is almost the same as problem 7 in the previous section, and by a similar argument, the time complexity is O(n^2). Note that it doesn't matter if the inner loop starts at `i` or `i+1` (or even `i+70`) -- it's still a "triangle sum" and works out to n^2.*

*Only constant additional space is allocated here (no lists or strings or collections), so the space complexity is O(1).*

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
*This loop displays the power of exponential growth - `i` doubles every time! That means it will run `log2(n)` times before `i >= len(l)`, so we will append to `res` as many times. That makes both the time AND space complexity O(log n), where `n` is the length of `l`.*

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
*This example is the same as the previous one. Instead of doubling, `i` gets multiplied by 8/7. However, that's still exponential growth, albeit at a different rate! The loop will run log-base-8/7(n) times, but log bases don't matter for big-Oh notation, so the time and space complexity is still O(log n).*

## 6
```
def triangles(l):
    for i in range(100):
        for j in range(i):
            print("*" * j)       
```
*This looks like one of those triangle sums, but observe that the input `l` isn't actually used anywhere in the function! In fact, if you count, the inner loop will print 0 times when `i` is 0, then 1 time when `i` is 1, and so on until `i` is 100... but that's just a large sum of constant factors (it works out to something like 5000), which is itself a constant, so the time complexity is O(1).*

*We allocate constant numbers of variables here, so the space complexity is O(1) as well.*

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
*This function iterates through a list of numbers until it finds an even number, so the best case is that the first number is even, and the worst case is that none of them are. That means the time complexity in the best case is O(1) and in the worst case it's O(n).*
## 2
```
def double_search(l, num1, num2):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == num1 and l[j] == num2:
                return True
    return False  
```
*This function searches a list for two numbers at once by checking all distinct pairs of numbers in the list. As with many search algorithms, in the best case, we find what we're looking for right away (on the first pair), and in the worst case, we don't find the numbers at all (so both loops run to their full extent). That makes the time complexity O(1) in the best case and O(n^2) in the worst case.*

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
*This function is just selection sort with a twist! It keeps a `need_swap` flag that becomes True if we find two out-of-order elements, but if it stays False for the whole `for` loop, we know the list is already sorted. This means selection sort can terminate early if it ever realizes the list has been sorted, instead of having to go through the whole O(n^2) steps it usually takes. In the best case, we'll loop over the input list one time, discover it's already sorted, and stop, so the best case time complexity is O(n) where n is the length of `l`, and the worst case time complexity is O(n^2), just as with normal selection sort.*

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
*This function looks like a variant of bubble sort, with the weird additional condition that we immediately stop and return `l` if we ever find two elements where the left element is not greater than the one on the right. Additionally, we only scan up to the `j`th element in the list in each "pass" of the loop (the astute reader will note that this algorithm doesn't necessarily even sort the list, even if it runs all the way through without returning early. Strange indeed!)*

*It turns out (and this takes some thinking about -- this probably should have been a challenge problem) that this algorithm will only run all the way through (without hitting that early return statement) if `l` is sorted in **descending order**. In that case, we're looking at your typical nested loop (the `if/else` statement inside the `while` will run 0, then 1, then 2, up until n-1 times), so the worst-case time complexity is O(n^2), where n is the length of `l`. In the best case, the first two elements of the list are already in order, and we immediately hit the early return statement, for an O(1) time complexity.
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

*The algorithm runs in O(n^2) time and O(1) space, as written.*

*We can rewrite the algorithm to trade some space for time by keeping track of elements we've seen so far:*
```
def has_two_elements_that_sum_to_zero(l):
    seen = set()  # yep! we're using a set!
    for num in l:
        if -num in seen:  # if we've seen that number's negative, we can return true because x and -x are in the list for some x
            return True
        seen.add(num)  # otherwise, note down that we've seen num and continue
    return False
```

*To improve our time complexity without using additional space, we can sort the list first, then take advantage of the fact that the sum of any two numbers in the sorted list will increase if we move one of the numbers to the right and decrease if we move one of the numbers to the left:*
```
def has_two_elements_that_sum_to_zero(l):
    l.sort()  # in-place, so no extra memory used
    i = 0
    j = len(l) - 1
    while i < j:
        if l[i] + l[j] == 0:
            return True
        elif l[i] + l[j] > 0:
            j -= 1
        else
            i += 1
    return False
```
*The while loop runs in O(n) time because i and j will eventually reach each other after taking a combined n-1 steps, but sorting the list takes O(n log n) time, as we saw in class. So the overall time complexity is O(n log n) and the space complexity stays O(1).*
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

*When I wrote this question, I lazily assumed the complexity was O(2^n) because each recursive call generates two subproblems. Unfortunately, the answer is far more complicated than that. Please check out [this article](https://evoniuk.github.io/posts/fibonacci.html) if you'd like to hear more. I'm going to skip to the second part.*

*If we memoized the code like this:*
```
memo = {}
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    memo[n] = res
    return res
```
*The result would be that we would compute `fibonacci(k)` exactly once for all `k` between 1 and `n` -- and every subsequent time we tried to compute `fibonacci(k)`, memoization would rescue us and make that computation an `O(1)` operation. Moreover, we would only compute `fibonacci(k)` one other time after initially storing it in memo (because the recursive call from `fibonacci(k+1)` would result in computing `fibonacci(k)`, and we would later need it further up the call stack in the second recursive call of `fibonacci(k+2)`. That second lookup would take constant time because we would immediately find `k` in `memo`.*

*If you trace out the tree of recursive calls, you'll find that every single `fibonacci(n-2)` call ends up returning a memoized result, so the tree is really a single line starting at `n` and going down to 1, then back up. The time complexity ends up being O(n) - an incredible improvement!*

*What does this mean? In general, in computer science, there's a tradeoff between CPU and memory - we can write faster algorithms by using more memory to store intermediate results or other helpful data, but if memory is scarce, we're stuck computing more things from scratch more often, and our time complexity suffers!*