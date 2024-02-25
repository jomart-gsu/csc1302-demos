def binary_search(my_list, target):
    l = 0
    h = len(my_list) - 1
    while l < h:
        m = (l + h) // 2
        if my_list[m] == target:
            return True
        elif my_list[m] < target:
            l = m+1
        else:
            h = m-1

    if my_list[l] == target:
        return True
    return False


print(binary_search([2,4,6,8,10], 2))
print(binary_search([2,4,6,8,10], 3))
print(binary_search([2,4,6,8,10], 6))


def binary_search_recursive(my_list, target):
    def helper(my_list, target, l, h):
        if l >= h:
            return my_list[l] == target

        m = (l + h) // 2
        if my_list[m] == target:
            return True
        elif my_list[m] < target:
            return helper(my_list, target, m+1, h)
        else:
            return helper(my_list, target, l, m-1)

    return helper(my_list, target, 0, len(my_list) - 1)

print(binary_search_recursive([2,4,6,8,10], 6))