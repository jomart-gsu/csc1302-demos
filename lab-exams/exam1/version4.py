def bigger_bubble_sort(l):
    # TODO: implement bubble sort in the function below. Your function should modify l so that it is sorted at the end.

    # However, there is a twist! Recall that in normal bubble sort, we swap adjacent PAIRS
    # of elements if they are out of order

    # Your task is to make the "bubbles" larger by looking at THREE elements at a time, and reordering them
    # to be correctly sorted as you move through the list.

    # For example, the first operation of bubble sort on this list would be:
    #
    #       (i  j)             5 and 4 are swapped because 4 < 5
    #    1  (5  4)  6  9  3

    # Your algorithm should look at blocks of three numbers and reorder them appropriately
    #
    #    (i  j  k)           1, 5, 4 is reordered as 1, 4, 5 so that l[i] <= l[j] <= l[k]
    #    (1  5  4)  6  9  3
    pass

# ------ TEST CODE: DO NOT MODIFY ------ #

# all outputs should be [1,2,3,4,5,6,7,8,9]
l1 = [4,2,3,1,5,7,9,6,8]
bigger_bubble_sort(l1)
print(l1)

l2 = [4,8,3,6,2,9,7,1,5]
bigger_bubble_sort(l2)
print(l2)

l3 = [7,8,6,1,2,3,4,5,9]
bigger_bubble_sort(l3)
print(l3)