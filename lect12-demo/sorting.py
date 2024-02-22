def bubble_sort(l):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                did_swap = True
    return l

print(bubble_sort([1,4,5,2]))

def selection_sort(l):
    for i in range(len(l)):
        smallest = float("inf") # this is Python's EXTREMELY strange way of saying "infinity"
        smallest_index = -1
        for j in range(i, len(l)):
            if l[j] < smallest:
                smallest = l[j]
                smallest_index = j
            l[i], l[smallest_index] = l[smallest_index], l[i]
    return l  # technically you don't need to return from an in-place sort function, but it will make the testing code simpler

print(selection_sort([1,3,5,4,2]))

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        tmp = l[j]
        while j > 0 and tmp < l[j-1]:
            l[j] = l[j-1]  # shift the element right
            j -= 1
        l[j] = tmp
    return l

print(insertion_sort([1,3,5,4,2]))



