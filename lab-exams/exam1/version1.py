def find_missing_number(l):
    # TODO: Fill in this function. Your function should return the "missing" number in l, and it should find it by performing a binary search.
    # You may assume l is a list of consecutive numbers, starting at 0, with one number missing.
    # Examples: [0,1,2,3,5], [0,1,2,3,4,6,7,8,9], [0,1,2,3,5,6]

    # Hint: it's not obvious this is a binary search, but it is!
    # You can tell whether to look right or left from the midpoint by whether the
    # number at position m is equal to m! If it is, it means we haven't skipped a number yet,
    # so the missing number is on the right. If it isn't, it means we already skipped a number, so
    # the missing number is on the left.
    pass

# ------ TEST CODE: DO NOT MODIFY ------ #
print(find_missing_number([0,1,2,3,5])  # should return 4
print(find_missing_number([0,1,2,3,4,6,7,8,9])  # should return 5
print(find_missing_number([0,1,2,3,4,5,6,7,8,9,10,11,12,14])  # should return 13