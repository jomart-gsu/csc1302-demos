def smart_selection_sort(l):
    # TODO: implement in-place selection sort in the function below. Your function should modify l so that it is sorted at the end.

    # However, there is a twist! Recall that the best case runtime for selection sort
    # is O(n^2) because even if the list is already sorted (or close to sorted), the algorithm
    # will still pass through the list n times finding each successive next-smallest element.

    # Your task is to add logic to selection sort so that it can detect when the list is sorted
    # and stop early when that is the case. In other words, if after putting the third-smallest element in place,
    # your list is sorted, your algorithm should not bother finding and moving the fourth-smallest element.

    # Your algorithm should run in O(n) time in the best case.
    pass

# ------ TEST CODE: DO NOT MODIFY ------ #

# all outputs should be [1,2,3,4,5]
l1 = [4,2,3,1,5]
smart_selection_sort(l1)
print(l1)

l2 = [4,3,2,1,5]
smart_selection_sort(l2)
print(l2)

l3 = [1,2,3,4,5]
smart_selection_sort(l3)
print(l3)