"""
Writing out solutions manually. Note that the 4 stair solutions starting with 1 look suspiciously
like the 3 stair solutions :o
2 stairs
1 1
2


3 stairs
1 1 1
1 2
2 1

4 stairs

1 1 1 1
1 1 2
1 2 1

2 1 1
2 2
"""

def climbing_stairs(n):
    """
    Number of ways to climb n stairs taking them 1 or 2 at a time
    """
    if n == 2:
        return 2
    if n == 1:
        return 1

    return climbing_stairs(n-1) + climbing_stairs(n-2)



def iterative_fib(n):
    i = 0
    prev1 = 1
    prev2 = 1
    while i < n:
        if i == 0:
            print(1)
        elif i == 1:
            print(1)
        else:
            new_num = prev1 + prev2
            prev2 = prev1
            prev1 = new_num
            print(new_num)

        i += 1


def recursive_fib(n):
    if n == 1 or n == 2:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

def memoized_fib(n):
    memo = {}
    return helper(n, memo)

def helper(n, memo):
    """
    Return the nth fibonacci number
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n in memo:
        return memo[n]

    res = helper(n-1, memo) + helper(n-2, memo)
    memo[n] = res
    return res


# BONUS: What if our goal is to print the first N numbers??
def recursive_print_fib(n):
    """
    It's actually pretty hard to print the first n Fibonacci numbers recursively.

    Think about it: how do you stop the recursive calls from also printing their numbers?

    We should probably just memoize the solution and then print from our stash of computed solutions.
    """
    memo = {}
    helper(n, memo)
    print(sorted(m.values()))

