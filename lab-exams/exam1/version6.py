def alternating_selection_sort(l):
    # TODO: implement in-place selection sort in the function below. Your function should modify l so that it is "sorted" at the end.

    # However, there is a twist! Here, "sorted" means l should start with the smallest element, but the next element should be the
    # largest element, then the second smallest, then the second largest, etc.

    # You should achieve this with a slight modification of selection sort.

    pass

# ------ TEST CODE: DO NOT MODIFY ------ #


l1 = [4,2,3,1,5]
smart_selection_sort(l1)
print(l1)  # should be [1,5,2,4,3]

l2 = [4,3,2,1,6,7,5]
smart_selection_sort(l2)
print(l2)  # should be [1,7,2,6,3,5,4]