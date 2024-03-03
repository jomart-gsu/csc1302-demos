########################################################################
#                           README
########################################################################

# Merge sort and Quicksort are DIFFICULT. In addition to using sneaky recursion
# and some tricky non-recursive algorithmic steps, we have to do them in-place
# as much as possible (that is, without creating new lists) to ensure they're
# memory efficient (and time efficient in practice, although the big-Oh time complexity
# isn't affected).

# The algorithms get harder to understand when we take steps to make them in-place.
# Therefore, in the below, I have written two versions of each algorithm: one that is
# slightly inefficient, but easier to understand, and one that is more efficient (still not
# fully optimized, but pretty good).

# The second versions match the code from the slides better. However, you should read the
# first versions to get a handle on how the algorithm works, if you're still less than clear
# on that. Good luck!

########################################################################
#                           MERGE SORT
########################################################################

# Original merge algorithm from class
def merge(listA, listB):
    result = []
    i = j = 0
    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1

    while i < len(listA):
        result.append(listA[i])
        i += 1

    while j < len(listB):
        result.append(listB[j])
        j += 1
    return result

# This is the merge sort that results from the above merge() algorithm.
# Note that it requires creating a lot of copies of list slices. As a result, it isn't very efficient.
# In particular, while it does still achieve O(n log n) runtime, it now also requires O(n log n) space,
# where the below will only require O(n) additional space (you're going to have to trust me on this --
# these comments are already very long).
def merge_sort_inefficient(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort_inefficient(arr[0:mid])
    right_half = merge_sort_inefficient(arr[mid:len(arr)])
    return merge(left_half, right_half)

print(merge_sort_inefficient([5,4,3,2,1]))



# Merge algorithm rewritten to use indices within a single list as start points for the "two" sorted lists.
# So, we're treating the segment starting at a and the segment starting at b as the two sorted lists.
# Before this algorithm, arr[a:b] and arr[b:c+1] are sorted. After the algorithm, arr[a:c+1] will be sorted.
# The above uses list slice syntax, so [b:c+1] means "from the element at b to the element at c, inclusive" (arr[c+1] is not included).
def merge(arr, a, b, c):
    result = []
    # we need separate variables because if we reassign a and b, the while loop conditions won't make
    # sense anymore
    i = a
    j = b
    while i < b and j <= c:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    while i < b:
        result.append(arr[i])
        i += 1

    while j <= c:
        result.append(arr[j])
        j += 1

    # write the merged piece into arr
    for k in range(len(result)):
        arr[a+k] = result[k]



# Now we're ready to write a merge sort that works in-place, mostly.
# We still need to allocate an additional array to store the results of the merge() step,
# but that keeps our additional space usage at O(n).

# How do you choose a and b initially? They should always be 0 and the len(arr) - 1. That
# tells the algorithm that you want to sort the WHOLE array.
def merge_sort(arr, a, b):
    if a < b:
        mid = (a + b) // 2
        merge_sort(arr, a, mid)
        merge_sort(arr, mid+1, b)
        merge(arr, a, mid+1, b)

arr = [5,4,3,2,1]
merge_sort(arr, 0, 4)
print(arr)


########################################################################
#                           QUICKSORT
########################################################################


# same structure - I'll show an inefficient but easy-to-read quicksort, then a more "in-place" one.
def partition_simple(arr):
    # choose our pivot to be the end of the array
    end = len(arr) - 1
    pivot = arr[end]

    # this loop takes a while to understand. k is going to represent the number of elements
    # we've found that are smaller than the pivot. so when we find such a number, we move it
    # to the kth spot, then increment k.
    i = 0
    k = 0
    while i < len(arr)-1:
        if arr[i] < pivot:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
        i += 1

    # because of how we wrote the above, the pivot now belongs at position k, and arr[k] > pivot,
    # so it's okay to swap to the end
    arr[k], arr[end] = arr[end], arr[k]

    return k  # need to return k so we know how to slice up the array later

arr = [11,12,1,9,6,5,4,7]
partition_simple(arr)
print(arr)


# Based on that, we can write a copy-heavy quicksort.
# For the same reasons as above, this uses O(n log n) space.
def quicksort_simple(arr):
    if len(arr) <= 1:
        return arr

    k = partition_simple(arr)
    return quicksort_simple(arr[0:k]) + [arr[k]] + quicksort_simple(arr[k+1:])


print(quicksort_simple([5,4,3,2,1]))


# To call partition() repeatedly without making new copies of slices of arr, we need to augment
# it with a range (low, high) that says we're just focusing on arr[low:high] right now.
# The algorithm itself is pretty much the same.
def partition(arr, low, high):
    pivot = arr[high]

    i = low
    k = low
    while i < high:
        if arr[i] < pivot:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
        i += 1

    arr[k], arr[high] = arr[high], arr[k]

    return k


# Same rule for choosing low and high as above - their initial values should be the endpoints
# of the list you want to sort!
def quick_sort(arr, low, high):
    if low < high:
        k = partition(arr, low, high)
        quick_sort(arr, low, k-1)
        quick_sort(arr, k+1, high)

arr = [11,12,1,9,6,5,4,7]
quick_sort(arr, 0, 7)
print(arr)
