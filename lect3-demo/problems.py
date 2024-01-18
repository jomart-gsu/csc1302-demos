# Question 1 - Print the first 10 powers of 2
def powers_of_two(n):
    # having a parameter n wasn't part of the question, but it's a nice opportunity
    # to write generalizable code!
    x = 2
    for i in range(n):  # numbers 0 through n-1, so this loop will run n times
        print(x)
        x *= 2

powers_of_two(5)

# Question 3 - Smallest number in a list
# This structure of "iterate over a list and keep track of the smallest/largest/longest/etc" is EVERYWHERE in coding
def smallest_number(l):
    smallest = None  # we could set smallest as a number to begin with, but what if all the list elements are larger than that?
    for num in l:
        # You can say "is" instead of == for None (or any literal, but it's only recommended for None)
        if smallest is None or num < smallest:  # note how this if statement evaluates to True the first time, no matter what
            smallest = num

    return smallest


# Shorter version
def smallest_number(l):
    return min(l)


# Question 3 - Return the string with the most vowels
def most_vowels(strings):
    most_vowels = 0
    most_vowels_string = ""
    for string in strings:
        vowels = 0

        # count vowels in the string
        for char in string:
            if char in ["a", "e", "i", "o", "u"]:
                vowels += 1

        # replace the max values
        if vowels > most_vowels:
            most_vowels = vowels
            most_vowels_string = string

    return most_vowels_string

print(most_vowels(["foo", "bar", "baz"]))
print(most_vowels(["foo", "baaaar", "baz"]))


# Question 4 - Second smallest element
def second_smallest(l):
    """
    This is just like Question 2, but with a more complicated update step.
    """
    smallest = None
    second_smallest = None
    for num in l:
        # we need <= and not < because if there's a tie for smallest, then that same number is also the second smallest
        if smallest is None or num <= smallest:
            # what would happen if we swapped these lines?
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num

    return second_smallest

print(second_smallest([1,2,3,4,5,6]))
print(second_smallest([7,6,5,4,3,2]))


# Question 5 - Almost a Palindrome?
def almost_palindrome(s):
    """
    This question is very challenging!

    For context, the rule is we should return True if:
        s is a palindrome like "kayak" OR
        s is a palindrome with one extra letter like "kagyak" or "kayakg"

    Strategy: we're going to check for a palindrome just like we did last class.
    But if we find mismatched letters, either letter might be the extra letter, so we
    check if each letter matches the next letter over
    """
    i = 0
    j = len(s) - 1
    skipped = False
    while i < j:
        if s[i] != s[j]:
            # You only get to skip one letter, so as soon as we pass this check,
            # we shut the door behind us.
            if skipped:
                return False
            skipped = True
            # skip index i if i+1 matches j
            if s[i+1] == s[j]:
                i += 1
            # otherwise, skip index j
            elif s[i] == s[j-1]:
                j -= 1
            # if there's no way to match both letters, can return False immediately
            else:
                return False
        i += 1
        j -= 1
    # if we finish the while loop without finding an error, we can just return True
    return True

print(almost_palindrome("kayak")) # True
print(almost_palindrome("kabyak")) # True
print(almost_palindrome("krayagk")) # False
print(almost_palindrome("kayakg")) # True